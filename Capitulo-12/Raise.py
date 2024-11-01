#Nome, iIdade, Cargo
cadastro_csv = [
    "Joao, 28w, Analista de Sistemas",
    "Maria, 31, Desenvolvedora Frontend",
    "Jonas, 37, Gerente de Projeto",
    "Alberto, 47"
]

def processa_dados(cadastros):
    for cadastro in cadastros:
        dados = cadastro.split(',')

        if len(dados) != 3:
            raise ValueError("Formato incorreto dos dados")

        nome = dados[0]
        try:
            idade = int(dados[1])
        except ValueError:
            raise ValueError("Erro no formato de dado 'Idade'")
        cargo = dados[2]

        print(f"{nome} tem {idade} e exerce o cargo de {cargo}")


try :
    processa_dados(cadastro_csv)

except ValueError as err:
    print(f"O programa encontrou um erro, ERRO: {err}")