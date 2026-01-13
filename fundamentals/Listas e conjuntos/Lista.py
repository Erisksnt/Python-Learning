#para usar vc primeira declara os itens da lista e dps para chamar basta colocar o nome declarado seguido de "[]".

#Exemplos de listas

frutas = ["maçã", "laranja", "uva", "pera"]
print(frutas[0])  # maçã
print(frutas[2])  # uva


letras = list("python")
# numeros = list(range(10))
# carro = ["Ferrari", "F8", 4200000, 2020, 2900, "São Paulo", True]
lista = ["p", "y", "t", "h", "o", "n"]

print(lista[2:])     # ['t', 'h', 'o', 'n']
print(lista[:2])     # ['p', 'y']
print(lista[1:3])    # ['y', 't']
print(lista[0:3:2])  # ['p', 't']
print(lista[::])     # ['p', 'y', 't', 'h', 'o', 'n']
print(lista[::-1])   # ['n', 'o', 'h', 't', 'y', 'p']

#EXEMPLO DE MATRIZ 
matriz = [
[1, "a", 2],
["b", 3, 4],
[6, 5, "c"]
]

print(matriz[0]) # [1, "a", 2]​
print(matriz[0][0]) # 1​
print(matriz[0][-1]) # 2​
print(matriz[-1][-1]) # "c"​

#Exemplo utilizando o FOR 
carros = ["gol", "celta", "palio"]

for carro in carros:
    print(carro)

for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")

#Utilizando o append 
numeros = [1, 30, 21, 2, 9, 65, 34]
pares = []

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)
print(pares)

#Outro exemplo de utilização do append
numeros = [1, 30, 21, 2, 9, 65, 34]
quadrado = []

for numero in numeros:
    quadrado.append(numero ** 2)
print(quadrado)
