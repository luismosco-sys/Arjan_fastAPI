from pydantic import BaseModel
from typing import Optional


# class Item(BaseModel):
#     #id:int
#     name:str
#     price:float
#     count:int
#     category:str

class ItemResponse(BaseModel):
    id :int
    name :str
    price :float
    count :int
    category :str

class ItemCreate(BaseModel):
    name : str
    price : float
    count : int
    category : str