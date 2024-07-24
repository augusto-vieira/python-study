#. Craindo uma Classe 
class Conta:
    # __init__ --> Constructor
    # self --> referência ao próprio objeto, equivalente ao "this" em Java 
   
    def __init__(self, numero, titular, saldo, limite):
        # __ --> torna o método privado, equivalente "private" no Java
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
         
    def extrato(self):
        # ":.2f" quantidade de casa no print
        print(f"Saldo de {self.__saldo:.2f} do titular {self.__titular}")
    
    def deposita(self, valor):
        self.__saldo += valor
    
    # Método privado
    def __pode_sacar(self, valor_a_sacar):
        valor_disponivel_a_sacar = self.__saldo + self.limite
        return valor_a_sacar <= valor_disponivel_a_sacar

    def saca(self, valor):  
        if(self.__pode_sacar(valor)):
            self.__saldo -= valor
        else:
            print("O valor passou do limite!")
    
    def trasferir(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)
    
    # Métodos getters e setters
    def get_saldo(self):
        return self.__saldo
    
    def set_limite(self, limite):
        self.__limite = limite
    
    def get_limite(self):
        return self.__limite   
    
    # Usando property e setter 
    @property
    def saldo(self):
        return self.__saldo

    @property
    def limite(self):
        return self.__limite
    
    @limite.setter
    def limite(self, valor):
        self.__limite =  valor
        return self.__limite
    
    # Usando Métodos da Classe, vc pode acessar sem criar um objeto!
    # São chamados de métodos estáticos (staticmetodo), eles pertencem a classe
    @staticmethod
    def codigos_bancos():
        return {"BB": "001", "Caixa": "104", "Bradesco": "237"}