#exemplo utilização do for
texto = input("Informe um texto: ")
vogais = "AEIOU"

for letra in texto:
    if letra.upper() in vogais:
        print(letra, end="")

print()# pular uma linha

#exemplo for + range
for numero in range(0,11):
    print(numero, end=" ")

print()# pular uma linha

#exemplo tabuada 
# (primeiro numero é o inicio do laço, o segundo é o ultimo numero do laço e o terceiro é a como a repetição se comportará)
for n in range(0,51,5):
    print(n, end=" ")

