from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()


class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None


@app.get("/", tags=['root'])
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}", tags=["Item"])
def read_item(item_id: int, q: Union[str, None] = None):
    """
    example url: http://127.0.0.1:8000/items/5?q=somequery.
    """
    return {"item_id": item_id, "q": q}


@app.put("/items/{item_id}", tags=["Item"])
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id, "data": item.__dict__}
