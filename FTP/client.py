"""
Program: Cliente FTP
Alvo: ftp.unicamp.br
"""

# Bibliotecas
from ftplib import FTP


def conexao():

    try:
        # Configuracoes
        host = "ftp.unicamp.br"  # Servidor FTP
        port = 21
        username = "anonymous"
        password = "anonymous"

        # Montagem de conexao (objeto)
        ftp = FTP()

        # Conexao
        ftp.connect(host, port)
        ftp.login(user=username, passwd=password)

        # Mensagem
        print("Conectado com sucesso !")
        print(f"Server -> {host}: {port}\n")

        # Retorno de objeto
        return ftp

    except Exception as e:
        print(f"Erro de conexao: {e}")


def listagem(ftp):

    try:
        if ftp:
            ftp.retrlines("LIST")
            print("\nListagem completa de diretorios | Servidor em operacao !")

    except Exception as e:
        print(f"Erro de comando {e}")

    finally:
        ftp.quit()
        ftp.close()


def main():

    try:
        resposta = conexao()

        if resposta:
            listagem(resposta)

    except Exception as e:
        print(f"Erro de conexao: {e}")

if __name__ == '__main__':
    main()