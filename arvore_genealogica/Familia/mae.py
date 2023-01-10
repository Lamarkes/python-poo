from arvore_genealogica.PessoaModel.pessoa import Pessoa


class Mae(Pessoa):

    def __init__(self):
        super().__init__()
        self.nome = "Neusa"
        self.idade = 29
        self.cor_dos_cabelos = "castanhos"
        self.tipo_de_sangue = "O-"
        self.carteira_de_trabalho = True

    def cozinhar(self):
        print("Sabe cozinhar")

    def correr(self):
        print("Pode sair correndo")


    def __str__(self):
        return f"<Nome: {self.name}," \
               f" Idade: {self.idade}," \

