import requests

response = requests.get('http://localhost:5000/')

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print('Erro ao fazer a solicitação:', response.status_code)
