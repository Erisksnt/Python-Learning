#Exemplo de utilização de tuplas (listas imutaveis)
frutas = ("laranja", "pera", "uva",)
letras = tuple("python")
numeros = tuple([1, 2, 3, 4])
pais = ("Brasil",)


matriz = [
(1, "a", 2),
("b", 3, 4),
(6, 5, "c"),
]

print(matriz[0]) # [1, "a", 2]​
print(matriz[0][0]) # 1​
print(matriz[0][-1]) # 2​
print(matriz[-1][-1]) # "c"​