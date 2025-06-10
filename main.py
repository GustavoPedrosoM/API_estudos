from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from database import SessionLocal, engine
import models
import schemas
import redis
import json
import os
import time

# Cria as tabelas no banco
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Configura Redis com variáveis de ambiente
redis_host = os.getenv("REDIS_HOST", "localhost")
redis_port = int(os.getenv("REDIS_PORT", 6379))

# Tentativa de conexão com Redis (retry)
def conectar_redis():
    for tentativa in range(10):
        try:
            r = redis.Redis(host=redis_host, port=redis_port, db=0, decode_responses=True)
            r.ping()
            print("✅ Redis conectado com sucesso.")
            return r
        except redis.exceptions.ConnectionError:
            print(f"⏳ Redis não disponível. Tentativa {tentativa + 1}/10...")
            time.sleep(2)
    raise Exception("❌ Não foi possível conectar ao Redis após várias tentativas.")

r = conectar_redis()

# Dependência de sessão do banco
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def read_root():
    return {"message": "API funcionando localmente!"}

@app.get("/tarefas", response_model=list[schemas.TarefaOut])
def listar_tarefas(db: Session = Depends(get_db)):
    cached = r.get("tarefas")
    if cached:
        return json.loads(cached)

    tarefas = db.query(models.Tarefa).all()
    tarefas_dict = [t.__dict__ for t in tarefas]
    for t in tarefas_dict:
        t.pop('_sa_instance_state', None)
    r.set("tarefas", json.dumps(tarefas_dict), ex=30)
    return tarefas_dict

@app.post("/tarefas", response_model=schemas.TarefaOut, status_code=201)
def criar_tarefa(tarefa: schemas.TarefaCreate, db: Session = Depends(get_db)):
    db_tarefa = models.Tarefa(**tarefa.model_dump())
    db.add(db_tarefa)
    db.commit()
    db.refresh(db_tarefa)
    r.delete("tarefas")
    return db_tarefa

@app.delete("/tarefas/{id}")
def deletar_tarefa(id: int, db: Session = Depends(get_db)):
    tarefa = db.query(models.Tarefa).filter(models.Tarefa.id == id).first()
    if not tarefa:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")
    db.delete(tarefa)
    db.commit()
    r.delete("tarefas")
    return {"mensagem": "Tarefa removida"}
