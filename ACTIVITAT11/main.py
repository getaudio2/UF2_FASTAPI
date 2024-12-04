from fastapi import FastAPI
import get_info_pantalla

app = FastAPI()

@app.get("/boto_inici", response_model=str)
async def get_boto_inici():
    return get_info_pantalla.get_boto_inici()