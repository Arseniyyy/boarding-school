from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    is_offer: Optional[bool] = None

@app.get('/')
def index():
    return {'data': 'items list'}

@app.get('/items/unpublished')
def unpublished():
    return {'data': 'all unpublished'}

@app.get('/items/{item_id}')
def show(item_id: str, q: Optional[str] = None):
    return {'data': {'item_id': item_id}}

@app.put('/items/{item_id}')
def update_item(item_id: int, item: Item):
    return {'item_name': item.price, 'item_id': item_id}