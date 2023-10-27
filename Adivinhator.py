import random

print("Eu sou o adivinhator, vou pensar em um numero de 1 a 10 e voce precisa acertar.")

numeroPensado = random.randint(1,10)

while True:
    numeroDigitado = int(input("Em qual número eu estou pensando? "))
    if numeroDigitado == numeroPensado:
        print("Parabéns voce acertou")
        break
    else:
        print("Errou, tente novamente")
