from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from crud.get_from_table import get_hangman, get_info_pantalla, get_usuari_joc_data
from crud.get_from_table.get_usuari_joc_data import get_usuari_game_data

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/boto_inici", response_model=str)
async def get_boto_inici():
    return get_info_pantalla.get_boto_inici()

@app.get("/paraula_secreta", response_model=str)
async def get_paraula_secreta():
    return get_info_pantalla.get_paraula_secreta()

@app.get("/hangman_img", response_model=str)
async def get_hangman_img():
    return get_hangman.get_hangman_img()

@app.get("/abecedari", response_model=str)
async def get_abecedari():
    return get_info_pantalla.get_abecedari()

@app.get("/usuari", response_model=list)
async def get_usuari_info():
    return get_usuari_game_data()