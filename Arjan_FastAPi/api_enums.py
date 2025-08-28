from pydantic import BaseModel
from schemas import Category

class Item(BaseModel):
    id: int
    name: str
    price: float
    count: int
    category: Category
