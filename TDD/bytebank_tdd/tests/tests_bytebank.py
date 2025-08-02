# import os, sys  # Assim funciona # OK!
# sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))  # OK!
#sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))


from codigo.bytebank import Funcionario  

print('aqui') 

# Given - When -Then
# Dado (contexto)
# Quando (Ação)
# Então (Desfecho) 

'''
# Criar um Classe para cada trecho de código que eu quero testar, deixa mais organizado.
class TestClass:
    def test_quando_idade_recebe_13_03_200_deve_retornar_22(self):       
        entrada = '13/03/2000'  # Given-Contexto
        esperado = 22

        funcionario_teste = Funcionario('Teste', entrada, 1111)
        
        resultado = funcionario_teste.idade() # When-ação

        assert resultado == esperado # Then-desfecho

''' 

