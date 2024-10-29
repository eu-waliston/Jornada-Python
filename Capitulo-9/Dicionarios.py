# # Criando seus primeiros Dicionários
#
# cadastro = {
#     "id" : 1,
#     "nome" : "Oliver Sykes",
#     "filhos" : ["Lucas", "Felipe", "Maria"],
#     "compras" : [
#         {
#             "id" : 2144,
#             "produto" : "Notebook Gameer",
#             "preço" : 2345.89
#         }
#     ]
# }
#
# # print(cadastro["Compras"][0])
# # # print(f"O usuário {cadastro['nome']} pai de {cadastro['filhos'][-1]}")
# # # print(f"O usuário {cadastro['nome']} Efetuou a compra\n\t{cadastro['cadastro'["compras"]})
# #
# # usuario = cadastro.get("nome")
# # notebook_games = cadastro['compras'][0]
# # print(f"O usuário {usuario}\nrealizou a seguinte compra:\n{notebook_games['produto']}")
#
# # Adicionando e atualizando elementos em Dicionários
#
# computador = {
#     'cpu' : 'Core i7',
#     'ram' : 'DDR4 16Gb',
#     'ssd' : 'Samsung Evo 840 500Gb',
#     'gpu' : 'RTX 2080 Ti'
# }
#
# print(f'Computador v1:{computador}')
#
# computador['ram'] = 'DDR4 32Gb'
#
# print(f'Computador v2:{computador}')
#
# computador['fonte'] = 'Fonte 60Wt Corsair'
#
# print(f'Computador v3:{computador}')
#
# computador.update({
#     'fonte' : 'Fonte Corsair 850',
#     'ssd' : '1Tb',
#     'cpu' : 'Cire i9'
# })
#
# print(f'Computador v4:{computador}')
#
# # Excluindo elementos de Dicionários
# fila = {
#     '0' : 'João',
#     '1' : 'Joana',
#     '2' : 'Clara',
#     '3' : 'Ana',
#     '4' : 'Julio'
# }
#
# print(fila)
#
# # del
# del fila['0']
#
# print(fila)
#
# # pop
#
# valor_retirado = fila.pop('1')
# print(valor_retirado)
# print(fila)
#
# # popitem >> delkerta sermpre o ultimo eleemnto do dicionario
# valor_r = fila.popitem()
# print(fila)
#
# #clear >> limpa todos os elementos do dicionario
# fila.clear()
# print(fila)

# Métodos de Dicionários

familia = {
    'pai' : 'Jose sa Silva',
    'mae' : 'Ana Almeida',
    'filho' : 'Cléber da Silva Almeida',
    'filha' : 'Joana da Silva Almeida'
}

print(f"Familia >> {familia}")

# COPY
# cria uam copia do dicionario
copia_familia = familia.copy()
print(f"Copia do dicionario Familia >> {copia_familia}")

# ITENS
# retorna os apres chave e valor no formarto lista
itens = familia.items()
# print(f'Itens: ', itens)
for item in itens:
    print(item)

# KEYS
# retorna todas as chaves em formato de lista

keys = familia.keys()
for key in keys:
    print(key)

# VALUES
# retorna apenas os valores
values = familia.values()
for value in values:
    print(value)

#SETDEFAULT
# insere a chave e o valor passado SE a chave não estiver no dicionario
# retorna o vlaor da chabe SE a chave ja estiver presente no dicionario

familia.setdefault('sobrinho' , 'Zé Felipe')

# familia.setdefault('mae', 'Maria Tereza') >> dont override the value ^^

print(f"Familia >> {familia}")

#FROMEKYS
# cria um dicionario a partir de uma lista de chaves e um valor
chaves = ['mae','pai', 'filho', 'filha']
valor = 0

jogo = dict.fromkeys(chaves, valor)
print(f"o jogo {jogo}")



















