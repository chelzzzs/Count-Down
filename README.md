# Count-Down
Temporizador programado em phyton. Onde o usuário digita um número inteiro e o código converte este número para variáveis de minutos : segundos. Após inicia uma contagem que se encerra no 0. 

🚀 Como usar
Execute o script em um terminal ou ambiente Python.

Digite o tempo desejado em segundos quando solicitado.

O programa exibirá uma contagem regressiva em tempo real no formato MM:SS.

Ao final do tempo, a mensagem "TEMPO ESGOTADO" será exibida.

📦 Requisitos
Python 3.x

🧠 Como funciona
Solicita que o usuário digite o tempo em segundos.

Verifica se a entrada é um número inteiro válido usando isdigit().

Converte os segundos para o formato minutos:segundos com divmod().

Usa time.sleep(1) para aguardar 1 segundo entre cada iteração da contagem.

Atualiza a exibição do tempo na mesma linha com \r e end="".
