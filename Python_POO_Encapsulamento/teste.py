def cria_conta(numero, titular, saldo, limite):
    conta = {"numero": numero, "titular": titular, "saldo": saldo, "limite": limite}
    return conta

def extrato(conta):
    print(f"Saldo é {conta["saldo"]}")