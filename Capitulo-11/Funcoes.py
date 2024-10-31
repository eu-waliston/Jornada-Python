# def welcome():
#      nome = input("Olá qual seu nome: ")
#      func = input("Qual sua função: ")
#      return print(f"Bem-vindo {nome} Voce agora é nosso {func}")
#
# welcome()

# def soma2(n1,n2):
#     return n1 + n2
#
# print(f"Soma: {soma2(3,4)}")

def cal_media_mediana(notas):
    mediana = 0
    media = sum(notas) / len(notas)
    if len(notas) % 2 == 0:
        central_menor = len(notas) / 2 - 1
        central_maior = len(notas) / 2

        ponto_menor = notas[int(central_menor)]
        ponto_maior = notas[int(central_maior)]

        mediana = (ponto_menor + ponto_maior) / 2
    else:
        notas_ordenadas = sorted(notas)
        indice_mediana = int(len(notas) / 2)
        mediana = notas_ordenadas[indice_mediana]
    return media, mediana


resultado_media, resultado_mediana = cal_media_mediana([5,6,4, 5])
print(resultado_media)
print(resultado_mediana)
