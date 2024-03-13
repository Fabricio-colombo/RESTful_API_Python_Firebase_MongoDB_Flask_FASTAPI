from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return "Bem-vindo à API de Livros! Esta é uma API para consultar livros de ficção que estão no banco de dados do Firebase, e livros de não ficção no banco de dados MongoDB."