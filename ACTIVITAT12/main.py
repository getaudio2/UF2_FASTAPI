from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from crud.get_from_table import get_hangman, get_info_pantalla, get_usuari_joc_data
from crud.insert_into_table import insert_usuari
from schema.usuari_schema import usuaris_schema

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Usuari(BaseModel):
    username: str
    password: str

class RegistreJoc(BaseModel):
    usuari_id: int
    punts_actuals: int
    total_partides: int
    partides_guanyades: str
    highscore: str

@app.put("/put_registre_joc")
async def update_registre_joc(registreJoc: RegistreJoc):

@app.post("/post_usuari/")
async def create_usuari(usuari: Usuari):
    return insert_usuari.insert_usuari(usuari.username, usuari.password)

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

@app.get("/usuari", response_model=list[dict])
async def get_usuari_info():
    return usuaris_schema(get_usuari_joc_data.get_usuari_game_data())