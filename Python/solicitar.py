import requests
import json

url = 'http://127.0.0.1:8000/livro_de_ficcao'
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    formatted_data = json.dumps(data, indent=4)
    print(formatted_data)
else:
    print('Erro ao fazer a solicitação:', response.status_code)
