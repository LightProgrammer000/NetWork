"""
Client: SSH
Server: bandit.labs.overthewire.org
Porta: 2220
"""

# Biblioteca
from paramiko import SSHClient, AutoAddPolicy

try:
    # Configuracoes
    host = "bandit.labs.overthewire.org"
    port = 2220
    username = "bandit0"
    password = "bandit0"

    # Montagem
    client = SSHClient()
    client.set_missing_host_key_policy(AutoAddPolicy())

    # Conexao
    client.connect(hostname=host, port=2220, username=username, password=password)

    # Loop: Comandos infinitos
    while True:

        # Resposta
        stdin, stdout, stderr = client.exec_command(input("Comando: "))

        if stdout:
            print(stdout.read().decode())

        if stderr:
            print(stderr.read().decode())

except Exception as e:
    print(f"Erro na conexao SSH: {e}")