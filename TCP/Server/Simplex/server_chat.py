"""
Servidor: Chat com NetCat
"""

# Biblioteca
from socket import socket, AF_INET, SOCK_STREAM, SOL_SOCKET, SO_REUSEADDR

# Montagem
server = socket(AF_INET, SOCK_STREAM)
server.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

# Bind de conexao
server.bind(("127.0.0.1", 666))
server.listen(5)

# Conexao
client_socket, client_address = server.accept()
client_socket.send(b"=-= Bem vindo ao Chat Servidor =-=\nEnvie uma mensagem: ")

while True:

    resp = client_socket.recv(1024).decode()
    if resp == "sair\n":
        break

    print(f"{client_address[0]}: {resp}")

    msg = input("Servidor: ") + "\n"
    if msg == "sair\n":
        break

    client_socket.send(b"Servidor: " + msg.encode())
    client_socket.send(b"Cliente: ")