from fastapi import FastAPI
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_config import caminho_secret

app = FastAPI()

@app.get("/")
def home():
    return "Bem-vindo à API de Livros! Esta é uma API para consultar livros de ficção que estão no banco de dados do Firebase, e livros de não ficção no banco de dados MongoDB."


#função get /books_fiction que vai ser conectado com o banco de dados do Firebase