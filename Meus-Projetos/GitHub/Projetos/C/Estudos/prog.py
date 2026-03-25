import random
saldo = 100
print("--- Menu do Tigrinho ---\n   [1] - Aposta\n   [2] - saldo\n   [0] - Sair")
escolha = input("Escolha uma opção: ")
match escolha:
    case 1:
        print("---Menu de aposta---")
        valor_aposta = input("Qual o valor da sua aposta: ")
        numero = int(input("Digite um numero: "))
        if valor_aposta > saldo:
            valor_aleatorio = random.choice(1,50)
            if numero == valor_aleatorio:
                
