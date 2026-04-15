import requests

BASE_URL = "http://127.0.0.1:5000/tarefas"


def criar():
    tarefa = {
        "titulo": "Estudar API Flask",
        "descricao": "Treinar backend para estágio"
    }

    r = requests.post(BASE_URL, json=tarefa)
    print("Criado:", r.json())


def listar():
    r = requests.get(BASE_URL)
    print("Lista:", r.json())


def atualizar():
    dados = {"concluida": True}
    r = requests.put(f"{BASE_URL}/1", json=dados)
    print("Atualizado:", r.json())


def deletar():
    r = requests.delete(f"{BASE_URL}/1")
    print(r.json())

if __name__ == "__main__":
    criar()
    listar()
    atualizar()
    listar()
    deletar()