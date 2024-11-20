from fastapi import Body, FastAPI
from pydantic import BaseModel, Field, HttpUrl
import users_schema
import read_users

app = FastAPI()

class Item(BaseModel):
    name: str
    surname: str
    age: int
    email: str


@app.get("/users/")
async def read_users():
    return users_schema.users_schema(read_users.read_all())