'''
.
Exemplo de um código procedural!
.
'''
print(".\n---------------------------------------")
print("Código procedural!")
#. teste = nome do módulo
#. import = importar
#. importando a função para usar no meu programa main.py
from teste import cria_conta, extrato

# Crinado uma conta utilizando a nossa função
conta = cria_conta(123, "Vitoria", 100.00, 50.00)
print(conta["numero"])

# Print do saldo da conta
extrato(conta)
print("---------------------------------------\n.")
#. 

'''
.
Exemplo de um código Orientado a Obejto!
.
'''
print("+++++++++++++++++++++++++++++++++++++++")
print("Orientado a Objeto!")

#. Importo a Class para meu projeto
#.
from conta import Conta
obj_conta = Conta(321, "Augusto", 100.00, 25.00)

#. Usando a função do objeto
obj_conta.extrato()
obj_conta.deposita(1000.50)
obj_conta.saca(10000)
obj_conta.extrato()

obj2 = Conta(321, "Vitoria", 100.00, 100)

obj_conta.trasferir(75,obj2)
obj2.extrato()

# . Usando métodos getters e setters
print(obj2.get_saldo())
obj2.set_limite(5)
print(obj2.get_limite())

print("\n+++++++++++++++++++++++++++++++++++++++")
# . Usando os modificadores do python
from cliente import Cliente
obj_cliente = Cliente("alba")

# Parece que estamos acessando um atributo, mas na vdd é um método
#  " @property "
print("chamando um método @property nome()")
print(obj_cliente.nome)

# Criando um setter
# " @nome.setter "
obj_cliente.nome = "joão"
print(obj_cliente.nome)

# Métodos estáticos
print("\nChamando um método estático")
print(Conta.codigos_bancos())

