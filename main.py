from starlette.middleware.cors import CORSMiddleware
from models.pydantic_models import QueryRequest, EmailRequest, VisionRequest, CreatorSearchRequest, WebSearchRequest
from vision.run_vision_tool import run_vision_tool
from web_search.web_search import run_web_search_tool
from mail.mail import send_email
from db.setup_db import  database
from typing import Dict, List
from fastapi import FastAPI, HTTPException, WebSocket, WebSocketDisconnect
from search.get_query_engine import get_query_engine, get_test_query_engine
import logging
import sys
import llama_index.core

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))
llama_index.core.set_global_handler("simple")

app = FastAPI()

# CORS Middleware Setup
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

#This dictionary keeps track of active WebSocket connections
active_connections: Dict[str, WebSocket] = {}

@app.on_event("startup")
async def startup():
    await database.connect()
    global query_engine

    # persist_dir = "/var/indexes/persist_dir_23_05_may_20"
    # persist_dir = "/var/indexes/persist_dir_22_50_may_22"
    persist_dir = "/var/indexes/persist_dir_11_39_june_12_free"

    query_engine = await get_query_engine(persist_dir)
    #query_engine = await get_test_query_engine()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

@app.post("/query")
async def run_search_creators_endpoint(request: QueryRequest):
    try:
        print(request.user_id)

        return await query_engine.aquery(request.query)

    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/creator_search")
async def run_search_creators_endpoint(request: CreatorSearchRequest):
    try:
        return await query_engine.aquery(request.query)

    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/vision")
async def run_search_creators_endpoint(request: VisionRequest):
    try:
        print("vision")

        print("request.content_urls")
        print(request.content_urls)

        result = await run_vision_tool(request.content_urls)
        return result

    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail=str(e))


@app.websocket("/ws/{user_id}")
async def websocket_endpoint(websocket: WebSocket, user_id: str):
    print('websocket_endpoint called')
    await websocket.accept()
    active_connections[user_id] = websocket
    try:
        # Keep the connection open.
        while True:
            await websocket.receive_text()
    except WebSocketDisconnect:
        active_connections.pop(user_id, None)

async def send_data_to_user(user_id: str, data: str):
    if user_id in active_connections:
        await active_connections[user_id].send_text(data)

@app.post("/send-data/{user_id}")
async def send_data_endpoint(user_id: str, usernames: List[str]):
    # This endpoint can be used to send a list of usernames to the specified user
    await send_data_to_user(user_id, usernames)
    return {"message": "Data sent successfully."}

##python -m uvicorn main:app --reload --port 8001
