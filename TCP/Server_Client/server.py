"""
Program: Servidor para se conectar com o cliente
"""

# Biblioteca
from socket import socket, AF_INET, SOCK_STREAM, SOL_SOCKET, SO_REUSEADDR

# Montagem
server = socket(AF_INET, SOCK_STREAM)
server.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

# Bind de Conexao
server.bind(("0.0.0.0", 666))
server.listen(5)

print("Escutando ...")
client_socket, client_address = server.accept()

ip = client_address[0]
pacote = client_socket.recv(1024).decode()

print(f"{ip}: {pacote}")
client_socket.send(b"Servidor: Cliente conectado\n")