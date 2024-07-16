import os
import time
import logging
from dotenv import load_dotenv; load_dotenv()
from base import BaseConfig

from llama_index.llms.openai import OpenAI
from llama_index.embeddings.openai import OpenAIEmbedding
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.core import load_index_from_storage, StorageContext, get_response_synthesizer
from llama_index.core.retrievers import KnowledgeGraphRAGRetriever
from llama_index.core.query_engine import RetrieverQueryEngine
from llama_index.core.postprocessor import LLMRerank

from search.parsers import custom_parse_choice_select_answer_fn

config = BaseConfig("query_engine", log_level=logging.INFO)
logger = logging.getLogger("query_engine")

# Define default parameters
DEFAULT_PARAMS = {
    "llm_model": "gpt-4-turbo",
    "llm_temperature": 0.1,
    "embed_model": "openai",
    # "embed_model": "BAAI/bge-small-en-v1.5",
    "response_mode": "compact",
    "embedding_mode": "hybrid",
    "similarity_top_k": 25,
    "rerank_top_n": 20
}

# Define evaluation parameters (currently same as default)
# Define default parameters
EVAL_PARAMS = {
    "llm_model": "gpt-4-turbo",
    "llm_temperature": 0.1,
    "embed_model": "BAAI/bge-small-en-v1.5",
    "response_mode": "compact",
    "embedding_mode": "hybrid",
    "similarity_top_k": 25,
    "rerank_top_n": 20
}

async def get_query_engine(persist_dir="./persist_dir", eval_mode=False):
    logger.info("Initializing query engine...")
    start_time = time.time()

    os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

    # Choose parameters based on mode
    params = EVAL_PARAMS if eval_mode else DEFAULT_PARAMS

    # Initialize LLM
    llm = OpenAI(temperature=params["llm_temperature"], model=params["llm_model"])

    # Initialize embedding model
    embed_model_name = params["embed_model"]
    if embed_model_name == "BAAI/bge-small-en-v1.5":
        embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-small-en-v1.5")
    elif embed_model_name == "openai":
        embed_model = OpenAIEmbedding()
    else:
        raise ValueError(f"Invalid embedding model: {embed_model_name}")
    logger.debug(f"Embedding model initialized: {embed_model}")

    # Load index and create query engine
    storage_context = StorageContext.from_defaults(persist_dir=persist_dir)
    logger.debug(f"Storage context created: {storage_context}")

    logger.info("Loading index from storage...")
    new_index = load_index_from_storage(storage_context)
    index_load_time = time.time() - start_time
    logger.info(f"Index loaded in {index_load_time:.2f} seconds")

    reranker = LLMRerank(
        top_n=params["rerank_top_n"],
        llm=llm,
        parse_choice_select_answer_fn=custom_parse_choice_select_answer_fn
    )

    query_engine = new_index.as_query_engine(
        llm=llm,
        embed_model=embed_model,
        response_mode=params["response_mode"],
        embedding_mode=params["embedding_mode"],
        similarity_top_k=params["similarity_top_k"],
        node_postprocessors=[reranker],
    )
    logger.debug(f"Query engine created with embed_model: {embed_model}")
    logger.debug(f"Query engine type: {type(query_engine)}")
    logger.debug(f"Query engine attributes: {dir(query_engine)}")

    if eval_mode:
        # Prepare parameters dictionary for evaluation mode
        eval_params = {
            "persist_dir": persist_dir,
            "eval_mode": eval_mode,
            "llm": str(llm),
            "embed_model": str(embed_model),
            "response_mode": params["response_mode"],
            "embedding_mode": params["embedding_mode"],
            "similarity_top_k": params["similarity_top_k"],
            "reranker": str(reranker),
            "parse_function": custom_parse_choice_select_answer_fn.__name__,
            "index_load_time": index_load_time
        }
        return query_engine, eval_params
    else:
        return query_engine
    


def get_test_query_engine():
    os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

    # Initialize LLM
    llm = OpenAI(temperature=0, model="gpt-3.5-turbo-1106")

    # Load index and create query engine
    storage_context = StorageContext.from_defaults(persist_dir="./persist_dir")

    new_index = load_index_from_storage(storage_context)

    query_engine = new_index.as_query_engine(
        response_mode="tree_summarize", 
        embedding_mode="hybrid",
        similarity_top_k=10,
        llm=llm
    )

    return query_engine



KG_EVAL_PARAMS = {
    "llm_model": "gpt-4-turbo",
    "llm_temperature": 0.1,
    "embed_model": "BAAI/bge-small-en-v1.5",
    "response_mode": "compact",
    "embedding_mode": "hybrid",
    "similarity_top_k": 25,
}

# knowledge graph retriever - save for later!
def get_kg_retriever_query_engine(persist_dir="./persist_dir", eval_mode=False):
    logger.debug(f"Initializing KG Retriever with persist_dir: {persist_dir}")
    os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

    params = KG_EVAL_PARAMS

    # Initialize LLM
    llm = OpenAI(temperature=params["llm_temperature"], model=params["llm_model"])

    # Initialize embedding model
    embed_model_name = params["embed_model"]
    if embed_model_name == "BAAI/bge-small-en-v1.5":
        embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-small-en-v1.5")
    elif embed_model_name == "openai":
        embed_model = OpenAIEmbedding()
    else:
        raise ValueError(f"Invalid embedding model: {embed_model_name}")
    logger.debug(f"Embedding model initialized: {embed_model}")

    # build index
    storage_context = StorageContext.from_defaults(persist_dir=persist_dir)
    kg_index = load_index_from_storage(storage_context)
    logger.debug(f"KG Index loaded: {kg_index}")

    # configure retriever
    kg_retriever = KnowledgeGraphRAGRetriever(
        index=kg_index,
        storage_context=storage_context,
        top_k=params["similarity_top_k"],
    )

    # configure response synthesizer
    response_synthesizer = get_response_synthesizer(
        response_mode=params["response_mode"],
    )

    # assemble query engine
    query_engine = RetrieverQueryEngine(
        retriever=kg_retriever,
        response_synthesizer=response_synthesizer
    )

    logger.debug(f"KG Retriever Query Engine created: {query_engine}")

    return query_engine