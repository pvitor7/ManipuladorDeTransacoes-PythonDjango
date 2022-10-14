
# Instruções:

### Crie o ambiente virtual pelo terminal utilizando o comando:

#####    - python -m venv venv

### Ative o venv com o comando(linux):

####   - source venv/bin/activate

### Instale as dependências:

####   - pip install -r requirements.txt

### Execute as migrações:

####   - ./manage.py migrate

### Rode o projeto:

####   - ./manage.py runserver

<h1 align="center">
  Organizador de Transações
</h1>

<blockquote align="center"></blockquote>

<h3 align= "center">
  Tecnologias&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</h3>

<p align="center" >
  As tecnologias utilizadas no projeto foram: Python | Django | Djanfo Rest Framework | SQLite3.
</p>

<br/>
<br/>

<h2 align="center">
  <a href ="#endpoints">API</a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</h2>

<p align="left">
  Após gerar o ambiente de desenvolvimento e rodar o projeto, a API estárá disponível atrávez da porta local tendo como endereço de base: <a href="http://localhost:8000/" target="_blank">http://localhost:8000/</a>
</p>

<p align="center">
  <a href="#endpoints">Endpoints</a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</p>

A API tem um total de 3 endpoints, sendo o inicial o para upload de movimentações. Eles podem ser executados direto no navegador. <br/>

<br />
<br />
<br />
<br />

## **Endpoints**

## Rota para upload de movimentações

```json
"https://http://localhost:8000/api/movments/"
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


<h2 align ='center'> Listando Transações </h2>
<br>
<br>

`GET /transactions`

<br>
<br>

FORMATO DA RESPOSTA - STATUS 200` </p>

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



<h2 align ='center'> Lista de estabelecimentos </h2>

`GET /stores`

<h2 align ='center'> Requisição </h2>


`FORMATO DA RESPOSTA - STATUS 200`

<br />
<br />

```json
[
    {
        "store": " BAR DO JOÃO      ",
        "owner": "JOÃO MACEDO  "
    },
    {
        "store": "LOJA DO Ó - MATRIZ",
        "owner": "MARIA JOSEFINA"
    },
    ...
]
```
