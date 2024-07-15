import os
import logging
from openai import OpenAI, AsyncOpenAI
import dotenv; dotenv.load_dotenv()

class BaseConfig:
    def __init__(self, name, log_level=logging.INFO):
        # API settings
        self.OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
        self.configure_logging(name, log_level)

    def configure_logging(self, name, log_level):
        logger = logging.getLogger(name)
        logger.setLevel(log_level)
        if not logger.handlers:
            handler = logging.StreamHandler()
            formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            handler.setFormatter(formatter)
            logger.addHandler(handler)

    def get_openai_client(self):
        return OpenAI(api_key=self.OPENAI_API_KEY)

    def get_async_openai_client(self):
        return AsyncOpenAI(api_key=self.OPENAI_API_KEY)  # Return the asynchronous client