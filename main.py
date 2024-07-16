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

# initialize query engine
query_engine = None

# startup event
@app.on_event("startup")
async def startup_event():
    global query_engine
    persist_dir = "./persist_dir"  # default persist dir from this dir (set to test) 
    # persist_dir = "/Volumes/LaCie/noometic/indexes/7.15.24/_data/persist_dir_11_39_june_12_free" # ken's ssd
    try:
        query_engine = await get_query_engine(persist_dir, eval_mode=False)
        logger.debug("Query engine initialized successfully")
    except Exception as e:
        logger.error(f"Error initializing query engine: {str(e)}")
        raise


    
#### main query endpoint ####
@app.post("/query")
async def run_query(request: QueryRequest):
    try:
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
    except Exception as e:
        logger.error(f"Error processing query: {str(e)}")
        logger.error(traceback.format_exc())
        raise HTTPException(status_code=500, detail=str(e))


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=9090, reload=True)