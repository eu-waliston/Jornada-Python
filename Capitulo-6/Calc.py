n1 = input("Digite o primeiro numero")
n2 = input("Digite o segundo numero")

print("Digite a operação:\n\t+ para Adição\n\t- para Subtração\n\t* para Multiplicação\n\t/ para Divisão")

operacao = input("Digite a operação: ")

equacao = f"{n1} {operacao} {n2}"

result = eval(equacao)

print(f" Resultado: {result}")