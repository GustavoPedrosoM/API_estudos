# FastAPI Todo List API

![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

Este é um projeto de uma API RESTful simples para gerenciamento de tarefas (_to-do list_), criada com foco em aprendizado prático de tecnologias como **FastAPI**, **MySQL**, **Redis** e **Docker**. Ela permite realizar operações básicas de CRUD com persistência em banco de dados e cache com Redis, tudo orquestrado com Docker Compose.

---

## Funcionalidades

- Criar tarefas
- Listar tarefas
- Atualizar tarefas
- Excluir tarefas
- Persistência com MySQL
- Integração com Redis para cache

---

## Tecnologias Utilizadas

- [Python 3.12](https://www.python.org/)
- [FastAPI](https://fastapi.tiangolo.com/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [MySQL](https://www.mysql.com/)
- [Redis](https://redis.io/)
- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)

---

## Pré-requisitos

- Docker instalado
- Docker Compose instalado

---

## Estrutura do Projeto

.
|--- app/
│   |--- main.py
│   |--- models.py
│   |--- schemas.py
│   |--- database.py
|
|--- .dockerignore
│--- docker-compose.yml
|--- Dockerfile
|--- README.md
|--- requirements.txt

---

## Como Executar

1. **Clone o repositório:**
    dentro do terminal...
    git clone https://github.com/gustavopedrosom/fastapi-todolist-studies.git
    cd fastapi-todolist-studies

2. **Construa e suba os containers com Docker Compose:**
    docker compose up -d --build

3. **Acesse a documentação interativa da API:** 
    Swagger UI: http://localhost:8000/docs
    ReDoc: http://localhost:8000/redoc

---

## Exemplos de Uso (via curl)

1. **Criar tarefa (POST)**
    curl -X POST http://localhost:8000/tarefas \
    -H "Content-Type: application/json" \
    -d '{"titulo": "Aprender FastAPI", "descricao": "Estudar a documentação oficial", "concluida": false}'

2. **Listar tarefas (GET)**
    curl http://localhost:8000/tarefas

3. **Atualizar tarefa (PUT)** 
    curl -X PUT http://localhost:8000/tarefas/1 \
    -H "Content-Type: application/json" \
    -d '{"titulo": "Estudar Docker", "descricao": "Aprender volumes e redes", "concluida": true}'

4. **Deletar tarefa (DELETE)**
    curl -X DELETE http://localhost:8000/tarefas/1

--- 

## Autor 

Desenvolvido por Gustavo Pedroso de Paula Machado como parte de um estudo prático de desenvolvimento backend e infraestrutura.

## Licença

Este projeto está licenciado sob a Licença MIT. Veja o arquivo [LICENSE](./LICENSE) para mais detalhes.




