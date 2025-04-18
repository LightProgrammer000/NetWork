"""
Conexao: Programa python
Server: NetCat (nc -lvp 666)
"""

# Bibliotecas
from socket import socket, AF_INET, SOCK_STREAM

try:

    # Montagem
    client = socket(AF_INET, SOCK_STREAM)

    # Conexao
    client.connect(("127.0.0.1", 666))
    print("Conexao estabelecida, aguardando mensagem de confirmacao...")

    # Envio + Recebimento
    client.send(b"Conexao estabelecida\nEnvie um mensagem de confirmacao: ")
    pacote = client.recv(1024).decode()

    # Mensagem
    print(f"Cliente: {pacote}")

except KeyboardInterrupt:
    pass

except Exception as e:
    print(f"Conexao encerrada: {e}")