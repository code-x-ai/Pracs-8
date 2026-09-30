import time
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Benchmark Target API")
items = {}

class Item(BaseModel):
    name: str
    price: int

@app.get("/")
def root():
    return {"message": "Benchmark Target API is running"}

@app.get("/fast")
def fast_endpoint():
    return {"status": "ok", "type": "fast", "data": [1, 2, 3, 4, 5]}

@app.get("/slow")
def slow_endpoint():
    time.sleep(0.5)
    return {"status": "ok", "type": "slow"}

@app.post("/items")
def create_item(item: Item):
    item_id = len(items) + 1
    items[item_id] = item.model_dump()
    return {"id": item_id, "item": item.model_dump()}
