"""
Server: Enviando mensagem pelo cliente para ser gravado no servidor
"""

# Bibliotecas
from socket import socket, AF_INET, SOCK_STREAM, SOL_SOCKET, SO_REUSEADDR

try:
    # Montagem
    server = socket(AF_INET, SOCK_STREAM)
    server.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

    # Conexao
    server.bind(("127.0.0.1", 666))
    server.listen(5)

    print("Escutando...")
    client_socket, client_address = server.accept()

    client_socket.send("=-= Bem Vindo ao Servidor =-=\n".encode())
    client_socket.send(b"\n# Mensagem: ")

    try:
        with open("File/message.txt", "w") as file:

            recebido = client_socket.recv(1024).decode()
            file.write(recebido)

        print(f"{client_address[0]}: {recebido}")
        print("Mensagem recebida !")

    except FileNotFoundError:
        print("Arquivo nao encontrado !")

except BrokenPipeError:
    print("Conexao encerrada !")

except KeyboardInterrupt:
    pass

finally:
    server.close()