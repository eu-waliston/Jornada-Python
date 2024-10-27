# lista = [1,2,3,4,5,6,7,8,9,10]
from numpy.random import randint

# print(lista)
# print(type(lista))
#
# L = list(["Maça", "Banana", "Laranja"])

# for itens in L:
#     pass
#     # print(itens)
#
# pares = [2,4,6,8]
# impares = [1,3,5,7]

# print(pares[0] * impares[0])
# print(pares[0] ** impares[2])
# print(f"O segundo elemento da lista \'pares\' é {pares[0]}")
# print(pares[-1])
# print(pares[2])

alunos = ["Felipe", "Joao", "Carlos", "Felipe", "Sergio"]

# for aluno_1 in alunos:
#     print(f'O nome do aluno é: {aluno_1}')

# for aluno_2 in alunos:
#     nota = randint(3,10)
#     print(f"A nota do aluno {aluno_2} foi {nota}")

for aluno in alunos:
    n1 = randint(5,10)
    n2 = randint(4,9)
    n3 = randint(3,7)

    n_f = n1 * 0.2 + n2 * 0.3 + n3 * 0.5
    print(f"A nota final do aluno {aluno} foi: {n_f}")
    if n_f >= 6:
        print(f"PARABENS {aluno} pela nota {n_f}")