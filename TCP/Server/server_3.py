"""
Server: TCP + Netcat
Objetivo: Descobrir a senha do servidor para que o mesmo envie a chave publica GPG ao cliente
"""

# Bibliotecas
from socket import socket, AF_INET, SOCK_STREAM, SOL_SOCKET, SO_REUSEADDR

# Contador de tentativas
cont= 0

try:
    # Montagem de conexao
    server = socket(AF_INET, SOCK_STREAM)
    server.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

    # Bind de conexao
    server.bind(("127.0.0.1", 666))
    server.listen(5)
    print("Escutando...")

    client_socket, client_address = server.accept() # Conexao em aceitacao
    client_socket.send(b"Bem Vindo, necessito da senha para enviar a chave GPG\n")
    client_socket.send("\nSenha: ".encode())

    while True:

        ip = client_address[0]
        recebido = client_socket.recv(1024).decode()

        if recebido == "senha123\n":

            try:
                with open("Files/gpg_public_key.txt", "rb") as file:

                    # Leitura aos pedacos do arquivo
                    file_data = file.read(1024)

                    while file_data:

                        # Cliente recebe em pedaços de 1024 bytes
                        client_socket.send(file_data)
                        file_data = file.read(1024)

                client_socket.send(b"Arquivo enviado com sucesso !\n")
                break

            except FileNotFoundError:
                print("Arquivo nao encontrado !")

        else:

            if cont < 2:
                cont += 1
                client_socket.send(b"Incorreto !\n")
                client_socket.send("\nSenha: ".encode())

            else:
                client_socket.send(b"Tentativas incorretas, servidor bloqueado\n")
                break


except Exception as e:
    print(f"Erro de conexao ! {e}")

except KeyboardInterrupt:
    print("Servidor finalizado !")

finally:
    server.close()