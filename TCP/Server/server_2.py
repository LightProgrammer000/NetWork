"""
Server: TCP + Netcat
Objetivo: Descobrir a senha do servidor
"""

# Bibliotecas
from socket import socket, AF_INET, SOCK_STREAM, SOL_SOCKET, SO_REUSEADDR

try:

    # Montagem de servidor
    server = socket(AF_INET, SOCK_STREAM)

    # Bind de conexao
    server.bind(("0.0.0.0", 666))
    server.listen(5)

    print("Escutando...")
    client_socket, client_address = server.accept()
    client_socket.send(f"{'=-=' * 5} Informa a senha ao servidor {'=-=' * 5}\n".encode())

    while True:

        # Dados recebidos
        recebido = client_socket.recv(1024).decode()
        ip = client_address[0]

        print(f"{ip}: {recebido}")

        if recebido == "senha123\n":
            client_socket.send(b"Acesso ao servidor concedido !\n")
            break

        else:
            client_socket.send(b"Tente novamente !\n")

except KeyboardInterrupt:
    pass

except Exception as e:
    print(f"Erro de conexao: {e}")

finally:
    server.close()