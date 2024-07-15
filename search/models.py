from pydantic import BaseModel

class QueryRequest(BaseModel):
    query: str
    parse: bool = False  # Default to False if not provided