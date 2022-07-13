from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Produto(BaseModel):
    id: int
    nome: str
    preco: float
    em_oferta: bool = False


produtos = [
    Produto(id=1, nome='Playstation 5', preco=5000.00, em_oferta=True),
    Produto(id=2, nome='Xbox 360', preco=2000.00, em_oferta=True),
    Produto(id=3, nome='Nintendo WII', preco=1000.00),
    Produto(id=4, nome='Playstation 3', preco=3000.00, em_oferta=True),
    Produto(id=5, nome='Super Nintendo', preco=4000.00)
]


@app.get('/')
async def index():
    return {"Geek": "University"}


@app.get('/produtos/{id}')
async def buscar_produtp(id: int):
    for produto in produtos:
        if produto.id == id:
            return produto
        return None


@app.put('/produtos/{id}')
async def atualizar_produto(id: int, produto: Produto):
    for prod in produtos:
        if prod.id == id:
            prod = produto
            return prod
        return None
