class animal:
    def __init__(self, nro_patas):
        self.nro_patas = nro_patas

    #Utilizado para percorrer todos os items da def main
    def __str__(self):
        return f"{self.__class__.__name__}: {[f'{chave}={valor}' for chave, valor in self. __dict__.items()]}"

class mamifero(animal):
    def __init__(self, cor_pelo, **kw): #**kwargs é um parâmetro especial usado em funções para capturar argumentos nomeados
        self.cor_pelo = cor_pelo
        super().__init__(**kw) #herda coisa da classe pai
        
class ave(animal):
    def __init__(self, cor_bico, **kw):
        self.cor_bico = cor_bico
        super().__init__(**kw) #herda coisa da classe pai
        
class gato(mamifero):
    pass

class onitorrinco(mamifero,ave):   
    pass

gato = gato(nro_patas = 4, cor_pelo="Preto")
print(gato)

onitorrinco = onitorrinco(nro_patas = 2, cor_pelo="Marrom",cor_bico ="Laranja")
print(onitorrinco)