import uuid; 
from fastapi import FastAPI
from pydantic import BaseModel  
from typing import List, Optional 
from fastapi import HTTPException

#cria classse com nome e quantidade do produto
class ItemPedido(BaseModel):
    produto_id: str  
    quantidade: int  

# cria classe pedido com itens, nome do cliente e endereco de entrega
class Pedido(BaseModel):
    itens: List[ItemPedido]      
    cliente_nome: Optional[str] = None  
    endereco_entrega: Optional[str] = None 

app = FastAPI()
pedidos_db = {} 
@app.get("/")

# criar funcao read_root entrada da api
def read_root():
    '''END RAIZ - AQUI E PORTA DE ENTRADA DA API'''
    
    return {"message": "Bem-vindo à API de Pedidos!"}
@app.post("/pedidos/", status_code=201)

# criar funcao criar_pedido para receber pedido
async def criar_pedido(pedido: Pedido):
    '''Cria o Pedido e armazena no banco de dados simulado'''
   
    pedido_id = str(uuid.uuid4())
    pedidos_db[pedido_id] = pedido.model_dump()
    print(f"Pedido {pedido_id} recebido e armazenado:", pedidos_db[pedido_id])
    return {"pedido_id": pedido_id, "status": "Pedido criado com sucesso!", "dados_pedido": pedido}


# --- Endpoint para buscar um pedido pelo ID !!! ---


@app.get("/pedidos/{pedido_id}")
async def ler_pedido(pedido_id: str):
    """
    Busca e retorna um pedido específico pelo seu ID.
    Retorna erro 404 se o pedido não for encontrado.
    """
    if pedido_id not in pedidos_db:
        # Se o ID não está no nosso dicionário, retorna erro 404
        raise HTTPException(status_code=404, detail="Pedido não foi encontrado")
    
    # Retorna os dados do pedido encontrado
    return {"pedido_id": pedido_id, "dados": pedidos_db[pedido_id]}
