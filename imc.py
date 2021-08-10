altura = float(input("Qual sua altura?").strip())
sexo = input("Qual seu sexo? M ou F?").strip()
homem = 'M'
mulher = 'F'

if (sexo.lower() == homem.lower()):
    peso_ideal = (72.7 * altura) - 58

if (sexo.lower() == mulher.lower()):
    peso_ideal = (62.1 * altura) - 44.7

print("O peso ideal para você seria de {0:.2f} Kg.".format(peso_ideal))