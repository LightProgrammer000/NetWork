"""
Program: Cliente FTP
Alvo: ftp.unicamp.br
"""

# Bibliotecas
from ftplib import FTP

# Classe
class FTP_UNICAMP:

    # Construtor
    def __init__(self):

        self.host = "ftp.unicamp.br"  # Servidor FTP
        self.port = 21
        self.username = "anonymous"
        self.password = "anonymous"


    # Objeto String
    def __str__(self):
        return "FTP Unicamp"


    # Conexao
    def conexao(self):

        # Montagem de conexao (objeto)
        ftp = FTP()

        # Conectado
        ftp.connect(self.host, self.port)
        ftp.login(user=self.username, passwd=self.password)

        # Mensagem
        print("Conectado com sucesso !")
        print(f"Server -> {self.host}: {self.port}\n")

        return ftp


    # Listagem
    def listagem(self, ftp):

        if ftp:
            ftp.retrlines("LIST")
            print("\nListagem completa de diretorios | Servidor em operacao !")


# Testes
ftp_unicamp = FTP_UNICAMP()
conecta = ftp_unicamp.conexao()
ftp_unicamp.listagem(conecta)