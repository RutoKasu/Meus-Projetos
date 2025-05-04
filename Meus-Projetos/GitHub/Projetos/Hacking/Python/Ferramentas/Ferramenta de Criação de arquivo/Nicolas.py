import socket
import os 
import getpass
import platform

caminho_windows = f"C:\\Users\\{getpass.getuser()}\\Desktop"
caminho_linux = f"/home/{getpass.getuser()}/Desktop"

var_os = platform.system()

if var_os == "Linux":
    os.chdir(caminho_linux)
if var_os == "Windows":
    os.chdir(caminho_windows)

else:
    print("Os not found")

os.mkdir("Dados")
os.chdir("Dados")

with open("DadosColetados.txt","w") as f:
    f.write("Teste de Coleta de dados.\n")
    f.write(f"User: {getpass.getuser()}\n")
    f.write(f"IP: {socket.gethostbyname(socket.gethostname())}\n")
    f.write(f"OS: {platform.system()}")