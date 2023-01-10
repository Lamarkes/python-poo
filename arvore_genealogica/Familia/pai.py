from arvore_genealogica.PessoaModel.pessoa import Pessoa


class Pai(Pessoa):

    def __init__(self):
        super().__init__()
        self.nome = "Joao"
        self.idade = 28
        self.tipo_de_sangue = "A+"
        self.cor_dos_olhos = "Verde_agua"
        self.carteira_motorista = "9821213231"

    def sentar(self):
        print("Esta sentando")

    def jogar_bola(self):
        print("Gosta de jogar bola")

    def __str__(self):
        return f"<Nome: {self.name}," \
               f" Idade: {self.idade},"
