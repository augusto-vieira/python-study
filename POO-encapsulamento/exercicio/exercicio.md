### Implementando o código
Para implementar o código visto nesta aula, siga os passos abaixo:

1. Crie a função **cria_conta**, que recebe como argumento **numero, titular, saldo e limite.**
2. Dentro dela, **crie o dicionário conta** com os argumentos da função e retorne-o no final da função.
3. Crie a função **deposita**, que recebe como argumento a **conta** e o **valor** e adiciona o valor ao saldo da conta.
4. Crie a função **saca**, que recebe como argumento a conta e o valor e subtrai o valor do saldo da conta.
5. Crie a função **extrato**, que recebe como argumento a conta e imprime o seu saldo.

### Criando conta
Chegou a hora de criar a sua primeira classe, a classe Conta. Para tal, crie o arquivo conta.py e siga os passos abaixo:

1. Defina a classe, utilizando a palavra-chave class, e em seguida defina o seu nome.
2. Defina a função construtora da classe, recebendo uma referência do próprio objeto como argumento.
3. Receba também como argumento os valores dos atributos da classe, isto é, **numero, titular, saldo e limite.**
4. Através da referência do objeto, defina os atributos numero, titular, saldo e limite com os respectivos valores recebidos como argumento.

### Criando getters e setters
Na aula anterior, foi visto que quando há dois underscores à frente de um atributo, não deve-se acessá-lo diretamente. Para ler um atributo, cria-se um getter para ele, e para modificar um atributo, cria-se um setter para ele.

Então, crie os **getters para os atributos saldo, titular e limite.** 

### Criando propriedades
Agora que vimos as propriedades, crie-os no lugar dos getters da classe Conta.

### Verificando o saque e métodos estáticos
Então, crie o **método pode_sacar**, que recebe o valor a ser sacado por argumento e verifica se há dinheiro suficiente na conta para o saque ser realizado, isto é, o valor do saque tem que ser menor ou igual ao saldo mais o limite da conta.

E no método **saca, faça um if para verificar se realmente o valor pode ser sacado da conta,** se sim, o saque é feito, se não, imprima uma mensagem externando que o valor passou o limite.

Por fim, como o **método pode_sacar** foi criado apenas para uma verificação interna, não faz sentido ele ser utilizado fora da classe, então **torne-o privado.**

### Métodos estáticos
Estamos criando contas de um único banco, o Banco do Brasil, que possui um código, o 001. Como esse código independe da conta, faz sentido acessá-lo sem termos um objeto da classe Conta.

Para isso, crie o **método estático codigo_banco,** que retorna o código do banco. E crie também o método estático **codigos_bancos**, que retorna um dicionário com os códigos dos bancos BB, Caixa e Bradesco, que são 001, 104 e 237, respectivamente.
