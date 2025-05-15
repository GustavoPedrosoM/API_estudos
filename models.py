from pydantic import BaseModel

class Tarefa(BaseModel):
    id: int
    titulo: str
    concluida: bool = False
