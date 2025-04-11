"""
Server: Script Python + Netcat
Objetivo: Descobrir a senha do servidor para que o mesmo envie a chave publica GPG ao cliente
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
    server.bind(("0.0.0.1", 666))
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

        if pacote == "admin123\n":

            client_socket.send(b"Parabens ao acesso ! Aqui esta a chave publica\n\n")

            # Arquivo a ser enviado ao cliente
            with open("File/gpg_public_key.txt", "rb") as file:

                while True:
                    file_data = file.read(1024)

                    if not file_data:
                        break

                    else:
                        client_socket.send(file_data)

                print("Cliente tem acesso ao servidor e a chave publica")
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