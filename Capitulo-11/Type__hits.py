def aplica_baskhara(a: float,b: float,c: float) -> (float,float):
    delta = b ** 2 - 4 * a * c
    x_1 =   (-b * (delta ** 1/2) / (2 *a))
    x_2 =   (-b - (delta ** 1/2) / (2 *a))

    return x_1, x_2

def aplica_desconto(produto: dict, desconto: float) -> dict[str: str]:
    resultado = {}

    for nome_produto, valor in produto.items():
        resultado[nome_produto] = f'{valor * (1 - desconto):.2f}'
    return resultado
valores_produtos = {
    'microonda' : 499.99,
    'computador' : 5999.99,
    'forno' : 399.99
}

# print(aplica_desconto(valores_produtos, 0.15))
# print(aplica_baskhara(5.0, 15.0, 25.0))

x: list = "1,2,3".split(',')
print(x)
