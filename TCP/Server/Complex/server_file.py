"""
Program:
Envio de arquivo para o servidor
Envio de arquivo mediante ferramenta 'NetCat' (nc -q 1 127.0.0.1 666 < file.txt)
"""

# Biblioteca
from socket import socket, AF_INET, SOCK_STREAM, SOL_SOCKET, SO_REUSEADDR

try:
    # Montagem
    server = socket(AF_INET, SOCK_STREAM)
    server.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

    # Conexao
    server.bind(("0.0.0.0", 666))
    server.listen(5)

    client_socket, client_address = server.accept()
    client_socket.send(b"Bem Vindo ao servidor\n")
    client_socket.send(b"Envie um arquivo, caso use a ferramenta 'Netcat', "
                       b"use a sintaxe: nc -q 1 127.0.0.1 666 < file.txt\n")

    # Arquivo
    try:
        with open("File/file.txt", "w") as file:

            while True:
                file_data = client_socket.recv(1024)

                if not file_data:
                    break

                else:
                    file.write(file_data.decode())

    except Exception as e:
        print(e)

    finally:
        file.close()

except BrokenPipeError:
    print("Erro de conexao")

except KeyboardInterrupt:
    pass