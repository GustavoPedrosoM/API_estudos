from pydantic import BaseModel
from typing import Optional

class TarefaCreate(BaseModel):
    titulo: str
    descricao: str
    concluida: bool = False

class TarefaOut(TarefaCreate):
    id: int
