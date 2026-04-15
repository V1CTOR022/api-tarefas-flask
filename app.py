from flask import Flask, request, jsonify
import json
import os

app = Flask(__name__)

DB_FILE = "database.json"


def carregar_dados():
    if not os.path.exists(DB_FILE):
        return []
    with open(DB_FILE, "r") as f:
        return json.load(f)


def salvar_dados(dados):
    with open(DB_FILE, "w") as f:
        json.dump(dados, f, indent=4)


@app.route("/tarefas", methods=["GET"])
def listar_tarefas():
    tarefas = carregar_dados()
    return jsonify(tarefas)


@app.route("/tarefas", methods=["POST"])
def criar_tarefa():
    dados = carregar_dados()
    nova = request.json

    nova["id"] = len(dados) + 1
    nova["concluida"] = False

    dados.append(nova)
    salvar_dados(dados)

    return jsonify(nova), 201

@app.route("/tarefas/<int:id>", methods=["PUT"])
def atualizar_tarefa(id):
    dados = carregar_dados()

    for tarefa in dados:
        if tarefa["id"] == id:
            tarefa.update(request.json)
            salvar_dados(dados)
            return jsonify(tarefa)

    return jsonify({"erro": "Tarefa não encontrada"}), 404


@app.route("/tarefas/<int:id>", methods=["DELETE"])
def deletar_tarefa(id):
    dados = carregar_dados()
    novos = [t for t in dados if t["id"] != id]

    salvar_dados(novos)
    return jsonify({"mensagem": "Tarefa removida"})

if __name__ == "__main__":
    app.run(debug=True)