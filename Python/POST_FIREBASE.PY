import requests

url = 'http://127.0.0.1:8000/livro_de_ficcao'

livro_ficcao = {
    "title": "A Guerra dos Tronos",
    "author": "George R. R. Martin",
    "language": "Português",
    "pages": 694,
    "rating": 4.5,
    "year": 1996
}

response = requests.post(url, json=livro_ficcao)

if response.status_code == 200:
    print("Livro de ficção adicionado com sucesso")
else:
    print('Erro ao fazer a solicitação:', response.status_code)
