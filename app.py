import os
from fastapi import FastAPI, HTTPException
from starlette.middleware.cors import CORSMiddleware
from search.models import QueryRequest
from search.query_engine import get_query_engine
from search.utils import parse_source_nodes
import uvicorn
import asyncio
import logging
import traceback

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

app = FastAPI()
# CORS Middleware Setup
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Environment setup
ENV = os.getenv('ENV', 'dev')

if ENV == 'dev':
    FREE_PERSIST_DIR = "/Volumes/LaCie/noometic/indexes/7.15.24/_data/persist_dir_11_39_june_12_free"
    PREMIUM_PERSIST_DIR = "/Volumes/LaCie/noometic/indexes/7.15.24/_data/persist_dir_11_39_june_12_premium"
else:
    FREE_PERSIST_DIR = "/var/indexes/persist_dir_11_39_june_12_free"
    PREMIUM_PERSIST_DIR = "/var/indexes/persist_dir_11_39_june_12_premium"

# initialize query engines
free_query_engine = None
premium_query_engine = None

# startup event
@app.on_event("startup")
async def startup_event():
    global free_query_engine, premium_query_engine
    try:
        free_query_engine = await get_query_engine(FREE_PERSIST_DIR, eval_mode=False)
        premium_query_engine = await get_query_engine(PREMIUM_PERSIST_DIR, eval_mode=False)
        logger.debug("Query engines initialized successfully")
    except Exception as e:
        logger.error(f"Error initializing query engines: {str(e)}")
        raise

# Helper function for query processing
async def process_query(query_engine, request: QueryRequest):
    if query_engine is None:
        raise HTTPException(status_code=500, detail="Query engine not initialized")
    
    response = await asyncio.to_thread(query_engine.query, request.query)
    
    if request.parse:
        # If parse is True, return the parsed data
        parsed_nodes = parse_source_nodes(response.source_nodes)
        return {"response": str(response), "query": request.query, "nodes": parsed_nodes}
    else:
        # If parse is False or not provided, return the original response
        return {"response": str(response), "query": request.query, "nodes": response.source_nodes}

@app.post("/query/free")
async def run_free_query(request: QueryRequest):
    try:
        return await process_query(free_query_engine, request)
    except Exception as e:
        logger.error(f"Error processing free query: {str(e)}")
        logger.error(traceback.format_exc())
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/query/premium")
async def run_premium_query(request: QueryRequest):
    try:
        return await process_query(premium_query_engine, request)
    except Exception as e:
        logger.error(f"Error processing premium query: {str(e)}")
        logger.error(traceback.format_exc())
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=9091, reload=True)