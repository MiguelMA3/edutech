import adivinhacao
import forca

def escolhe_jogo():

    print("*********************************")
    print("*************JOGOS***************")
    print("*********************************")

    print("(1) Forca (2) Adivinhação")

    jogo = int(input("O que vamos jogar? "))

    if (jogo == 1):
        print("Você escolheu forca.")
        forca.jogar()
    elif (jogo == 2):
        print("Você escolheu adivinhação.")
        adivinhacao.jogar()

if (__name__== "__main__"):
    escolhe_jogo()