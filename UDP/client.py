"""
Conexao UDP + Netcat (nc -luvp 666)
"""

# Biblioteca
from socket import socket, AF_INET, SOCK_DGRAM

try:
    # Montagem de conexao
    client = socket(AF_INET, SOCK_DGRAM)

    while True:

        client.sendto((input("Mensagem: ") + "\n").encode(), ("127.0.0.1", 666))
        recebido, address = client.recvfrom(1024)

        print(f"{address[0]}: {recebido.decode()}")

except Exception as e:
    print(f"Erro de conexao: {e}")