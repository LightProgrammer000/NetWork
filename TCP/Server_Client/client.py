"""
Program: Cliente para se conectar com o servidor
"""

# Biblioteca
from socket import socket, AF_INET, SOCK_STREAM

try:
    # Montagem
    client = socket(AF_INET, SOCK_STREAM)

    # Conexao
    client.connect(("127.0.0.1", 666))
    client.settimeout(1)

    # Envio + Recebimentos
    client.send(b"Cliente se conectando...\n")

    resposta = client.recv(1024).decode()
    print(resposta)

    print("Conexao com servidor estabelecida")

except BrokenPipeError:
    print("Conexao interrompida !")

except KeyboardInterrupt:
    print("Programa Finalizado !")