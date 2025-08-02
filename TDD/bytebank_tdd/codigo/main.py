from bytebank import Funcionario

def teste_idade():
    funcionario_teste = Funcionario('Teste', '13/03/2000', 1111)
    print(f'Teste = {funcionario_teste.idade()}')

    funcionario_teste1 = Funcionario('Teste', '13/12/1999', 1111)
    print(f'Teste = {funcionario_teste1.idade()}')

teste_idade()

