"""
Chat: Python + Netcat (nc -lvp 666)
"""

# Bibliotecas
from socket import socket, AF_INET, SOCK_STREAM

try:

    # Montagem de conexao
    client = socket(AF_INET, SOCK_STREAM)

    # Conexao
    client.connect(("127.0.0.1", 666))

    while True:

        # Envio + Recebimentos
        msg = input("Mensagem: ") + "\n"

        if msg == "sair\n":
            break
        else:
            mensagem = client.send(msg.encode())

        recebido = client.recv(1024).decode()
        if recebido == "sair\n":
            break
        else:
            print(f"Servidor: {recebido}")

except KeyboardInterrupt:
    pass

except Exception as e:
    print(f"Conexao encerrada ! {e}")

