"""
Server: TCP + Netcat
Objetivo: Descobrir a senha do servidor
"""

# Bibliotecas
from socket import socket, AF_INET, SOCK_STREAM, SOL_SOCKET, SO_REUSEADDR

# Contador
cont = 0

try:
    # Montagem
    server = socket(AF_INET, SOCK_STREAM)
    server.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

    # Conexao
    server.bind(("127.0.0.1", 666))
    server.listen(5)
    print("Servidor escutando ...")

    client_socket, client_address = server.accept()
    client_socket.send(b"Bem vindo ao servidor\n")
    client_socket.send(b"Adivinha a senha para o acesso -> Voce tem 4 tentativas\n\n")
    client_socket.send(b"Senha: ")

    while True:

        ip = client_address[0]
        pacote = client_socket.recv(1024).decode()

        print(f"{ip}: {pacote}")

        if pacote == "senha123\n":
            client_socket.send(b"Parabens ao acesso !")
            print("Cliente tem acesso ao servidor")
            break

        else:
            cont += 1

            if cont < 4:
                client_socket.send(f"Tentativa ({cont}): ".encode())

            else:
                client_socket.send(f"IP: {ip} rastreado ! Fim das tentativas".encode())
                break

except KeyboardInterrupt:
    pass

except BrokenPipeError as e:
    print(f"Conexao encerrada")

finally:
    server.close()