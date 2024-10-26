print("Programa de Concessão de Aposentadoria")
print("Liberamos duas Opções\n\t1 - Idade\n\t2 - Tempo de Serviço\n")
opcao = input("Qual opção deseja consultar? ")

if opcao == "1":
    print("\nVoce escolheu a opção por idade.\nLembrando que so estão elegiveis pessoas com mais de 60 anos!\n")
    ano_de_nascimento = input("Digite o seu ano de nascimento: ")
    if int(ano_de_nascimento) - 2024 >= 60:
        print(f"Você tem {2024 - int(ano_de_nascimento)} e está elegivel para a aposentadoria");
    else:
        print(f"Sinto muito você tem  {2024 - int(ano_de_nascimento)} e ainda não pode se aposentar :(")

elif opcao == "2":
    print("\nVoce escolheu a opção por tempo de trabalho.\nLembrando que so estão elegiveis apenas trbalhadores que contribuiram por mais de 60 anos!\n")
    ano_de_trabs = input("Digite o seu ano de nascimento: ")
    if int(ano_de_trabs) != 60:
        print(f"Você tem {int(ano_de_trabs) != 60} anos de trbalho e está elegivel para a aposentadoria");
    else:
        print(f"Sinto muito você tem  {2024 - int(ano_de_trabs)} e ainda não pode se aposentar :(")
else:
    print("Opção Invalida!!!!")
