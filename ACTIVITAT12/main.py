from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from crud.get_from_table import get_hangman, get_info_pantalla, get_usuari_joc_data
from crud.insert_into_table import insert_usuari, insert_registre_joc, insert_hangman, insert_info_pantalla
from crud.update_table import update_registre_joc, update_hangman
from crud.delete_from_table import delete_usuari
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

class ParaulaSecreta(BaseModel):
    paraula: str

class Hangman(BaseModel):
    img: str

@app.delete("/delete_user")
async def delete_user_by_id(id: int):
    return delete_usuari.delete_usuari(id)

@app.put("/put_hangman")
async def put_hangman_img(hangman: Hangman):
    return update_hangman.update_hangman_img(hangman.img)

@app.put("/put_info_pantalla")
async def put_paraula_secreta(paraulaSecreta: ParaulaSecreta):
    return paraulaSecreta.paraula

@app.put("/put_registre_joc")
async def put_registre_joc(registreJoc: RegistreJoc):
    return update_registre_joc.update_registre_joc(registreJoc.usuari_id, registreJoc.punts_actuals, registreJoc.total_partides, registreJoc.partides_guanyades, registreJoc.highscore)

@app.post("/post_hangman")
async def create_hangman(hangman: Hangman):
    return insert_hangman.insert_hangman_img(hangman.img)

@app.post("/post_registre_joc")
async def create_registre_joc(registreJoc: RegistreJoc):
    return insert_registre_joc.insert_registre_joc(registreJoc.usuari_id)

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