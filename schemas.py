from pydantic import BaseModel

class TarefaCreate(BaseModel):
    id: int
    titulo: str
    descricao: str
    concluida: bool = False

class TarefaOut(TarefaCreate):
    pass
