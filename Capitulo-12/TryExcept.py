
def divide_dois_numeros(dividendo, divisor):
    return dividendo / divisor

try:
    # codigo a ser testato
    numero_1 = (input("Digite um numero"))
    numero_2 = int(input("Digite um numero"))

    resultado = divide_dois_numeros(numero_1, numero_2)

except (ZeroDivisionError, TypeError) as erro:

    print(f"Divisão por ZERO não suportada ou Erro de tipagem, ERRO:\n{erro}")
except:
    #Executa esse codigo caso um erro ocorra
    print(f"Um erro ocorreu")

else:
    # Executa esse codigo caso nenhum erro ocorra
    print(resultado)
finally:
    # Sempre será executadio
    print("Finalizando o programa obrigado")