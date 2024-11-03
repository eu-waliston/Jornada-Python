from random import choice

class Desenvolvedor:
    def __init__(self, linguagem_programacao=None):
        self.linguagem_programacao = linguagem_programacao
        print(f"Novo DEV com expertise nas linguagens: \n\t{self.linguagem_programacao}")

    def desenvolver_codigo(self):
        print(f"Psssssiuu! Dev codando em {choice(self.linguagem_programacao)}!!!")

class Gerente:
    def __init__(self, softskills=None):
        self.softskills = softskills
        print(f'Novo Gerentre com habilidades nas Softskills: \n\t{self.softskills}')

    def gerenciar_equipe(self):
        print(f'Gerente esta utilizando {choice(self.softskills)} para gerenciar sua equipe!')

class TechLead(Desenvolvedor, Gerente):
    def __init__(self, linguagem_programacao=None, softskills=None):
        Desenvolvedor.__init__(self,linguagem_programacao)
        Gerente.__init__(self,softskills)

tech_lead = TechLead(['C', 'C#', 'Python'], ['Liderança', 'Comunicação Ativa', 'Feedbacks Positivos'])
print("!")
tech_lead.desenvolver_codigo()
tech_lead.gerenciar_equipe()