import json

try:
    with open("banco_dados.json", "r", encoding="utf-8") as arquivo:
        dados = json.load(arquivo)
except (FileNotFoundError, json.JSONDecodeError):

    dados = {}
    with open("banco_dados.json", "w", encoding="utf-8") as arquivo:
        json.dump(dados, arquivo)

#Funções

#Funções de menu
def criar():
    print(f"{50*"="}")
    print("Faça seu cadastro!\n")
    while True:

        nome = input("Digite seu nome de usuario:").lstrip()
        senha = input("Digite sua senha:").lstrip()

        if nome in dados:
            print("\nErro: Este usuário já existe!")
            continue 

        print(f"\n{nome} \nDeseja salvar seu cadastro?\n")
        resposta = input("S/N :").strip() .upper() 
        if resposta == "S":

            dados[nome] = senha

            with open("banco_dados.json", "w", encoding="utf-8") as arquivo:
                json.dump(dados, arquivo, indent=4, ensure_ascii=False)

            if nome in dados:
                print("\nCadastro concluido com sucesso!")    
                return True

        else:
            print("\nFaça seu cadastro novamente...")

def logar():
    print(f"{50*"="}")        
    print("Faça o seu Login:")

    while True:
        nome = input("Digite seu nome de usuario:").lstrip()
        senha = input("Digite sua senha:").lstrip()

        if nome in dados and dados[nome] == senha:
            return True

        else:
            print("\nUsuario ou senha errados, tente novamente")   

#Menu
while True: 

    print(f"{60*"="}")

    print("Qual das opções abaixo voce gostaria de executar?\n" \
    "[1] Criar login\n[2] Logar ")

    opcoes = input("\ninsira aqui:")

    if opcoes == "1":
        criar()
        break

    elif opcoes == "2":
        logar()
        break

    else:
        print("Erro, Opção não existente, tente:\n[1] Criar login\n[2] Logar")
    

print("\nOlá!")
