# API de Pedidos com FastAPI

API simples criada com FastAPI para receber e consultar pedidos.

**Tecnologias:**

* Python
* FastAPI
* Pydantic
* Uvicorn

**Como Rodar:**

1. Clone o repositório.
2. Crie e ative um ambiente virtual (`python -m venv venv`, `.\venv\Scripts\activate`).
3. Instale as dependências (`pip install -r requirements.txt`).
4. Crie um arquivo `.env` (adicione suas chaves API se necessário - *neste projeto não usamos API externa, mas é bom ter o .env no .gitignore*).
5. Rode o servidor (`uvicorn main:app --reload`).
6. Acesse `http://localhost:8000/docs` para interagir.