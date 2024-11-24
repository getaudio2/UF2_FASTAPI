from fastapi import Body, FastAPI
from pydantic import BaseModel, Field, HttpUrl
from users_schema import users_schema
from read_users import read_all

app = FastAPI()

class Item(BaseModel):
    name: str
    surname: str
    age: int
    email: str


@app.get("/users", response_model=list[dict])
async def read_users():
    return users_schema(read_all())