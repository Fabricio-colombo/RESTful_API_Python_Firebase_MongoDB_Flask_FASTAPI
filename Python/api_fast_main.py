from fastapi import FastAPI
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_config_FASTAPI import caminho_secret
from pymongo import MongoClient
from bson import ObjectId

app = FastAPI()

def conectar_mongodb():
    MONGO_URI = "mongodb://localhost:27017/"
    DB_NAME = "Books"
    COLLECTION_NAME = "Non-Fiction"

    client = MongoClient(MONGO_URI)
    db = client[DB_NAME]
    collection = db[COLLECTION_NAME]
    return collection 

def conectar_firebase():
    cred = credentials.Certificate(caminho_secret)
    firebase_admin.initialize_app(cred, {
        'databaseURL': 'https://books-fiction-go-default-rtdb.firebaseio.com/'
    })
    
def custom_encoder(document):
    if isinstance(document, list):
        return [custom_encoder(item) for item in document]
    if isinstance(document, ObjectId):
        return str(document)
    if isinstance(document, dict):
        return {key: custom_encoder(value) for key, value in document.items()}
    return document

@app.get("/livro_de_ficcao")
def get_books_fiction():
    conectar_firebase()
    ref = db.reference('/livro_de_ficcao')
    return ref.get()

@app.get("/livro_de_nao_ficcao")
def get_books_non_fiction():
    collection = conectar_mongodb()
    books = list(collection.find())
    return custom_encoder(books)

@app.post("/livro_de_ficcao")
def add_book_fiction(title: str, author: str, language: str, pages: int, rating: float, year: int):
    try:
        conectar_firebase()
        ref = db.reference('/livro_de_ficcao')
        new_book_ref = ref.push()
        new_book_ref.set({
            'title': title,
            'author': author,
            'language': language,
            'pages': pages,
            'rating': rating,
            'year': year
        })
        return {"message": "Livro de ficção adicionado com sucesso"}
    except Exception as e:
        return {"error": str(e)}


@app.get("/")
def home():
    return "Bem-vindo à API de Livros! Esta é uma API para consultar livros de ficção que estão no banco de dados do Firebase, e livros de não ficção no banco de dados MongoDB."




