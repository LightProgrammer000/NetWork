"""
Cliente: Requisicao HTTP por meio TCP
"""

# Bibliotecas
from socket import socket, AF_INET, SOCK_STREAM

try:
    # Montagem de conexao
    client = socket(AF_INET, SOCK_STREAM)

    # Conexao
    client.connect(("google.com", 80))
    client.settimeout(1)

    # Envio + Resposta
    client.send(b"GET / HTTP/1.1\nHost:www.google.com\n\n")
    pacotes = client.recv(1024).decode()

    # Mensagem
    print(pacotes)

except Exception as e:
    print(f"Erro na conexao: {e}")