# Bibliotecas
from socket import socket, AF_INET, SOCK_STREAM

try:
    # Montagem de conexao: Socket
    client = socket(AF_INET, SOCK_STREAM)

    # Conexao
    client.connect(("127.0.0.1", 666))

    # Dados
    client.send(b"Hacked\n")
    pacotes_recebidos = client.recv(1024).decode()

    # Mensagem decodificada
    print(pacotes_recebidos)

except Exception as e:
    print(f"Conexao encerrada: {e}")