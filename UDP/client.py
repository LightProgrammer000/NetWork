"""
Programa: Client UDP
"""

# Biblioteca
from socket import socket, AF_INET, SOCK_DGRAM

try:
    # Montagem
    client = socket(AF_INET, SOCK_DGRAM)

    while True:

        # Envio de mensagem
        msg = input("Mensagem: ")

        if msg == "sair":
            break

        else:
            envio = client.sendto(f"{msg}\n".encode(), ("127.0.0.1", 666))

            # Reposta
            pacote, address = client.recvfrom(1024)

            if pacote.decode() == "sair\n":
                break

            print(f"{address[0]}: {pacote.decode()}")

except KeyboardInterrupt:
    pass

except Exception as e:
    print(f"Erro de conexao: {e}")