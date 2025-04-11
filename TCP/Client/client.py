"""
Conexao: TCP
Server: NetCat (nc -lvp 666)
"""

# Bibliotecas
from socket import socket, AF_INET, SOCK_STREAM

try:

    # Montagem de conexao
    client = socket(AF_INET, SOCK_STREAM)

    # Conexao
    ip = input("IP: ")
    porta = int(input("PORTA: "))

    client.connect((ip, porta))
    client.settimeout(1)

    # Envio e Recebimento
    client.send(b"Envio de conexao\n")
    pacotes = client.recv(1024).decode()

    # Pacotes
    print(pacotes)

except Exception as e:
    print(f"Ligacao finalizada  {e}")