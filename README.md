# Manupulador de Transações

## Instruções

### Crie o ambiente virtual

#### - python -m venv venv

### Ative o venv

## linux

#### - source venv/bin/activate

#### Instale as dependências

#### - pip install -r requirements.txt

### Execute as migrações com os comandos

#### - ./manage.py makemigrations
#### - ./manage.py migrate

### A aplicação também possui testes, para executá-los digite o seguinte comando para ter o resultado no terminal
#### - ./manage.py test

### Já para executar o servidor e ativar os endpoints, utilize o comando:
#### - ./manage.py runserver



<h1 align="center">
  Organizador de Transações
</h1>

<blockquote align="center"></blockquote>

<h3 align= "center">
  Tecnologias&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</h3>

<p align="center" >
  As tecnologias utilizadas no projeto foram: Python | Django | Djanfo Rest Framework | SQLite3 | Testes unitários.
</p>

<br/>
<br/>

<h2 align="center">
  <a href ="#endpoints">API</a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</h2>

<p align="left">
  Após seguir gerar o ambiente de desenvolvimento e rodar o projeto, a API estárá disponível atráves da porta local tendo como endereço de base: <a href="http://localhost:8000/" target="_blank">http://localhost:8000/</a>
</p>

<p align="center">
  <a href="#endpoints">Endpoints</a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</p>

A API tem um total de 3 endpoints, sendo o inicial o para upload de movimentações. <br/>

<br />
<br />
<br />
<br />

## **Endpoints**

## Rota para upload de movimentações

```json
"url": "http://localhost:8000/api/movments/"
```

<h2 align ='center'> Realizando upload de arquivo </h2>

`POST /movements`

<h2 align ='center'> Requisição </h2>

No campo "HTML form", escolha um arquivo navegando pela opção "Escolher arquivo". Na pasta raiz do projeto há um arquivo de exemplo com o nome "Movimentacoes.txt".

<h2 align ='center'> Resposta de sucesso </h2>

`FORMATO DA RESPOSTA - STATUS 201`

```json
[
  {
    "file": null
  }
]
```

## Rota de movimentações

<h2 align ='center'> Listando Transações </h2>
Para listar as transações, o usuário receberá a seguinte resposta.

`GET /transactions - FORMATO DA RESPOSTA - STATUS 200`

```json

[
    {
        "total": "R$ 1.016,00"
    },
    [
        {
            "type_transaction": 3,
            "date": "2019-03-01",
            "hour": "15:34:53",
            "value": "-R$ 142,00",
            "cpf": "09620676017",
            "card": "4753****3153",
            "operation": "Saída",
            "store": 1
        },
        ...
    ]
```

<br />
<br />
<br />
<br />

## Rotas de Stores

<h2 align ='center'> Lista Stores </h2>

`GET /stores`

<h2 align ='center'> Requisição </h2>

`FORMATO DA RESPOSTA - STATUS 200`

```json
{
 "Stores": [
    {
      "id": 1,
      "store": " BAR DO JOÃO      ",
      "owner": "JOÃO MACEDO  ",
      "transactions": [
        {
        "type_transaction": 3,
        "date": "2019-03-01",
        "hour": "15:34:53",
        "value": "142,00",
        "cpf": "09620676017",
        "card": "4753****3153",
        "operation": "Saída",
        "store": 1
        },
        {
        "type_transaction": 2,
        "date": "2019-03-01",
        "hour": "23:42:34",
        "value": "112,00",
        "cpf": "09620676017",
        "card": "3648****0099",
        "operation": "Saída",
        "store": 1
        },
        },
            {
      "id": 2,
      "store": "LOJA DO Ó - MATRIZ",
      "owner": "MARIA JOSEFINA",
      "transactions": [
        {
        "type_transaction": 5,
        "date": "2019-03-01",
        "hour": "14:56:07",
        "value": "132,00",
        "cpf": "55641815063",
        "card": "3123****7687",
        "operation": "Entrada",
        "store": 2
        },
        {
        "type_transaction": 1,
        "date": "2019-03-01",
        "hour": "09:00:02",
        "value": "200,00",
        "cpf": "55641815063",
        "card": "1234****3324",
        "operation": "Entrada",
        "store": 2
        },
        {
        "type_transaction": 9,
        "date": "2019-03-01",
        "hour": "00:00:00",
        "value": "102,00",
        "cpf": "55641815063",
        "card": "6228****9090",
        "operation": "Saída",
        "store": 2
        }
      }
    ]
  }
]
```
