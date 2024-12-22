from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from crud.get_from_table import hangman_get, info_pantalla_get, usuari_joc_data_get
from crud.insert_into_table import usuari_insert, registre_joc_insert, hangman_insert, info_pantalla_insert
from crud.update_table import registre_joc_update, hangman_update, paraula_secreta_update
from crud.delete_from_table import usuari_delete
from schema.usuari_schema import usuaris_schema

app = FastAPI()

# Middleware per quan es vulgui conectar al frontend en javascript
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# L'usuari del joc
class Usuari(BaseModel):
    username: str
    password: str

# Les dades de la partida de cada jugador
class RegistreJoc(BaseModel):
    usuari_id: int
    punts_actuals: int
    total_partides: int
    partides_guanyades: str
    highscore: str

# La paraula secreta a jugar triada aleatoriament segons el THEME triat
class ParaulaSecreta(BaseModel):
    paraula: str

# La imatge del hangman o el nombre d'intents restants
class Hangman(BaseModel):
    img: str

# GET ENDPOINTS

@app.get("/boto_inici", response_model=str)
async def get_boto_inici():
    return info_pantalla_get.get_boto_inici()

@app.get("/paraula_secreta", response_model=str)
async def get_paraula_secreta():
    return info_pantalla_get.get_paraula_secreta()

@app.get("/hangman_img", response_model=str)
async def get_hangman_img():
    return hangman_get.get_hangman_img()

@app.get("/abecedari", response_model=str)
async def get_abecedari():
    return info_pantalla_get.get_abecedari()

@app.get("/usuari", response_model=list[dict])
async def get_usuari_info():
    return usuaris_schema(usuari_joc_data_get.get_usuari_game_data())

# POST ENDPOINTS

@app.post("/post_hangman")
async def create_hangman(hangman: Hangman):
    return hangman_insert.insert_hangman_img(hangman.img)

@app.post("/post_registre_joc")
async def create_registre_joc(registreJoc: RegistreJoc):
    return registre_joc_insert.insert_registre_joc(registreJoc.usuari_id)

@app.post("/post_usuari/")
async def create_usuari(usuari: Usuari):
    return usuari_insert.insert_usuari(usuari.username, usuari.password)

@app.post("/post_info_pantalla")
async def create_hangman():
    return info_pantalla_insert.insert_info_pantalla()

# PUT ENDPOINTS

@app.put("/put_hangman")
async def put_hangman_img(hangman: Hangman):
    return hangman_update.update_hangman_img(hangman.img)

@app.put("/put_paraula_secreta")
async def put_paraula_secreta(paraulaSecreta: ParaulaSecreta):
    return paraula_secreta_update.update_paraula_secreta(paraulaSecreta.paraula)

@app.put("/put_registre_joc")
async def put_registre_joc(registreJoc: RegistreJoc):
    return registre_joc_update.update_registre_joc(registreJoc.usuari_id, registreJoc.punts_actuals, registreJoc.total_partides, registreJoc.partides_guanyades, registreJoc.highscore)

# DELETE ENDPOINTS

@app.delete("/delete_user")
async def delete_user_by_id(id: int):
    return usuari_delete.delete_usuari(id)