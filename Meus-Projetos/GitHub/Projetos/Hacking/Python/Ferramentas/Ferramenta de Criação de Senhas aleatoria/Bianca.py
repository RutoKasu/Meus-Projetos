import random
import string
import os
import getpass
import sys

senha = []

tamanho = int(input("Digite o tamanho da senha: "))

esc_caracteres = int(input("Deseja oque: \n[1] Todos os caracteres \n[2] sem numero\n[3] sem caracteres especiais\n[4] letras minusculas\n[5] letras maiusculas\n[6] Todas as letras\n "))
if esc_caracteres == 1:
    caracteres = string.ascii_letters + string.digits + string.punctuation
elif esc_caracteres == 2:
    caracteres = string.ascii_letters + string.punctuation
elif esc_caracteres == 3:
    caracteres = string.ascii_letters + string.digits
elif esc_caracteres == 4:
    caracteres = string.ascii_lowercase
elif esc_caracteres == 5:
    caracteres = string.ascii_uppercase
elif esc_caracteres == 6:
    caracteres = string.ascii_letters
else:
    print("Número inválido!")
    sys.exit()


for i in range(tamanho):
    esc = random.choice(caracteres)
    senha.append(esc)

print(senha)

caminho = (f"C:\\Users\\{getpass.getuser()}\\Desktop")
os.chdir(caminho)
with open("Senha.txt","w") as f:
    for i in senha:
        f.write(i)
    
