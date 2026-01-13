#Trabalhando com Variaveis de objetos
class estudante:
    escola ="DIO"

    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula

    def __str__(self):
        return f"{self.nome} - {self.matricula} - {self.escola}"
    
def mostrar_valores(*objs):
    for obj in objs:
        print(obj)

aluno_1 = estudante("Erick",1)
aluno_2 = estudante("Brunno", 2)
mostrar_valores(aluno_1,aluno_2)

estudante.escola = "Phyton"
aluno_3 = estudante("Guilherme", 3)
mostrar_valores(aluno_1, aluno_2, aluno_3)
