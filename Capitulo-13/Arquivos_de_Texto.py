import os

caminho = 'dados.txt'

texto_1 = "Jornada Python - Manipulação de Arquivos\n"
texto_2 = "Venha DOMINAR Python"

if os.path.exists(caminho) and os.path.getsize(caminho) != 0:
    arquivo_a_ser_lido = open("dados.txt", "r")
    retorno = arquivo_a_ser_lido.read()
    print(retorno)
    arquivo_a_ser_lido.close()
else:
    arquivo = open("dados.txt", "a")
    arquivo.write(texto_1)
    arquivo.write(texto_2)
    arquivo.close()
