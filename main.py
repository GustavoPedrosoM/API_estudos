from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from database import SessionLocal, engine
import models
import schemas
import redis
import json
import os

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

redis_host = os.getenv("REDIS_HOST", "localhost")
r = redis.Redis(host=redis_host, port=6379, db=0, decode_responses=True)

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
        t.pop('_sa_instance_state', None)  # remove metadado do SQLAlchemy
    r.set("tarefas", json.dumps(tarefas_dict), ex=30)  # cache por 30 segundos
    return tarefas_dict

@app.post("/tarefas", response_model=schemas.TarefaOut)
def criar_tarefa(tarefa: schemas.TarefaCreate, db: Session = Depends(get_db)):
    db_tarefa = models.Tarefa(**tarefa.dict())
    db.add(db_tarefa)
    db.commit()
    db.refresh(db_tarefa)
    r.delete("tarefas")  # invalida cache
    return db_tarefa

@app.delete("/tarefas/{id}")
def deletar_tarefa(id: int, db: Session = Depends(get_db)):
    tarefa = db.query(models.Tarefa).filter(models.Tarefa.id == id).first()
    if not tarefa:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")
    db.delete(tarefa)
    db.commit()
    r.delete("tarefas")  # invalida cache
    return {"mensagem": "Tarefa removida"}
