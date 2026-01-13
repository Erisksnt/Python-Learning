#Aula sobre conjuntos

conjunto_a = {1, 2, 3, 4}
conjunto_b = {1, 4, 5, 6}
conjunto_c = {9, 7, 0, 1}

#une os conjuntos a e b
conjunto_a.union(conjunto_b)

#pega os pontos em comum entre cojunto a e b
conjunto_a.intersection(conjunto_b)

#pega os pontos diferentes entre os conjuntos a e b
conjunto_a.difference(conjunto_b)

#pega os pontos que simetricos (une os dois pontos diferentes)
conjunto_a.symmetric_difference(conjunto_b)

#verifica se os elementos de um conjunto estão dentro outro conjunto, o retorno é "verdadeiro" ou "falso"
conjunto_a.issubset(conjunto_b)

#verifica se os elementos de um conjunto NÃO estão dentro outro conjunto, o retorno é "verdadeiro" ou "falso"
conjunto_a.issuperset(conjunto_b)

#Verifica se há ou não interseção entre os conjuntos, o retorno é "verdadeiro" ou "falso"
conjunto_a.isdisjoint(conjunto_c)

# o .add adiciona algum elemento dentro do conjunto, caso ele ja não esteja
conjunto_a.add(9) #se não houver 9 dentro do conjunto_a, será adicionado

#Gera uma copia do conjunto
conjunto_a.copy()

#Limpa o conjunto
conjunto_a.clear()

#Discarta um valor do conjunto
conjunto_a.discard(1)

#Remove elemetos do conjunto (em ordem)
conjunto_a.pop(3)

#Remove elemetos do conjunto (posso informar a posição que eu quero que seja removida)
conjunto_a.remove(0)

# O IN verifica se o numero informado esta dentro do conjunto (retorno de verdadeiro ou falso)
1 in conjunto_a