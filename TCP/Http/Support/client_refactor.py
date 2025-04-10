# Biblioteca
from socket import socket, AF_INET, SOCK_STREAM


def montagem_conexao():

    try:
        return socket(AF_INET, SOCK_STREAM)

    except Exception as e:
        print(f"Montagem de conexao falhou!: {e}")
        return None


def conexao():

    try:
        client = montagem_conexao()
        client.settimeout(1)

        # Envio de pacotes + recebimentos
        client.connect(("google.com", 80))
        client.send(b"GET / HTTP/1.1 \nHost: www.google.com\n\n")

        return client

    except Exception as e:
        print(f"Falha na conexao: {e}")
        return None


def resposta():

    try:
        pacotes = conexao()

        recebidos = pacotes.recv(1024).decode()
        return recebidos

    except Exception as e:
        print(f"Pacotes recebidos {e}")
        return None


def main():
    print(resposta())


# Execucao
if __name__ == '__main__':
    main()

