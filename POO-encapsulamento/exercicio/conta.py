#. 1 
class Conta:
    #. 2       #. 3
    def __init__(self, numero, titular, saldo, limite):
        #. 4
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
    
#. Criando getters e setters
    def get_saldo(self):
        return self.__saldo
    
    def get_titular(self):
        return self.__titular
    
    def get_limite(self):
        return self.__limite
    
    def set_limite(self, valor):
        self.__limite =  valor
        return self.__limite
    
#. Criando Propriedades
    @property
    def saldo(self):
        return self.__saldo
    
    @property
    def titular(self):
        return self.__titular
    
    @property
    def limite(self):
        return self.__limite
    
    @limite.setter
    def limite(self, valor):
        self.__limite =  valor
        return self.__limite

#. Criando Métodos privados
    def __pode_sacar(self, valor):
        verifica_saldo_disponivel = self.__saldo + self.__limite
        return valor <=  verifica_saldo_disponivel
    
    def saca(self, valor):
        if(self.__pode_sacar(valor)):
            self.__saldo -= valor
        else:
            print("O Valor passou do limite!")

#. Criando Métodos Estáticos
    @staticmethod
    def codigo_banco():
        return "001"

    @staticmethod
    def codigos_banco():
        return {"BB": "001", "Caixa": "104", "Bradesco": "237"}
    
