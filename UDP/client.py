# Bibliotecas
from socket import socket, AF_INET, SOCK_DGRAM

try:

    # Montagem do socket de conexao
    client = socket(AF_INET, SOCK_DGRAM)

    while True:

        # Envio e recebimentos
        client.sendto((input("Mensagem: ") + "\n").encode(), ("127.0.0.1", 666))
        dados, sender = client.recvfrom(1024)

        # Mensagem
        print(f"{sender[0]}: {dados.decode()}")

except Exception as e:
    print(f"Erro de conexao: {e}")