from pydantic import BaseModel
from schemas import Category
from typing import Optional
from fastapi import Query

class Item(BaseModel):
    id: int
    name: Optional[str]
    price: Optional[float]
    count: Optional[int]
    category: Optional[Category]

class query_Item(BaseModel):
    id: Optional[int] = Query(None, description="Id of the item")
    name: Optional[str] = Query(None, max_length=20, description="Name of the item")
    price: Optional[float] = Query(None, description="Price of the item")
    count: Optional[int] = Query(None, description="Amount of items")
    category: Optional[Category] = Query(None, description="Item's category")