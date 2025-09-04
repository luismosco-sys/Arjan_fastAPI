from fastapi import FastAPI, HTTPException, Depends 
from sqlalchemy.orm import Session
from typing import List

from db_setup import Item, get_db
from schemas_api import  ItemResponse, ItemCreate

app = FastAPI(title="Basic tools deposit API")

#Sample table // SUSPENDED DUE TO RESTRUCTURE TO DB 
# items = {
#     0: Item(name="Hammer", price=9, count=20, id=0, category=Category.TOOLS),
#     1: Item(name="Pliers", price=5.99, count=20, id=1, category=Category.TOOLS),
#     2: Item(name="Nails", price=1.99, count=100, id=2, category=Category.CONSUMABLES),
# }

# ENDPOINTS
@app.get("/")
def root():
    return("Terminal messsage: System Working")

#GET AN ITEM
@app.get("/item/{item_id}", response_model=ItemResponse)
def get_item(item_id:int, db:Session=Depends(get_db)):
    item = db.query(Item).filter(Item.id == item_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Not Found")
    return item

#POST A NEW ITEM 
@app.post("/item", response_model=ItemCreate)
async def add_item(item:ItemCreate, db:Session = Depends(get_db)):
    #Crear nuevo registro
    if db.query(Item).filter(Item.name == item.name).first():
        raise HTTPException(status_code = 404, detail = "Item already registered")

    new_register = Item(**item.model_dump())
    db.add(new_register)
    db.commit()
    db.refresh(new_register)
    return new_register

# UPDATE AN ITEM
@app.put("/item/{item_id}", response_model=ItemResponse)
def update_item(item_id: int, item: ItemCreate, db: Session = Depends(get_db)):
    db_item = db.query(Item).filter(Item.id == item_id).first()
    if not db_item:
        raise HTTPException(status_code=404, detail="Item not found")
    
    for field, value in item.dict().items():
        setattr(db_item, field, value)
    
    db.commit()
    db.refresh(db_item)
    return db_item

#REMOVE AN EXISTING ITEM
@app.delete("/item/{item_id}")
def delete_item(item_id:int, db:Session =Depends(get_db)):
    item = db.query(Item).filter(Item.id == item_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    
    db.delete(item)
    db.commit()
    return{"message":"Item Removed"}

#GET ALL ITEMS
@app.get("/items/", response_model=List[ItemResponse])
def get_all_items(db:Session = Depends(get_db)):
    return db.query(Item).all()