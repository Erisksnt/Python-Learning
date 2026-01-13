class Cachorro:
    #__init__ constroi a classe, e sempre usado no inicio
    def __init__(self, nome, cor, acordado=True):
        print("Inicializando a classe ...")
        self.nome = nome
        self.cor = cor
        self.acordado = acordado

    def __del__(self):
        print("Removendo a instacia da classe...")

    def falar(self):
        print("Au au au")

    #__del__ remove o objeto e sempre utilizado ao final
def criar_cachorro():
    c = Cachorro("Dentinho","Caramelo", False)
    print(c.nome)

c = Cachorro("Rex","amarelo")
c.falar()

criar_cachorro()
