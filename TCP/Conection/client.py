# Bibliotecas
from socket import socket, AF_INET, SOCK_STREAM

try:
    # Montagem
    conexao = socket(AF_INET, SOCK_STREAM)

    # Conexao
    conexao.settimeout(1)
    conexao.connect((input("IP: "), int(input("Porta: "))))

    # Dados
    conexao.send(b"Hacked\n")
    print(conexao.recv(1024).decode())

except Exception as e:
    print("Conexao interrompida !")

except KeyboardInterrupt:
    pass