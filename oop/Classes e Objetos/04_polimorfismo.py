#Trabalhando com Polimorfismo
#Polimorfismo é quando tem um obj e esse objeto pode se comportar de diferentes formas

class passaro:
    def voar(self):
        print("Voando....")

#Exemplo para "ganhar" herança do metodo voar
class pardal(passaro):
    def voar(self):
        super().voar()

#Exemplo para "ganhar" herança do metodo voar
class avestruz(passaro):
    def voar(self):
        print("Avestruz não voa")

def plan_voo(obj):
    obj.voar()

# FIXME: Exemplo RUIM para "ganhar" herança do metodo voar
class aviao(passaro):
    def voar(self):
        print("Avião decolando")

plan_voo(pardal())
plan_voo(avestruz())
plan_voo(aviao())






