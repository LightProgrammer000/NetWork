"""
Cliente: Requisicao HTTP
"""

# Bibliotecas
from socket import socket, AF_INET, SOCK_STREAM

try:
    # Montagem
    client = socket(AF_INET, SOCK_STREAM)

    # Conexao
    client.connect(("google.com", 80))
    client.settimeout(1)

    # Envio + Recebimento
    client.send(b"GET / HTTP/1.1\nHost:www.google.com\n\n")
    pacote = client.recv(1024).decode()

    # Mensagem
    print(pacote)

except Exception as e:
    print(f"Erro de conexao: {e}")