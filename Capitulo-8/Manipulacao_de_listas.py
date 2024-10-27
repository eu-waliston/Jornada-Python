sacola = ['Arroz', 'Feijão', 'Carne', 'Farinha']

print(f"A lista inicial é: {sacola}")

# METODO: APPEND(objeto)
#Adiciona um item ao fim da lista
sacola.append("Macarrão")
print(f"Lista após o APPEND: {sacola}")

#METODO: EXTEND(estrutura)
#Adiciona todos os itens de outra estrutura ao fim da lista
sacola.extend(['Leite', 'Oléo', 'Maionese'])
print(f"Lista após o EXTEND: {sacola}")

#METODO INSERT(indice, objeto)
#Adiciona um item na posição desejada
sacola.insert(0, "Pão")
print(f"Lista após o INSERT: {sacola}")

#METODO REMOVE(objeto)
#Remove o primerio elemento igual ao valor passado
sacola.remove("Feijão")
print(f"Lista após o REMOVE: {sacola}")

#METODO POP(indice)
#Remove o item da posição desejada da lista e o retorna
#Caso o indice não seja especificado, retorna o último elemento
elemento = sacola.pop(3)
print(f"Lista após o POP: {sacola}")
print(f"Elemento removido: {elemento}")

#METODO CLEAR()
#Removetodos os elementos da lista
# sacola.clear()
# print(f"Lista após o CLAER: {sacola}")

#METODO INDEX(valor, começo, fim)
#Retorna o indice do primeiro elemento do valor especifico
#Podemos ainda passar outros dois parametros que dizem onde pesquisar na lista (coemço e fim)
print(f"Aposição do elemento pesquisado é: {sacola.index("Macarrão",0 ,-1)}")
print(f"Lista após o INDEX: {sacola}")

#METODO COUNT(valor)
#Conta a número de ocorrencias do vlaorespecificado na lsita
print(f"Lista após o COUNT: {sacola.count("Carne")}")

#METODO SORT([chave, recverse)
#Ordena os itens da lista, parametros adicionais podem ser utilizados para customizar a ordenação
sacola.sort(reverse=True)
print(f"Lista após o SORT {sacola}")

#METODO REVERSE()
#Reverte os elementos da lista
sacola.reverse()
print(f"Lista após o REVERSE: {sacola}")

#METODO COPY()
#retorna uma lista com a copia dos elementos da lista de origem
copia_sacola = sacola.copy()
print(f"Lista após o COPY {copia_sacola}")
