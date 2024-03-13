import requests
import json

url = 'http://localhost:8080/livros'
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    formatted_data = json.dumps(data, indent=4)  # Indenta o JSON para uma melhor legibilidade
    print(formatted_data)
else:
    print('Erro ao fazer a solicitação:', response.status_code)
