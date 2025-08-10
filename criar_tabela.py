# criar_tabela.py
from db import engine
from models import Base

# Cria todas as tabelas definidas nos modelos
Base.metadata.create_all(engine)

# Execute no terminal:
# python criar_tabela.py