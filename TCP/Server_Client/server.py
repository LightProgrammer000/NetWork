"""
Server: TCP
"""

from socket import socket, AF_INET, SOCK_STREAM, SOL_SOCKET, SO_REUSEADDR

try:

    # Montagem de servidor
    server = socket(AF_INET, SOCK_STREAM)
    server.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

    # Bind
    server.bind(("0.0.0.0", 666))
    server.listen(5)

    # Aceitando conexoes
    print("Escutando ...")
    client_socket, client_conection = server.accept()
    print("Conexao estabelecida")

    # Dados recebidos
    recebido = client_socket.recv(1024).decode()
    ip = client_conection[0]
    print(f"{ip}: {recebido}")

    # Envio de mensagem
    client_socket.send(b"Conexao estabelecido com o servidor\n")

except KeyboardInterrupt:
    pass

except Exception as e:
    print(e)

finally:
    server.close()