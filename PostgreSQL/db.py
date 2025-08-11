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