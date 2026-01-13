class veiculo:
    def __init__(self, cor, placa, numero_rodas):
        self.cor = cor
        self.placa = placa
        self.numero_rodas = numero_rodas

    def ligar_motor(self):
        print("Ligando motor...")

    def __str__(self):
        return self.cor
#Herdando caracteristica da classe "veiculo"
class motocicleta(veiculo):
    pass
class carro(veiculo):
    pass

#Herdando caracteristica da classe "veiculo" porem tendo extensões especifica
class caminhao(veiculo):
    def __init__(self, cor, placa, numero_rodas, carregado):
        
        super().__init__(cor, placa, numero_rodas) #command "super" faz com que continue a receber caracterista da classe pai
        self.carregado = carregado

    def esta_carregado(self):
        print(f"{'SIM' if self.carregado else 'NAO'} estou carregado")

moto = motocicleta("amarelo","123-abc",2)
print(moto)
moto.ligar_motor()

carro = carro("vermelho","dmp-2010", 4)
carro.ligar_motor()


caminhao = caminhao("preto", "xxx-1023", 8, True)
caminhao.ligar_motor()
caminhao.esta_carregado()
print(caminhao)