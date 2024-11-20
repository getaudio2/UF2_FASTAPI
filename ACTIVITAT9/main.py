from fastapi import Body, FastAPI
from pydantic import BaseModel, Field, HttpUrl

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str | None = Field(
        default=None, title="The description of the item", max_length=300
    )
    price: float = Field(gt=0, description="The price must be greater than zero")
    tax: float | None = None


@app.get("/users/")
async def read_users(item_id: int, item: Item):
    results = {"item_id": item_id, "item": item}
    return results