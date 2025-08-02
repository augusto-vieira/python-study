class Cliente:
    def __init__(self, nome):
        self.__nome = nome

    # @property --> Define o método como uma propriedade
    # cliente.nome() -> cliente.nome 
    # Não é necessário usar o " () "
    # title -> função(do pyhton) que coloca a primeira letra do nome maiúscula
    @property
    def nome(self):
       ## print("chamando um método @property nome()")
        return self.__nome.title()
    
    # Criando um setter
    @nome.setter
    def nome(self, nome):
        print("chamando um método setter nome()")
        self.__nome = nome