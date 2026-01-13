def meu_gereador(numeros: list[int]):
    for num in numeros:
        yield num * 2 #utiliza-se 'yield' para retornar algo quando é gerador

for i in meu_gereador(numeros = [1, 2, 3]):
    print(i)