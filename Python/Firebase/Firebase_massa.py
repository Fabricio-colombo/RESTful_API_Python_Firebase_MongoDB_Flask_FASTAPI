import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_config import caminho_secret
from books_fiction import novos_livros

cred = credentials.Certificate(caminho_secret)

firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://books-fiction-go-default-rtdb.firebaseio.com/'
})

ref = db.reference('/')

for livro in novos_livros:
    ref.child('livro_de_ficcao').push(livro)

print("Livros de ficção adicionados com sucesso!")


# A lista de dicionarios contendo os livros de ficção estão no arquivo books_fiction para melhor organização do codigo.
