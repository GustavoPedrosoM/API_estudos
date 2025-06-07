from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Use os dados do seu docker-compose
DATABASE_URL = "mysql+pymysql://gustavo:1234@mysql-dev:3306/todolist"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)
Base = declarative_base()
