from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/items/")
async def read_item():
    return {"item_id": "1",
            "item_name": "Apple",
            "item_price": "3.0$"}