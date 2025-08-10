# Python + Bancos de Dados — Guia objetivo

> Arquivo objetivo com exemplos práticos, código comentado e boas práticas.

---

# Sumário

1. [Formas de usar Python com Banco de Dados](#formas)

- 1.1 [Exemplos simples](#formas-exemplos)
- 1.2 [Operações e funcionalidades principais](#formas-operacoes)
- 1.3 [Detalhes, código comentado e práticas de projeto](#formas-praticas)

2. [Python com PostgreSQL](#postgres)

- 2.1 [Exemplos simples](#pg-exemplos)
- 2.2 [Operações e funcionalidades principais](#pg-operacoes)
- 2.3 [Detalhes, código comentado e práticas de projeto](#pg-praticas)

---

# 1. Formas de usar Python com Banco de Dados {#formas}

## 1.1 Resumo rápido das opções

- **Drivers DB-API**: `sqlite3` (embutido), `psycopg2`/`psycopg[binary]` (Postgres), `pymysql`/`mysql-connector-python` (MySQL), `pyodbc` (ODBC).
- **ORMs**: `SQLAlchemy` (Core + ORM) — padrão do mercado; `Django ORM`; `Peewee` (leve); `Tortoise ORM` (async).
- **Drivers async**: `asyncpg` (Postgres), `aiomysql` (MySQL), `databases` (API async que funciona com SQLAlchemy core).
- **NoSQL**: `pymongo` (MongoDB), `redis-py` (Redis).
- **Ferramentas**: `Alembic` (migrations para SQLAlchemy), `alembic`/`django migrations`, `psycopg2.pool` (pool), `sqlalchemy.pool`.

**Quando usar o quê (objetivo):**

- Prototipagem/pequenos scripts → `sqlite3`.
- Aplicações profissionais relacionais → `SQLAlchemy` + driver (psycopg2 para Postgres).
- Alta concorrência async → `asyncpg` ou `databases` + SQLAlchemy Core.
- Document store → `pymongo`.

---

## 1.1 Exemplos simples de usar {#formas-exemplos}

### 1) `sqlite3` (embutido) — exemplo mínimo

```python
import sqlite3
from contextlib import closing

# Arquivo DB: app.db (persistente) — ideal para testes e protótipos
with sqlite3.connect('app.db') as conn:
    conn.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT)')
    # parâmetro trocado por ? => evita SQL injection
    conn.execute('INSERT INTO users (name) VALUES (?)', ("Alice",))
    conn.commit()

with sqlite3.connect('app.db') as conn:
    cur = conn.execute('SELECT id, name FROM users')
    for row in cur.fetchall():
        print(row)
```

### 2) SQLAlchemy Core — conexão e query direta

```python
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, select

engine = create_engine('sqlite:///app.db', echo=False)
metadata = MetaData()
users = Table('users', metadata,
              Column('id', Integer, primary_key=True),
              Column('name', String))
metadata.create_all(engine)

# Inserir e selecionar com Engine (Core)
with engine.connect() as conn:
    conn.execute(users.insert().values(name='Bob'))
    result = conn.execute(select(users))
    for row in result:
        print(row)
```

### 3) Exemplo NoSQL (MongoDB com pymongo)

```python
from pymongo import MongoClient
client = MongoClient('mongodb://localhost:27017')
db = client['appdb']
users = db.users
users.insert_one({'name': 'Carol'})
for u in users.find():
    print(u)
```

---

## 1.2 Exemplos usando as principais operações e funcionalidades {#formas-operacoes}

Vamos abordar **CRUD**, transações, bulk inserts e uso de pools.

### CRUD com SQLAlchemy ORM — exemplo direto e prático

```python
# models.py
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

# main.py (uso)
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, User

engine = create_engine('sqlite:///app.db')
Session = sessionmaker(bind=engine)
Base.metadata.create_all(engine)

# Create
session = Session()
new = User(name='Dani')
session.add(new)
session.commit()

# Read
user = session.query(User).filter_by(name='Dani').first()
print(user.id, user.name)

# Update
user.name = 'Daniela'
session.commit()

# Delete
session.delete(user)
session.commit()

session.close()
```

**Notas rápidas:** use `sessionmaker()` e feche a sessão; em apps web, use um escopo por request (ou `scoped_session`).

### Transações e rollbacks (exemplo com context manager)

```python
from sqlalchemy.orm import Session

with Session(engine) as session:
    try:
        user = User(name='TransTest')
        session.add(user)
        # mais operações...
        session.commit()  # ou commit no final
    except Exception:
        session.rollback()
        raise
```

### Bulk insert — execute\_values (psycopg2) ou bulk\_insert\_mappings (SQLAlchemy)

```python
# psycopg2 + execute_values (mais performático para muitos registros)
from psycopg2.extras import execute_values
import psycopg2

conn = psycopg2.connect("dbname=test user=appuser password=secret")
with conn, conn.cursor() as cur:
    rows = [(1, 'A'), (2, 'B')]
    execute_values(cur, "INSERT INTO t (id, name) VALUES %s", rows)
```

---

## 1.3 Detalhes e práticas de projeto (código comentado) {#formas-praticas}

### Estrutura mínima de projeto (exemplo)

```
project/
├─ app/
│  ├─ __init__.py
│  ├─ config.py        # carrega variáveis de ambiente
│  ├─ db.py            # engine, Session, utilitários
│  ├─ models.py
│  └─ repository.py    # funções de acesso a dados (camada única)
├─ migrations/         # alembic ou django migrations
├─ tests/
└─ requirements.txt
```

### Boas práticas objetivas

- **Configuração**: use variáveis de ambiente (`os.environ`) para credenciais e URL do DB; não comitar senhas.
- **Pooling**: em produção, ative pool (`SQLAlchemy` engine já tem pool); não abrir/fechar conexão a cada query.
- **Injeção de dependência**: passe `Session`/`engine` para funções em vez de variáveis globais quando possível.
- **Migrations**: use `Alembic` ou sistema de migrations do framework; nunca aplicar schema manualmente em produção.
- **Segurança**: sempre **queries parametrizadas** — nunca faça f"...{user\_input}..." para montar SQL.
- **Transações**: agrupe operações relacionadas em transações; trate rollback em exceções.
- **Testes**: use DB de teste (SQLite in-memory ou containers) e fixtures que criem/dropem schema.
- **Logs**: habilite logging SQL apenas em debug e filtre dados sensíveis.

---

# 2. Como usar Python com PostgreSQL {#postgres}

## 2.1 Exemplos simples de usar {#pg-exemplos}

### 1) Usando `psycopg2` (síncrono) — exemplo mínimo

```python
import os
import psycopg2
from psycopg2.extras import RealDictCursor

DSN = os.getenv('DATABASE_URL', 'postgresql://app:pass@localhost:5432/appdb')

# 'with' garante commit/rollback automático ao final do bloco
with psycopg2.connect(DSN, cursor_factory=RealDictCursor) as conn:
    with conn.cursor() as cur:
        cur.execute('CREATE TABLE IF NOT EXISTS users (id SERIAL PRIMARY KEY, name TEXT NOT NULL)')
        cur.execute('INSERT INTO users (name) VALUES (%s) RETURNING id', ('Eve',))
        new_id = cur.fetchone()['id']
        print('Inserido id =', new_id)

# seleção
with psycopg2.connect(DSN, cursor_factory=RealDictCursor) as conn:
    with conn.cursor() as cur:
        cur.execute('SELECT id, name FROM users')
        rows = cur.fetchall()
        for r in rows:
            print(r)
```

**Observação**: `psycopg2` usa `%s` como placeholder; **não** usar `?`.

### 2) Usando `SQLAlchemy` com PostgreSQL (ORM) — string de conexão

```python
from sqlalchemy import create_engine

# formato: postgresql+psycopg2://user:password@host:port/dbname
engine = create_engine('postgresql+psycopg2://app:pass@localhost:5432/appdb')
```

Use o mesmo código ORM do capítulo 1 substituindo a engine.

---

## 2.2 Exemplos das principais operações e funcionalidades {#pg-operacoes}

### Pooling com `psycopg2.pool` — exemplo simples

```python
from psycopg2 import pool

pool = pool.SimpleConnectionPool(minconn=1, maxconn=10, dsn=DSN)

conn = pool.getconn()
try:
    with conn.cursor() as cur:
        cur.execute('SELECT 1')
        print(cur.fetchone())
finally:
    pool.putconn(conn)

pool.closeall()
```

### Bulk insert rápido com `psycopg2.extras.execute_values`

```python
from psycopg2.extras import execute_values

rows = [(f'name{i}', ) for i in range(10000)]
with psycopg2.connect(DSN) as conn:
    with conn.cursor() as cur:
        execute_values(cur, "INSERT INTO users (name) VALUES %s", rows)
```

### COPY (CSV) — carregar dados grandes (alto desempenho)

```python
# CSV -> tabela
with open('data.csv', 'r') as f:
    with psycopg2.connect(DSN) as conn:
        with conn.cursor() as cur:
            # a tabela já deve existir e colunas combinarem com CSV
            cur.copy_expert("COPY users(name) FROM STDIN WITH (FORMAT csv)", f)
```

### Transações avançadas — Savepoints

```python
with psycopg2.connect(DSN) as conn:
    with conn.cursor() as cur:
        cur.execute("BEGIN")
        cur.execute("INSERT INTO users (name) VALUES (%s)", ('A',))
        cur.execute("SAVEPOINT sp1")
        try:
            cur.execute("INSERT INTO users (name) VALUES (%s)", (None,))  # pode falhar
        except Exception:
            cur.execute("ROLLBACK TO SAVEPOINT sp1")
        cur.execute("COMMIT")
```

### Async com `asyncpg` — exemplo mínimo

```python
import asyncio
import asyncpg

async def main():
    conn = await asyncpg.connect(dsn='postgresql://app:pass@localhost:5432/appdb')
    await conn.execute('CREATE TABLE IF NOT EXISTS t (id serial primary key, name text)')
    await conn.execute('INSERT INTO t(name) VALUES($1)', 'AsyncUser')
    rows = await conn.fetch('SELECT id, name FROM t')
    print(rows)
    await conn.close()

asyncio.run(main())
```

**Observação**: `asyncpg` usa placeholders no formato `$1, $2...`.

---

## 2.3 Detalhes e práticas de projeto para PostgreSQL (código comentado) {#pg-praticas}

### Conexão segura e configuração (exemplo `db.py`)

```python
# db.py
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DB_URL = os.getenv('DATABASE_URL')  # defina via ENV (ex: postgres://...)
if not DB_URL:
    raise RuntimeError('DATABASE_URL não configurado')

# pool_size/max_overflow ajustados para a produção
engine = create_engine(DB_URL, pool_size=10, max_overflow=20)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# utilitário para usar em aplicações web
from contextlib import contextmanager

@contextmanager
def get_session():
    session = SessionLocal()
    try:
        yield session
        session.commit()
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()
```

### Migrations com Alembic (prática)

- Inicialize `alembic init alembic`
- Configure \`alembic
