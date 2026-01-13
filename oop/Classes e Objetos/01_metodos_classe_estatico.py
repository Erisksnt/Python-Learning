class pessoa:
    def __init__(self, nome=None, idade=None):
        self.nome = nome
        self.idade = idade

    #Preciso ter acesso ao contexto da classe? se sim utiluzo metodo da classe
    #Transforma em metodo de class ("cls" é referencia para classe)
    @classmethod
    def criar_de_data_nasc(cls, ano, mes, dia, nome):
        idade = 2025 - ano
        return cls(nome, idade)

    #Preciso ter acesso ao contexto da classe? se não utiluzo metodo estatico
    #Transforma em metodo estatico
    @staticmethod
    def maior_idade(idade):
        return idade >= 18
    
p = pessoa("Erick",23)
print(p.nome,p.idade)

p2 = pessoa.criar_de_data_nasc(2002,2,7,"Erick")
print(p2.nome, p2.idade)

print(pessoa.maior_idade(18))
print(pessoa.maior_idade(8))
