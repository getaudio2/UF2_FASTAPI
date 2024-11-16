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

items = {}

# Exercici 2: Mètode GET HTTP que retorna un diccionari amb return
@app.get("/items/")
async def read_item():
    return {"item_id": "1",
            "item_name": "Apple",
            "item_price": "3.0$"}

@app.get("/itemsResponse/{id}", status_code=200)
async def get_item_by_id(id: int, response: Response):
    if id not in items:
        # Exercici 6: mostrar un error 404 amb response si no es troba l'item
        response.status_code = status.HTTP_404_NOT_FOUND
        return "Aquest item no existeix"
    return {"item": items[id]}

@app.get("/itemsHttp/{id}", status_code=200)
async def get_item_by_id(id: int):
    if id not in items:
        # Exercici 7: mostrar l'error amb HTTPException
        raise HTTPException(status_code=404, detail="Aquest item no existeix")
    return {"item": items[id]}

# Exercici 5: Mètode POST que treballa un item tipus BaseModel
@app.post("/itemAdd/", status_code=status.HTTP_201_CREATED)
async def create_item(item: Item):
    items[item.id] = item
    return item