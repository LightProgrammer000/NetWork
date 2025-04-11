"""
Client: SSH
"""

from paramiko import SSHClient, AutoAddPolicy

host = ""
user = ""
passwd = ""

# Montagem de conexao
client = SSHClient()
client.set_missing_host_key_policy(AutoAddPolicy())
client.connect(host, username=user, password=passwd)

while True:

    try:
        stdin, stdout, stderr = client.exec_command(input("Comando: "))
        print(stdout.read().decode())

        if stderr:
            print(stderr.read().decode())

    except Exception as e:
        print(e)