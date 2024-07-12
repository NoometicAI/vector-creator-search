from llama_index.core.postprocessor import LLMRerank
from llama_index.embeddings.openai import OpenAIEmbedding
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.core import load_index_from_storage
from llama_index.core import StorageContext
import os
from llama_index.llms.openai import OpenAI
from llama_index.core.indices.utils import default_parse_choice_select_answer_fn
import dotenv; dotenv.load_dotenv()
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

def custom_parse_choice_select_answer_fn(answer: str, num_choices: int):
    print('====>>', answer)
    _answer = answer.split('Explanation')[0]
    return default_parse_choice_select_answer_fn(_answer, num_choices)

async def get_query_engine(persist_dir):
    logger.debug(f"Initializing query engine with persist_dir: {persist_dir}")
    
    os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

    # Initialize LLM
    llm = OpenAI(temperature=0.1, model="gpt-4-turbo")

    # Initialize embedding model if using the persist_dir in this directory
    # embed_model = OpenAIEmbedding()
    # Use BAAI model for production persist_dir
    embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-small-en-v1.5")
    logger.debug(f"Embedding model initialized: {embed_model}")

    # Load index and create query engine
    storage_context = StorageContext.from_defaults(persist_dir=persist_dir)
    logger.debug(f"Storage context created: {storage_context}")

    new_index = load_index_from_storage(storage_context)
    logger.debug(f"Index loaded: {new_index}")

    llm_rerank = llm

    reranker = LLMRerank(top_n=20, llm=llm_rerank, parse_choice_select_answer_fn=custom_parse_choice_select_answer_fn)

    query_engine = new_index.as_query_engine(
        llm=llm,
        embed_model=embed_model,
        response_mode="compact",
        embedding_mode="hybrid",
        similarity_top_k=25,
        node_postprocessors=[
            reranker
        ],
    )
    logger.debug(f"Query engine created with embed_model: {embed_model}")
    logger.debug(f"Query engine type: {type(query_engine)}")
    logger.debug(f"Query engine attributes: {dir(query_engine)}")

    return query_engine

def get_test_query_engine():
    os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

    # Initialize LLM
    llm = OpenAI(temperature=0, model="gpt-3.5-turbo-1106")

    # Load index and create query engine
    storage_context = StorageContext.from_defaults(persist_dir="./persist_dir")

    new_index = load_index_from_storage(storage_context)

    query_engine = new_index.as_query_engine(response_mode="tree_summarize", embedding_mode="hybrid",
                                             similarity_top_k=10,
                                             llm=llm)

    return query_engine