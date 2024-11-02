import string
import random

# print(string.ascii_letters)
# print(string.punctuation)
# print(string.digits)
# print(random.choices(string.ascii_letters))

tamanho_senha = int(input("Tamanho da Senha: "))
senha = []

for i in range(0, tamanho_senha):
    senha.append(random.choice(string.ascii_letters))
    senha.append(random.choice(string.digits))

print("".join(senha))
