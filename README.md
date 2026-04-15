# API de Tarefas (Flask)

Este é um projeto simples de uma API de tarefas feita com Flask.  
Também inclui um script em Python que consome a API.

O objetivo foi praticar conceitos de backend e requisições HTTP.

---

## Funcionalidades

- Criar tarefas
- Listar tarefas
- Atualizar tarefas
- Deletar tarefas

---

## Tecnologias

- Python
- Flask
- Requests

---

## Como rodar

1. Instale as dependências:
pip install -r requirements.txt

2. Rode a API:
python api/app.py

3. Em outro terminal, rode o cliente:
python client/consumir_api.py

---

## Endpoints

- GET /tarefas
- POST /tarefas
- PUT /tarefas/{id}
- DELETE /tarefas/{id}

---

## Observação

Os dados são salvos em um arquivo JSON simples (`database.json`).

---

## Feito por

Victor Yuri
