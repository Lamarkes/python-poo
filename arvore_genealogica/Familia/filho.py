from pai import Pai
from mae import Mae


class CriancaMixin(Pai, Mae):
    def __init__(self, cpf):
        super().__init__()
        self.nome = ""
        self.idade = ""
        self.cpf = cpf

        del self.carteira_motorista
        del self.carteira_de_trabalho

    @property
    def nome(self):
        return self._nome
    @nome.setter
    def nome(self, nome_crianca):
        self._nome = nome_crianca

    def __str__(self):
        return f"Filho = Nome= {self._nome},CPF={self.cpf}, cor dos olhos= {self.cor_dos_olhos}, cor dos cabelos= {self.cor_dos_cabelos} "


filho = CriancaMixin("0000011111")

filho.nome = "Lamark"
print(filho)

filho.comer()
