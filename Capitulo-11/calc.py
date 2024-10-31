def soma():
    n1 = input("Digite o primeiro numero: ")
    n2 = input("Digite o segundo numero: ")
    res = int(n1) + int(n2)
    print(f"O resutlado é {res}")

def subtracao():
    n1 = input("Digite o primeiro numero: ")
    n2 = input("Digite o segundo numero: ")
    res = int(n1) - int(n2)
    print(f"O resutlado é {res}")

def multiplicacao():
    n1 = input("Digite o primeiro numero: ")
    n2 = input("Digite o segundo numero: ")
    res = int(n1) * int(n2)
    print(f"O resutlado é {res}")

def divisao():
    n1 = input("Digite o primeiro numero: ")
    n2 = input("Digite o segundo numero: ")
    res = int(n1) / int(n2)
    print(f"O resutlado é {res}")

def main__caluladora():
    print("Calculadora:")
    print("\t1 - Soma")
    print("\t2 - Subtração")
    print("\t3 - Multiplicar")
    print("\t4 - Divisão")
    option = input("O que deseja fazer: ")

    if option == "1":
        soma()
    elif option == "2":
        subtracao()
    elif option == "3":
        multiplicacao()
    elif option == "4":
        divisao()
    else:
        print("OPÇÃO INVALIDA!!!!!!!")

main__caluladora()