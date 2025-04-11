"""
Server: Enviando mensagem para ser enviado ao arquivo
"""

# Biblioteca
from socket import socket, AF_INET, SOCK_STREAM, SOL_SOCKET, SO_REUSEADDR

try:
    # Montagem de conexao
    server = socket(AF_INET, SOCK_STREAM)
    server.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

    # Bind de conexao
    server.bind(("0.0.0.0", 666))
    server.listen(5)
    print("Escutando...")

    client_socket, client_address = server.accept() # Conexao em aceitacao
    client_socket.send(b"\nEnvie um mensagem ao servidor para ser colocado ao arquivo interno\n") # Envio de mensagem

    # Pacotes recebidos
    ip = client_address[0]
    recebido = client_socket.recv(1024).decode()

    print(f"{ip}: {recebido}")

    try:
        with open("Files/mensagem.txt", "w") as file:
            file.write(recebido)

    except Exception as e:
        print("Arquivo nao encontrado !")

except KeyboardInterrupt:
    pass

except Exception as e:
    print(f"Erro de conexao {e}")

finally:
    server.close()