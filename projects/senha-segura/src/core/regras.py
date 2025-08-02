import re

def tem_maiuscula(senha: str) -> bool:
    return bool(re.search(r"[A-Z]", senha))

def tem_minuscula(senha: str) -> bool:
    return bool(re.search(r"[a-z]", senha))

def tem_numero(senha: str) -> bool:
    return bool(re.search(r"\d", senha))

def tem_caractere_especial(senha: str) -> bool:
    return bool(re.search(r"[!@#$%^&*(),.?\":{}|<>]", senha))

def tamanho_minimo(senha: str, minimo: int = 8) -> bool:
    return len(senha) >= minimo
