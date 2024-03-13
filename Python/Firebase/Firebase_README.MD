## Adicionando Livros ao Firebase com Python

Neste exemplo, demonstramos como adicionar livros a um banco de dados do Firebase usando Python. 

### Pré-requisitos

Antes de começar, é necessário ter uma conta no Firebase e criar um novo projeto. Além disso, é preciso ter o SDK do Firebase instalado e configurado em seu ambiente Python. Certifique-se de ter suas credenciais de serviço JSON do Firebase prontas para uso.

### Configuração do Ambiente

1. Instale o pacote `firebase_admin` usando o gerenciador de pacotes `pip`:

    ```bash
    pip install firebase-admin
    ```

2. Crie um novo arquivo chamado `firebase_config.py` onde você armazenará o caminho para suas credenciais de serviço JSON. Adicione o caminho ao seu arquivo `.gitignore` para proteger suas credenciais.

3. No arquivo `firebase_config.py`, adicione o seguinte conteúdo:

    ```python
    caminho_secret = "caminho_para_suas_credenciais.json"
    ```

### Código Python

Veja abaixo como adicionar livros ao Firebase usando Python:

```python
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_config import caminho_secret

# Inicialize o aplicativo Firebase com suas credenciais
cred = credentials.Certificate(caminho_secret)
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://seu-projeto.firebaseio.com/'
})

# Referência ao banco de dados
ref = db.reference('/')

# Lista de livros a serem adicionados ao banco de dados
livros = [
    # Lista de dicionários contendo informações de cada livro
]

# Adicionando os livros ao banco de dados
for livro in livros:
    ref.child('livros').push(livro)

print("Livros adicionados com sucesso!")
