from fastapi import FastAPI, HTTPException
from starlette.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from search.query_engine import get_query_engine, get_kg_retriever
import uvicorn
import asyncio
import logging
import traceback

app = FastAPI()

# CORS Middleware Setup
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class QueryRequest(BaseModel):
    query: str

query_engine = None

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

@app.on_event("startup")
async def startup_event():
    global query_engine
    persist_dir = "./persist_dir"  # Adjust this path as needed
    try:
        query_engine = await get_query_engine(persist_dir)
        logger.debug("Query engine initialized successfully")
    except Exception as e:
        logger.error(f"Error initializing query engine: {str(e)}")
        raise

@app.post("/query")
async def run_query(request: QueryRequest):
    try:
        if query_engine is None:
            raise HTTPException(status_code=500, detail="Query engine not initialized")
        
        response = await asyncio.to_thread(query_engine.query, request.query)
        return {"response": str(response), "nodes": response.source_nodes}
    except Exception as e:
        logger.error(f"Error processing query: {str(e)}")
        logger.error(traceback.format_exc())
        raise HTTPException(status_code=500, detail=str(e))

# @app.post("/retrieve_nodes")
# async def retrieve_nodes(request: QueryRequest):
#     try: 
#         logger.debug(f"Received node retrieval request: {request.query}")
#         query_engine = await get_kg_retriever("./persist_dir")
#         logger.debug(f"Query engine initialized: {query_engine}")
        
#         response = await asyncio.to_thread(query_engine.query, request.query)
#         logger.debug(f"Query response: {response}")
        
#         # Extract nodes
#         nodes = response.source_nodes if hasattr(response, 'source_nodes') else []
        
#         serializable_nodes = []
#         for node in nodes:
#             serializable_node = {
#                 "node_id": node.node_id,
#                 "text": node.text,
#                 "relationships": [
#                     {"source": rel.source, "target": rel.target, "relation": rel.relation}
#                     for rel in node.relationships
#                 ] if hasattr(node, 'relationships') else [],
#                 "metadata": node.metadata
#             }
#             serializable_nodes.append(serializable_node)
        
#         return {
#             "nodes": serializable_nodes,
#             "metadata": response.metadata if hasattr(response, 'metadata') else {},
#             "response": str(response)
#         }
#     except Exception as e:
#         logger.error(f"Error retrieving nodes: {str(e)}")
#         logger.error(traceback.format_exc())
#         raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=9090, reload=True)
