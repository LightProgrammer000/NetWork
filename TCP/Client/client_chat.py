"""
Programa: Chat
Ferramenta: Script python + Netcat (nc -lvp 666)
"""

# Bibliotecas
from socket import socket, AF_INET, SOCK_STREAM

try:
    # Montagem
    client = socket(AF_INET, SOCK_STREAM)

    # Conexao
    ip = "127.0.0.1"
    porta = 666
    client.connect((ip, porta))

    while True:

        # Envio + Recebimento
        msg = input("Cliente: ") + "\n"

        if msg == "sair":
            break

        client.send(msg.encode())
        pacote = client.recv(1024).decode()

        if pacote == "sair\n":
            break

        print(f"Servidor ({ip}): {pacote}")

except KeyboardInterrupt:
    pass

except Exception as e:
    print(f"Erro de conexao: {e}")

finally:
    client.close()