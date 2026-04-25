from src.main import *
from unittest.mock import patch
import pytest


@pytest.mark.asyncio
async def test_root():
    result = await root()
    assert result == {"mensagem": "Hello", "mundo": "World"}


@pytest.mark.asyncio
async def test_funcaoteste():
    with patch("random.randint", return_value=42):
        result = await funcaoteste()
    assert result == {"teste": True, "numeroAleatorio": 42}


@pytest.mark.asyncio
async def test_create_item():
    item_teste = Item(name="Teste", preco=10.0)
    result = await create_item(item_teste)

    # ajuste dependendo do retorno real da função
    assert result == item_teste  


@pytest.mark.asyncio
async def test_update_item_negativo():
    result = await update_item(-5)
    assert result is False


@pytest.mark.asyncio
async def test_update_item_positivo():
    result = await update_item(10)
    assert result is True


@pytest.mark.asyncio
async def test_delete_item_negativo():
    result = await delete_item(-5)
    assert result is False


@pytest.mark.asyncio
async def test_delete_item_positivo():
    result = await delete_item(10)
    assert result is True
