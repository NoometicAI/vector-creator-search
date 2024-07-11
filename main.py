from fastapi import FastAPI, HTTPException
from starlette.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from search.query_engine import get_query_engine  # Adjust this import based on your actual file structure
import uvicorn

PERSIST_DIR = 'persist_dir'

app = FastAPI()

# CORS Middleware Setup
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

class QueryRequest(BaseModel):
    query: str

query_engine = None

@app.on_event("startup")
async def startup_event():
    global query_engine
    query_engine = await get_query_engine(PERSIST_DIR)  # Adjust this based on how your get_query_engine function is defined

@app.post("/query")
async def run_query(request: QueryRequest):
    try:
        if query_engine is None:
            raise HTTPException(status_code=500, detail="Query engine not initialized")
        
        result = await query_engine.aquery(request.query)
        return {"result": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=9090, reload=True)