from fastapi import FastAPI
from crud.get_themes import read_themes
from schema.themes_schema import themes_schema
from crud.get_words import read_words_by_theme
from random import randint

app = FastAPI()

@app.get("/penjat/tematica/opcions", response_model=list[dict])
async def get_themes():
    return themes_schema(read_themes())

@app.get("/penjat/tematica/{option}", response_model=list[dict])
async def get_random_word_from_theme(option: str):
    words = read_words_by_theme(option)
    return [{"option":words[randint(0,99)][0]}]
