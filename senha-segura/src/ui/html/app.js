// Seleciona os elementos do DOM necessários para validação e exibição
const passwordInput = document.getElementById('password');
const messageContainer = document.getElementById('message');

const lengthItem = document.getElementById('length');
const uppercaseItem = document.getElementById('uppercase');
const lowercaseItem = document.getElementById('lowercase');
const numberItem = document.getElementById('number');
const specialItem = document.getElementById('special');

// Adiciona evento para validar a senha a cada caractere digitado
passwordInput.addEventListener('input', function() {
    const password = passwordInput.value;
    validatePassword(password);
});

/**
 * Valida a senha conforme os requisitos definidos
 * @param {string} password - Senha digitada pelo usuário
 */
function validatePassword(password) {
    // Verifica se a senha atende cada requisito
    const lengthValid = password.length >= 8;
    const uppercaseValid = /[A-Z]/.test(password);
    const lowercaseValid = /[a-z]/.test(password);
    const numberValid = /[0-9]/.test(password);
    const specialValid = /[!@#$%^&*(),.?":{}|<>]/.test(password);

    // Atualiza a classe dos itens da lista conforme o requisito é atendido
    lengthItem.className = lengthValid ? 'valid' : 'invalid';
    uppercaseItem.className = uppercaseValid ? 'valid' : 'invalid';
    lowercaseItem.className = lowercaseValid ? 'valid' : 'invalid';
    numberItem.className = numberValid ? 'valid' : 'invalid';
    specialItem.className = specialValid ? 'valid' : 'invalid';

    // Exibe mensagem final se todos os requisitos forem atendidos
    if (lengthValid && uppercaseValid && lowercaseValid && numberValid && specialValid) {
        messageContainer.textContent = '✅ Password is strong!';
    } else {
        messageContainer.textContent = '';
    }
}