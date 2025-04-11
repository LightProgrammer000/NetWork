"""
Servidor 1: Chat com NetCat
"""

# Bibliotecas
from socket import socket, AF_INET, SOCK_STREAM, SOL_SOCKET, SO_REUSEADDR

try:

    # Montagem de conexao
    server = socket(AF_INET, SOCK_STREAM)
    server.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

    # Bind de conexao
    server.bind(("0.0.0.0", 666))
    server.listen(5)

    # Conexao esperando ser aceita
    print("Escutando...")
    client_socket, client_address = server.accept()
    client_socket.send(b"=-=-= Chat estabelecido =-=-=\n\n")

    while True:

        # Dados recebidos
        ip = client_address[0]
        recebido = client_socket.recv(1024).decode()

        print(f"{ip}: {recebido}")
        client_socket.send((input("Mensagem: ") + "\n").encode())

except Exception as e:
    print(f"Erro de conexao: {e}")

except KeyboardInterrupt:
    pass

finally:
    server.close()