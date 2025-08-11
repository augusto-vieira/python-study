# Usando Python com PostgreSQL para Gerenciar POIs (Point of Interest)

Neste artigo, vamos criar um exemplo completo de como usar **Python** com **PostgreSQL** para gerenciar **POIs** (*Points of Interest*), armazenando **nome** (string) e **coordenadas** `x`, `y` (inteiros positivos).

Utilizaremos **SQLAlchemy** como camada de abstração (ORM), que facilita o mapeamento de tabelas e manipulação de dados, mantendo o código mais legível e seguro.

---

## 1. Configurando o ambiente
### Criação do ambiente virtual
```bash
uv venv
source .venv/bin/activate
``` 

### Instalação das dependências

```bash
uv pip install sqlalchemy dotenv psycopg
```

- **SQLAlchemy** → ORM para manipulação de dados.
- **psycopg** → driver para conectar ao PostgreSQL.

### Estrutura do projeto

```
poi_project/
├── db.py              # Configuração do banco
├── criar_tabela.py    # Criar tabela no banco
├── models.py          # Definição da tabela POI
├── main.py            # Operações CRUD
├── docker-compose.yml # Criar contêiner do PostgreSQL
├── .env               # Configuração das variáveis de ambientes 
└── requirements.txt
```

---
## 2. Configuração da conexão (`db.py`)

```python
# db.py
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Pegamos a URL do banco de dados via variável de ambiente (boa prática)
# Formato: postgresql+psycopg://usuario:senha@host:porta/banco
# Carrega as variáveis do ambiente pelo arquivo .env
load_dotenv(override=True)  # força sobrescrever variáveis existentes

# Agora lê do .env
DB_URL = os.getenv('DATABASE_URL') 

# Cria a Engine de conexão com pool (melhora performance)
engine = create_engine(DB_URL, echo=True)  # echo=True mostra as queries no console

# Fábrica de sessões para transações
SessionLocal = sessionmaker(bind=engine)
```

**Explicação:**

- Usamos **variáveis de ambiente** para evitar deixar senhas expostas no código.
- `engine` gerencia a conexão com o banco.
- `SessionLocal` cria instâncias de sessão para interagir com o banco.

---

## 3. Definindo a tabela POI (`models.py`)

```python
# models.py
from sqlalchemy import Column, Integer, String, CheckConstraint
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class POI(Base):
    __tablename__ = 'pois'  # Nome da tabela no banco

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    x = Column(Integer, nullable=False)
    y = Column(Integer, nullable=False)

    # Restrições para garantir apenas valores positivos
    __table_args__ = (
        CheckConstraint('x >= 0', name='check_x_positive'),
        CheckConstraint('y >= 0', name='check_y_positive'),
    )

    def __repr__(self):
        return f"<POI(id={self.id}, name='{self.name}', x={self.x}, y={self.y})>"
```

**Explicação:**

- `CheckConstraint` garante que `x` e `y` sejam **positivos**.
- O método `__repr__` facilita o debug, mostrando os dados de forma amigável.

---

## 4. Criando o banco e a tabela

```python
# criar_tabela.py
from db import engine
from models import Base

# Cria todas as tabelas definidas nos modelos
Base.metadata.create_all(engine)
```

Execute:

```bash
python criar_tabela.py
```

Isso criará a tabela `pois` no banco PostgreSQL.

---

## 5. Operações CRUD (`main.py`)
**C**reate **R**ead **U**pdate **D**elete

```python
# main.py
from db import SessionLocal
from models import POI

# Função para adicionar um POI
def add_poi(name: str, x: int, y: int):
    session = SessionLocal()
    try:
        poi = POI(name=name, x=x, y=y)
        session.add(poi)
        session.commit()
        print(f"POI '{name}' adicionado com sucesso!")
    except Exception as e:
        session.rollback()
        print("Erro ao adicionar POI:", e)
    finally:
        session.close()

# Função para listar todos os POIs
def list_pois():
    session = SessionLocal()
    try:
        pois = session.query(POI).all()
        for poi in pois:
            print(poi)
    finally:
        session.close()

# Função para buscar POI por nome
def find_poi(name: str):
    session = SessionLocal()
    try:
        pois = session.query(POI).filter(POI.name.ilike(f"%{name}%")).all()
        return pois
    finally:
        session.close()

# Função para atualizar POI
def update_poi(poi_id: int, new_name: str, new_x: int, new_y: int):
    session = SessionLocal()
    try:
        poi = session.query(POI).get(poi_id)
        if poi:
            poi.name = new_name
            poi.x = new_x
            poi.y = new_y
            session.commit()
            print("POI atualizado com sucesso!")
        else:
            print("POI não encontrado!")
    finally:
        session.close()

# Função para deletar POI
def delete_poi(poi_id: int):
    session = SessionLocal()
    try:
        poi = session.query(POI).get(poi_id)
        if poi:
            session.delete(poi)
            session.commit()
            print("POI removido com sucesso!")
        else:
            print("POI não encontrado!")
    finally:
        session.close()

if __name__ == "__main__":
    # Adicionando alguns POIs
    add_poi("Praça Central", 20, 35)
    add_poi("Museu da Cidade", 45, 60)

    print("\nLista de POIs:")
    list_pois()

    print("\nBuscando por 'Museu':")
    for p in find_poi("Museu"):
        print(p)

    print("\nAtualizando POI id=1:")
    update_poi(1, "Praça Nova Central", 25, 40)
    list_pois()

    print("\nRemovendo POI id=2:")
    delete_poi(2)
    list_pois()

    ## Novos POIs
    add_poi("Lanchonete", 27, 12)
    add_poi("Posto", 31, 18)
    add_poi("Joalheria", 15, 12),
    add_poi("Floricultura", 19, 21)
    add_poi("Pub", 12, 8)
    add_poi("Supermercado", 23, 6)
    add_poi("Churrascaria", 28, 2)
    list_pois()
```

**Explicação:**

- Todas as operações usam **sessões** (`SessionLocal`) para interagir com o banco.
- **Rollback** é usado em caso de erro.
- `.ilike()` permite busca **case-insensitive**.
- `.get()` busca por chave primária.

---

## 6. Boas práticas adotadas

- **Variáveis de ambiente** para credenciais.
- **CheckConstraint** para validar dados no banco.
- **Sessões curtas**: abertas apenas durante a operação.
- **Rollback** em caso de erro.
- **Funções separadas** para cada operação CRUD.
- **Echo SQL** no modo debug (`echo=True` na `engine`).

---

## 7. Próximos passos

- Criar **testes automatizados** 
- Implementar **migrations** com Alembic.
- Criar API REST com **FastAPI** para expor os POIs.

---


**Help**
```bash
docker exec -it poi_postgres bash
```
**Acessar o Banco diretamente**
```bash
psql -h localhost -U poiuser -d poidb  # senha poipass
```
**Comando interno do Banco**
```bash
\l                # Listar bancos de dados
\dt               # Listar tabelas do banco atual
\c                # dbname Conectar a outro banco
\q                # Sair do psql

\d nome_tabela    # Listar colunas de uma tabela
```
**Run Fast**
```bash
uv venv
source .venv/bin/activate
uv pip install sqlalchemy dotenv psycopg

docker-compose up -d

python criar_tabela.py
python main.py
```