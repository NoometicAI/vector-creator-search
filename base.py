import os
from openai import OpenAI, AsyncOpenAI
import dotenv; dotenv.load_dotenv()

class BaseConfig:
    def __init__(self, name):
        # API settings
        self.OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

    def get_openai_client(self):
        return OpenAI(api_key=self.OPENAI_API_KEY)

    def get_async_openai_client(self):
        return AsyncOpenAI(api_key=self.OPENAI_API_KEY)  # Return the asynchronous client