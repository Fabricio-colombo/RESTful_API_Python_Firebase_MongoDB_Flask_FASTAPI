import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_config import caminho_secret

# Carregar as credenciais do arquivo JSON
cred = credentials.Certificate(caminho_secret)

firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://books-fiction-go-default-rtdb.firebaseio.com/'
})

ref = db.reference('/')

novo_livro = {
    'title': 'A Song of Ice and Fire',
    'author': 'George R.R. Martin',
    'year': 1996,
    'pages': 694,
    'language': 'English',
    'rating': 4.8333
}
ref.child('livro_de_ficcao').set(novo_livro)
print("Livro de ficção criado com sucesso!")
