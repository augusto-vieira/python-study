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

**Criar o ambiente virtual**
```bash
uv venv                                   
source .venv/bin/activate                
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