nome = input("Informe your name: ")
age = input("How old are u?: ")
job = input("What your profission: ")
language: input("What language do you use: ")

#forma antiga (old style)
print("nome: %s age: %s" % (nome, age))

#forma normal
print("nome: {} age: {}".format(nome, age))

#outra forma, nessa forma e boa que posso repetir mais vezes se precisar
print("nome: {1} age: {0}, {1} and {0}".format(nome, age))

#outra forma com dicionario
dados = {"nome": "guilherme", "age": 28}
print("nome: {nome} age: {age}".format(**dados))

#outra forma mais simples
print(f"nome: {nome} age: {age}")