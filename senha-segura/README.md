```bash
secure-password/
├── src/
│   ├── api/                  # FastAPI app
│   │   └── main.py
│   │   
│   ├── ui/                   # Streamlit app
│   │   └── app.py
│   ├── core/                 # Regras de negócio (ex: validação de senha)
│   │   ├── regras.py
│   │   └── validador.py
│   └── utils/                # Funções auxiliares (ex: formatação, logs)
│       └── helpers.py
├── tests/
│   ├── test_validador.py
│   └── test_regras.py
├── .gitignore
├── pyproject.toml
├── README.md
```

**Criar ambiente e instalar dependências**
```bash
uv venv                                   # Cria o ambiente virtual
source .venv/bin/activate                 # Ativa o ambiente

uv uv pip install .                       # Instalando as dependência com .toml

uv pip install fastapi streamlit uvicorn  # Instala os pacotes manualmente
uv pip freeze > requirements.txt          # Gera o requirements


```
**Instalar o Projeto com .toml**
```bash
uv pip install .     # Instalação normal
uv pip install -e .  # Modo desenvolvimento (editable)
```
**Executar o FastAPI**
```bash
uvicorn src.api.main:app --reload
```

**Executar o Streamlit**
```bash
streamlit run src/ui/app.py
```
