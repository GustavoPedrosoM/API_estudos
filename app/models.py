from sqlalchemy import Column, Integer, String, Boolean
from app.database import Base

class Tarefa(Base):
    __tablename__ = "tarefas"

    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String(255), nullable=False)
    descricao = Column(String(255), nullable=False)
    concluida = Column(Boolean, default=False, nullable=False)
