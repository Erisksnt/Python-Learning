class MeuIterador:
    def __init__(self, numeros: list[int]):
        self.numeros = numeros
        self.contador = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        try:
            numero = self.numeros[self.contador]
            self.contador += 1
            return numero * 2
        except IndexError: #Significa que quando encontrar um 'IndexError, o programa parará o loop
            raise StopIteration #Finaliza o fluxo

#Necessario usar o 'For' para iterar o item dentro de um arquivo grande por exemplo
for i in MeuIterador(numeros=[1,2,3]):
    print(i)