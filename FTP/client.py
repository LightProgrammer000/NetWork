from ftplib import FTP

# ====== CONFIGURAÇÕES ======
host = "192.168.0.14"           # IP do servidor FTP
port = 2221                     # Porta FTP (troque se precisar, ex: 2221)
user = "android"                # Nome de usuário
passwd = "android"              # Senha

# ====== CONEXÃO ======
ftp = FTP()

print(f"Conectando em {host}:{port}...")
ftp.connect(host, port)
ftp.login(user, passwd)

print("Conectado com sucesso!")

# ====== LISTAGEM DE ARQUIVOS ======
print("\nArquivos no diretório remoto:")
ftp.retrlines("LIST")

# ====== FINALIZA ======
ftp.quit()
print("\nConexão encerrada.")
