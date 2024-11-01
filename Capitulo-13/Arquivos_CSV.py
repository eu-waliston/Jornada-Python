resultados = []

with open("cadastro.csv", 'r') as arquivo_entrada:
    linhas = arquivo_entrada.readlines()[1:]

    for linha in linhas:
        dados = linha.split(',')

        nome = dados[1]
        sobrenome = dados[2]
        email = dados[3].replace("\n", "")

        resultados.append(f"{nome} {sobrenome}, {email}\n")

with open("cad_saida.csv", "w") as arquivo_saida:
    for resultado in resultados:
        arquivo_saida.write(resultado)