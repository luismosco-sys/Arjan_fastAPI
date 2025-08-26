from pydantic import BaseModel
from schemas import Category

class Item(BaseModel):
    name: str
    price: float
    count: int
    id: int
    category: Category

