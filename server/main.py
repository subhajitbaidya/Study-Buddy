from typing import Union
import asyncio
from websockets.asyncio.client import connect
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class UserPrompt(BaseModel):
    prompt: str


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


async def hello():
    await asyncio.sleep(1)  # Wait for server readiness if needed
    async with connect("ws://localhost:8765") as websocket:
        await websocket.send("Hello world!")
        message = await websocket.recv()
        print("Received from WS server:", message)


@app.on_event("startup")
async def startup_event():
    asyncio.create_task(hello())
