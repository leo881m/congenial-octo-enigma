from pydantic import BaseModel
from fastapi import FastAPI
import random

app = FastAPI()

class Item(BaseModel):
    nome: str
    preco: float


@app.get("/")
async def read_root() -> object:
    return {"Hello": "World"}

@app.get("/teste")
async def funcaoteste():
    return {"teste": True, "numeroAleatorio": random.randint(1,2000)}

@app.post("/items/{item_id}")
def create_item(item_id: int, item: Item):
    db[item_id] = item
    return {"message": "Item criado", "item": item}

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    if item_id not in db:
        return {"erro": "Item não encontrado"}
    db[item_id] = item
    return {"message": "Item atualizado", "item": item}

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    if item_id not in db:
        return {"erro": "Item não encontrado"}
    
    del db[item_id]
    return {"message": "Item deletado"} 
