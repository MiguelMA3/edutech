import random

def jogar():
    print("*********************************")
    print("Bem vindo ao jogo de Adivinhação!")
    print("*********************************")

    numero1 = 1
    numero2 = 0
    tentativas = 0
    pontos = 0

    print("Qual o nível de dificuldade?")
    print("(1) Fácil (2) Médio (3) Difícil")

    nivel = int(input("Defina o nível: "))
    if (nivel == 1):
        tentativas = 3
        numero2 = 10
        pontos = 100
    elif (nivel == 2):
        tentativas = 5
        numero2 = 20
        pontos = 500
    else:
        tentativas = 10
        numero2 = 50
        pontos = 1000

    random.seed(random.randrange(1,100))
    numero_secreto = random.randrange(numero1, numero2) #int(numero_secret) corta os decimais, enquanto round()arredonda o número

    for rodada in range(1, tentativas + 1):
        print("Rodada {} de {}".format(rodada, tentativas))#{0}{1}... para escolher a ordem dos parâmetros
        chute_str = input("Digite um número entre {} e {}: ".format(numero1,numero2))
        chute = int(chute_str)
        print("Você digitou ", chute)

        if (chute < numero1 or chute > numero2):
            print("Você deve digitar um número entre {} e {}!".format(numero1,numero2))
            continue

        acertou = numero_secreto == chute
        maior   = chute > numero_secreto
        menor   = chute < numero_secreto

        pontos_perdidos = abs(pontos - chute)
        pontos = pontos_perdidos

        if (acertou):
            print("Você acertou! Você fez {} pontos!".format(pontos))
            break
        else:
            if (maior):
                print("Você errou! O seu chute foi maior que o número secreto.")
                if (rodada == tentativas):
                    print("O número era: {}".format(numero_secreto))
            elif(menor):
                print("Você errou! O seu chute foi menor que o número secreto.")
                if (rodada == tentativas):
                    print("O número era: {}".format(numero_secreto))

    print("Fim do jogo!")

if (__name__ == "__main__"):
    jogar()