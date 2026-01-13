#precisa declara uma classe.
#para isso usa-se comand "class" e o nome da classe

class Bicicleta:
    def __init__(self,cor,modelo,ano,valor): #Command que será estudado no futuro
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor

    #NÃO ESQUECER O "Self"  
    def buzinar(self):
        print("Plim plim...")

    def parar(self):
        print("Parando a bicicleta...")
        print("Bicicleta Parada!")

    def correr(self):
        print("Vrummm...")
    
    def color(self):
        return self.cor
    
    #representação mais legivel, retorna valores dentro da classe (porem voce passa valor por valor)
    def __str__(self):
        return f"Bicicleta: {self.cor}, {self.modelo}, {self.ano}, {self.valor}"

    #outra forma chamar as caracteristica da bike porem ele ja puxa direto todas as caracteristicas
    def __str__(self):
        return f"{self.__class__.__name__}: {[f'{chave}={valor}' for chave, valor in self. __dict__.items()]}"
    
    def marcha(nmro_marcha):
        print("Marcha trocada...")

bike_1 = Bicicleta("vermelha","caloi", 2025, 600) #caracteristica da bicicleta (atributos da classe)
bike_1.buzinar() #forma de chamar a função buzinhar
bike_1.correr()
bike_1.parar()
print(bike_1.cor,bike_1.modelo,bike_1.ano,bike_1.valor)

bike_2 = Bicicleta("Verde", "Monark", 2000, 190)
Bicicleta.buzinar(bike_2) #outra forma de chamar a função buzinar
print(bike_2.color()) #forma de chamar função color

print(bike_1)