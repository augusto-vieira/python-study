#. 1
def cria_conta(numero, titular, saldo, limite):
    conta = {"numero": numero, "titular": titular, "saldo": saldo, "limite": limite}
    return conta

#. 2
def deposita(conta, valor):
    conta["valor"] += valor

#. 3
def  saca(conta, valor):
    conta["valor"] -= valor

#. 4
def extrato(conta):
    print(f"Seu saldo é {conta["saldo"]}")
