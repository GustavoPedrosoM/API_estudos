from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import time

DATABASE_URL = "mysql+pymysql://gustavo:teste@mysql-dev:3306/todolist_db"

MAX_RETRIES = 10
WAIT_SECONDS = 5

for attempt in range(MAX_RETRIES):
    try:
        engine = create_engine(
            DATABASE_URL,
            pool_pre_ping=True,
            echo=False,
        )
        conn = engine.connect()
        conn.close()
        print("Banco de dados conectado!")
        break
    except Exception as e:
        print(f"Tentativa {attempt+1} de conexão falhou: {e}")
        time.sleep(WAIT_SECONDS)
else:
    raise Exception("Não foi possível conectar ao banco de dados após várias tentativas.")

SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)
Base = declarative_base()
