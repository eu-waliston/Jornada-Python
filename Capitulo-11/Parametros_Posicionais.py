def soma(max, *numeros):
    resultado = 0
    numeros_somados = []

    for numero in numeros:
        if(resultado + numero) > max:
            break

        resultado += numero
        numeros_somados.append(numero)

    return resultado, numeros_somados

resultado_soma,  numeros_somados = soma(100,2,5,10, 23,4,5,678,1234,67)
print(resultado_soma)
print(numeros_somados)
