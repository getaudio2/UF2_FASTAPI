from fastapi import FastAPI
import get_info_pantalla
import get_hangman

app = FastAPI()

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