from fastapi import FastAPI, HTTPException
from models import Tarefa
import redis
import json
import os

app = FastAPI()

# Substitua pelo endpoint do seu Redis
redis_host = "master.estudos-redis.pd7420.use1.cache.amazonaws.com"
redis_port = 6379  # Porta padrão
r = redis.StrictRedis(host=redis_host, port=redis_port, decode_responses=True)

@app.get("/")
def read_root():
    return {"message": "API com Redis funcionando!"}

@app.get("/tarefas")
def listar_tarefas():
    tarefas = r.lrange("tarefas", 0, -1)
    return [json.loads(tarefa) for tarefa in tarefas]

@app.post("/tarefas")
def criar_tarefa(tarefa: Tarefa):
    r.rpush("tarefas", json.dumps(tarefa.dict()))
    return {"mensagem": "Tarefa criada com sucesso"}

@app.delete("/tarefas/{id}")
def deletar_tarefa(id: int):
    tarefas = r.lrange("tarefas", 0, -1)
    for tarefa in tarefas:
        tarefa_json = json.loads(tarefa)
        if tarefa_json["id"] == id:
            r.lrem("tarefas", 1, tarefa)
            return {"mensagem": "Tarefa removida"}
    raise HTTPException(status_code=404, detail="Tarefa não encontrada")
