from llama_index.core import Settings
from llama_index.llms.ollama import Ollama


from llama_index.core import PromptTemplate

template = (
    "We have provided context information below. \n"
    "---------------------\n"
    "{context_str}"
    "\n---------------------\n"
    "Given this information, please answer the question: {query_str}\n"
)
qa_template = PromptTemplate(template)



Settings.llm = Ollama(model="llama3", request_timeout=360.0, json_mode=True)
