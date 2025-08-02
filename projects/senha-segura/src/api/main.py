# src/api/main.py (FastAPI)
from fastapi import FastAPI
from src.core.validador import is_secure_password

app = FastAPI()

@app.get("/check-password")
def check_password(password: str):
    return {"secure": is_secure_password(password)}
