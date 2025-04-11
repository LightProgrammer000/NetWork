"""
Conexao: Script python
Server: NetCat <nc -lvp 666>
"""

# Bibliotecas
from socket import socket, AF_INET, SOCK_STREAM

try:
    # Configuracoes
    ip = input("IP: ")
    porta = int(input("PORTA: "))

    # Montagem
    client = socket(AF_INET, SOCK_STREAM)

    # Conexao
    client.connect((ip, porta))
    print("Conexao estabelecida, aguardando cliente confirmar...")

    # Envio + Recebimento
    client.send(b"Conexao cliente\nEnvie uma mensagem de confirmacao: ")
    pacote = client.recv(1024).decode()

    # Mensagem
    print(pacote)

except KeyboardInterrupt:
    pass

except Exception as e:
    print(f"Conexao encerrada: {e}")