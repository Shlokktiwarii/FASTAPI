from fastapi import FastAPI
import asyncio
import time

app = FastAPI()

async def async_task(i):
    await asyncio.sleep(1)
    return f"async-{i}"


def sync_task(i):
    time.sleep(1)
    return f"sync-{i}"


@app.get("/async")
async def async_endpoint():
    await asyncio.sleep(5)  # Simulate a long-running task
    return {"message": "This is an async endpoint!"}

@app.get("/sync")
async def sync_endpoint():
    time.sleep(5)  # Simulate a long-running task
    return {"message": "This is a sync endpoint!"}



@app.get("/sync")
def sync_endpoint():
    time.sleep(5)  # Simulate a long-running task
    return {"message": "This is a sync endpoint!"}


@app.get("/async-multiple")
async def async_multiple_endpoint():
    tasks = [asyncio.create_task(async_task(i)) for i in range(5)]
    results = await asyncio.gather(*tasks)
    return {"results": results}


@app.get("/sync-multiple")
def sync_multiple_endpoint():
    results = [sync_task(i) for i in range(5)]
    return {"results": results}
