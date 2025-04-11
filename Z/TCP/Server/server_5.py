"""
Server: Envio de arquivo mediante ferramenta 'NetCat' (nc -q 1 127.0.0.1 666 < file.txt)
"""

# Bibliotecas
from socket import socket, AF_INET, SOCK_STREAM, SOL_SOCKET, SO_REUSEADDR

from Program.TCP.Client.client_chat import recebido

try:
    # Montando conexao
    server = socket(AF_INET, SOCK_STREAM)
    server.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

    # Bind de Conexao
    server.bind(("0.0.0.0", 666))
    server.listen(5)
    print("Escutando...")

    client_socket, client_address = server.accept() # Conexao em aceitacao
    client_socket.send(b"Envie um arquivo pelo netcat da seguinte forma -> nc -q 1'IP' 'PORTA' < arquivo\n")

    # Dado de conexao
    ip = client_address[0]
    print(f"Conexao estabelecida: {ip}")

    try:
        with open("Files/file.txt", "wb") as file:

            while True:
                data = client_socket.recv(4096)

                if not data:

                    print("Fim da Transmissao")
                    break

                file.write(data)

        print("Arquivo recebido com sucesso!")
        client_socket.send(b"Arquivo enviado com sucesso !")

    except FileNotFoundError as e:
        print(f"Arquivo nao encontrado: {e}")

except KeyboardInterrupt:
    pass

except Exception as e:
    print(f"Erro de conexao {e}")

finally:
    server.close()

