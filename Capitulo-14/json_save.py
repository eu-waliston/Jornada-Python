from json import dumps, dump

cadastros = [
    {
        "Nome" : "João",
        "Idade" : "31",
        "Profissões" : ["Estagiário", "Dev Python", "Engenheiro de Software"]
    }, {
        "Nome": "Clara",
        "Idade": "35",
        "Profissões": ["Estagiária de Design", "Desenvolvedora Front-rnd"]
    }
]

result = dumps(cadastros, ensure_ascii=False, indent=True)

print(result)
# Exportando para um arquivo JSON
with open("dados.json", "w",  encoding="utf-8") as arquivo:
    dump(cadastros, arquivo, indent=4, ensure_ascii=False)
