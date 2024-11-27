from fastapi import FastAPI
from get_themes import read_themes
from themes_schema import themes_schema

app = FastAPI()

@app.get("/penjat/tematica/opcions", response_model=list[dict])
async def get_themes():
    return themes_schema(read_themes())