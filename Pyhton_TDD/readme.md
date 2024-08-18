## Conteúdo Estudado
### Python e TDD: Explorando Testes Unitários
* Tipos de testes: `Teste Unitário`, `Teste de Integração`, `Teste de ponta a ponta (E2E)`.
* -
* -
----
> **Teste Unitário**: Focado em testar partes isoladas do código, como  Método/Funções ou Classes, para garantir que cada unidade funcione corretamente.

> **Teste de Integração**: Verifica a interação entre diferentes módulos ou componentes do sistema para garantir que funcionem bem juntos. Ele expõe problemas que podem surgir quando partes do sistema se combinam.

> **Teste de ponta a ponta (E2E)**: Testa a aplicação inteira, desde o início até o final, muitas vezes simula o usuário ou simulando ambiente de produção.

![Teste Unitários](https://files.speakerdeck.com/presentations/b72cae2d552e41078464804a856c284f/slide_4.jpg)

  ### Exemplo de uma calculadora:
Os `testes unitários` podem ser aplicados para verificar operações básicas, como garantir que a função **soma(a, b)** retorne o resultado correto ao somar dois números. Em seguida, os `testes de integração` podem ser usados para verificar a interação entre diferentes operações, como **somar** e **multiplicar números**, garantindo que a função **calculaExpressao("2 + 3 * 4")** produza o resultado correto ao combinar múltiplas operações aritméticas. Por fim, um `Teste de ponta a ponta (E2E)` poderia simular o uso da calculadora do início ao fim, como um _usuário inserindo uma expressão_ complexa no display, verificando se o sistema calcula e exibe o resultado esperado, englobando toda a lógica interna da aplicação.