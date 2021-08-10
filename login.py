nome = str(input("Nome: "))
username = str(input("Username: "))
senha = str(input("Senha: "))
while senha == username or senha == nome:
    print("A senha não pode ser igual ao usuário!")
    senha = str(input("Senha: "))

def login():
    qualusuario = str(input("Usuário: "))
    qualsenha = str(input("Senha: "))
    if qualsenha == senha:
        print(f"Bem-Vindo {nome}!")
    else:
        str(input("Informe a senha correta"))

login()

