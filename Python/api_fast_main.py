from fastapi import FastAPI
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_config_FASTAPI import caminho_secret

app = FastAPI()

def conectar_banco():
    cred = credentials.Certificate(caminho_secret)
    firebase_admin.initialize_app(cred, {
        'databaseURL': 'https://books-fiction-go-default-rtdb.firebaseio.com/'
    })

@app.get("/fiction")
def get_books_fiction():
    conectar_banco()
    ref = db.reference('/fiction')
    return ref.get()

@app.get("/")
def home():
    return "Bem-vindo à API de Livros! Esta é uma API para consultar livros de ficção que estão no banco de dados do Firebase, e livros de não ficção no banco de dados MongoDB."
