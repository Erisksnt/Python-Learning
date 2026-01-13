#Conceito de contrato (conceito de interface)
from abc import ABC, abstractmethod

#Classes abstratas não podem ser instanciadas
#Aqui você está definindo uma interface, ou seja, um "contrato" que obriga as subclasses a implementarem o método
class ControleRemoto(ABC):
    @abstractmethod
    def ligar(self):
        pass

    @abstractmethod #Quando eu indico
    def desligar(self):
        pass

    @property #Se eu adiciono uma função como property, mesmo sendo abstratada
    @abstractmethod #eu obrigatoriamente tenho que indicar como property nas instancias seguintes
    def marca(self):
        pass

#Apos utilizar o metodo abstrato, sou obrigado a instanciar os metodos
#nas classes referenciadas
class ControleTV(ControleRemoto):
    def ligar(self): 
        print("ligar TV")
        print("Tv ligada!")

    def desligar(self): 
        print("Desligando TV")
        print("Tv desligada!")

    @property
    def marca(self):
        return "LG"

class ControleArCondicionado(ControleRemoto):
    def ligar(self): 
        print("ligar AR")
        print("AR ligada!")

    def desligar(self): 
        print("Desligando AR")
        print("AR desligada!")

    @property
    def marca(self):
        return "Samsung"


controle = ControleTV()
controle.ligar()
controle.desligar()
print(controle.marca)

controle = ControleArCondicionado()
controle.ligar()

print(controle.marca)


