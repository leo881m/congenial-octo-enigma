from src.main import app, Item, db, read_root, funcaoteste, create_item, update_item, delete_item
from unittest.mock import patch
import pytest

@pytest.mark.asyncio
async def test_root():
    # O nome da função no main.py é read_root
    result = await read_root()
    assert result == {"Hello": "World"}

@pytest.mark.asyncio
async def test_funcaoteste():
    with patch("random.randint", return_value=42):
        result = await funcaoteste()
    assert result == {"teste": True, "numeroAleatorio": 42}

@pytest.mark.asyncio
async def test_create_item():
    # O campo correto é 'nome', não 'name'
    item_teste = Item(nome="Teste", preco=10.0)
    result = create_item(item_id=1, item=item_teste)
    assert result["item"].nome == "Teste"

@pytest.mark.asyncio
async def test_update_item_negativo():
    item_teste = Item(nome="Update", preco=20.0)
    # update_item exige o ID e o objeto Item
    result = update_item(item_id=-5, item=item_teste)
    assert result == {"erro": "Item não encontrado"}

@pytest.mark.asyncio
async def test_delete_item_positivo():
    # Primeiro criamos um item para poder deletar
    db[10] = Item(nome="Deletar", preco=5.0)
    result = delete_item(10)
    assert result == {"message": "Item deletado"}

@pytest.mark.asyncio
async def test_delete_item_negativo():
    result = delete_item(-5)
    assert result == {"erro": "Item não encontrado"}
