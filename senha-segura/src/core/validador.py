from src.core import regras

def is_secure_password(senha: str) -> bool:
    return all([
        regras.tamanho_minimo(senha),
        regras.tem_maiuscula(senha),
        regras.tem_minuscula(senha),
        regras.tem_numero(senha),
        regras.tem_caractere_especial(senha),
    ])

# 1vYQIYxO&p$yfI^r