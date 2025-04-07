let listaDeNumerosSorteados = [];
let limitNumber = 15;
let secretNumber = gerarNumeroAleatorio();
let attempts = 1;



function exibirTextoNaTela (tag, texto) {

    let campo = document.querySelector(tag);
    campo.innerHTML = texto;
    responsiveVoice.speak(texto, 'Brazilian Portuguese Female', {rate: 1.2});

}

exibirTextoNaTela('h1','Game of the secret number');
exibirTextoNaTela('p','Choose a number between 1 and 20');

function exibirMensagemInicial() {
    exibirTextoNaTela('h1','Game of the secret number');
     exibirTextoNaTela('p','Choose a number between 1 and 20');
}

exibirMensagemInicial();


function verificarChute() {
    let = chute = document.querySelector('input').value;

    if (chute == secretNumber) {
        exibirTextoNaTela('h1', 'Got it rigth!');

        let wordAttempt = attempts > 1 ? 'Attempts' : 'Attempt';
        let messageAttempts = `You discover the secret number with ${attempts} ${wordAttempt}!`;

        exibirTextoNaTela('p', messageAttempts);

        document.getElementById('reiniciar').removeAttribute('disabled');
    } else{
        if (chute > secretNumber) {
            exibirTextoNaTela ('h1','You made a mistake !');
            exibirTextoNaTela ('p', 'The secret number is taller');
        } else {
            exibirTextoNaTela ('h1','You made a mistake !');
            exibirTextoNaTela('p', 'The secret number is bigger');
        }
        attempts++;
        clearCamp;
    }
    
}

function gerarNumeroAleatorio() {
    let chooseNumber = parseInt(Math.random() * limitNumber + 1);
    let quantidadeDeElementosNaLista = listaDeNumerosSorteados.length;
     
    if(quantidadeDeElementosNaLista == limitNumber) {
        listaDeNumerosSorteados = [];
    }



    if (listaDeNumerosSorteados.includes(chooseNumber)) {
        return  gerarNumeroAleatorio();

    } else {
        listaDeNumerosSorteados.push(chooseNumber);
        return chooseNumber;
    }
    
}

function clearCamp() {
    chute = document.querySelector('input');
    chute.value = '';
}

function reiniciarJogo() {
    secretNumber = gerarNumeroAleatorio();
    clearCamp();
    attempts = 1;
    exibirMensagemInicial();
    document.getElementById('reiniciar').setAttribute('disabled', true);
    

}