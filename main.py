from fastapi import FastAPI, HTTPException
from models import Tarefa

app = FastAPI()

tarefas = []
@app.get("/")
def read_root():
    return {"message": "API para estudos cloud rodando com sucesso!"}

@app.get("/tarefas")
def listar_tarefas():
    return tarefas

@app.post("/tarefas")
def criar_tarefa(tarefa: Tarefa):
    tarefas.append(tarefa)
    return {"mensagem": "Tarefa criada com sucesso"}

@app.delete("/tarefas/{id}")
def deletar_tarefa(id: int):
    for tarefa in tarefas:
        if tarefa.id == id:
            tarefas.remove(tarefa)
            return {"mensagem": "Tarefa removida"}
    raise HTTPException(status_code=404, detail="Tarefa não encontrada")
