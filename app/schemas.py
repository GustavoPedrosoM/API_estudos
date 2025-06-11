from pydantic import BaseModel

class TarefaCreate(BaseModel):
    titulo: str
    descricao: str
    concluida: bool = False

class TarefaOut(TarefaCreate):
    id: int

    class Config:
        orm_mode = True
