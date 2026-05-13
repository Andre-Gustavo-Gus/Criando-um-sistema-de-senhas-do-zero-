banco_dados = {
    "admin": "admin"
}

while True:
    print("Faça seu login")
    user = input("Seu nome de usuario:")
    senha = input("Digite sua senha:")

    if user in banco_dados and banco_dados[user] == senha:
        break

    else:
        print("Erro! Usuario ou senha estão incorretos")
        