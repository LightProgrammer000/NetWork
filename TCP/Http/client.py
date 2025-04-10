"""
Cliente: TCP
"""

# Bibliotecas
from socket import socket, AF_INET, SOCK_STREAM

try:

    # Montagem de conexao: Criando Socket
    client = socket(AF_INET, SOCK_STREAM)

    # Conexao
    client.connect(("www.google.com.br", 80))
    client.settimeout(1)

    # Envio de requisicao e recebimento
    client.send(b"GET / HTTP/1.1\nHost: www.google.com\n\n")
    pacotes_recebidos = client.recv(1024).decode()

    print(pacotes_recebidos)

except Exception as e:
    print(f"Erro de conexao: {e}")