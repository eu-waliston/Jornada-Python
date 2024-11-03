from random import randint


class Celular:

    def __init__(self, fabrincante, modelo, tela, aramzenamento, memoria,
                 camera, batria, tela_ligada):
        self.fabrincante = fabrincante
        self.modelo = modelo
        self.tela = tela
        self.aramzenamento = aramzenamento
        self.memoria = memoria
        self.camera = camera
        self.batria = batria
        self.tela_ligada = tela_ligada

    def ligar_tela(self):
        self.tela_ligada = True

    def verifica_carga_bateria(self):
        porcentagem = randint(1, 100)
        print(f"A bateria esta em {porcentagem}% e ainda tem {self.batria}mA")


celular_android = Celular("Samsnung", "S10",
                          6.25, 128, 4, 21,
                          3400, False)

print(celular_android.verifica_carga_bateria())
