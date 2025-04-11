"""
Client: TCP
"""

# Bibliotecas
from socket import socket, AF_INET, SOCK_STREAM

try:

    # Montagem de conexao com sockets
    client = socket(AF_INET, SOCK_STREAM)

    # Conexao
    client.connect(("127.0.0.1", 666))
    client.settimeout(1)

    # Envio + Recebimentos
    client.send(b"Pedido de conexao com o servidor\n")
    recebido = client.recv(1024).decode()

    # Resposta
    print(recebido)

except Exception as e:
    print(f"Erro de conexao: {e}")