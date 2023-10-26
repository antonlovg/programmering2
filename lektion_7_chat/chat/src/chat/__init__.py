from quart import Quart, render_template, websocket
import asyncio
from chat.broker import Broker

app = Quart(__name__)

def run() -> None:
    app.run()


broker = Broker()

async def _receive() -> None:
    while True:
        message = await websocket.receive()
        await broker.publish(message)

@app.websocket("/ws")
async def ws() -> None:
    try:
        task = asyncio.ensure_future(_receive())
        async for message in broker.subscribe():
            await websocket.send(message)
    finally:
        task.cancel()
        await task

@app.get("/")
async def index():
    return await render_template("index.html")