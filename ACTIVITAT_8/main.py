from fastapi import FastAPI, status, Response, HTTPException
from pydantic import BaseModel

class Item(BaseModel):
    id: int
    name: str
    description: str | None = None
    price: float
    quantity: int
    brand: str

app = FastAPI()

items = {1: "patata", 2: "queso"}

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/items/")
async def read_item():
    return {"item_id": "1",
            "item_name": "Apple",
            "item_price": "3.0$"}

@app.get("/items/{id}", status_code=200)
async def get_item_by_id(id: int, response: Response):
    if id not in items:
        response.status_code = status.HTTP_404_NOT_FOUND
        #raise HTTPException(status_code=404, detail="Aquest item no existeix")
    return "Aquest item no existeix"
    #return {"item": items[id]}


@app.post("/itemAdd/", status_code=status.HTTP_201_CREATED)
async def create_item(item: Item):
    items[item.id] = item
    return item