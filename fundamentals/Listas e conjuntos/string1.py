nome = "ericK"
texto =" hellow mundo  "
menu = "phynton"

#printa com td maiusculo
print(nome.upper())

#printa com td minusculo
print(nome.lower())

#printa com a primeira letra maiuscula
print(nome.title())

#printa sem os espaço em branco na frente e atras
print(texto.strip())

#printa sem os espaço em branco da esquerda
print(texto.lstrip())

#printa sem os espaço em branco da direita
print(texto.rstrip())

#printa com frufru
print("###" + menu + "###")

#printa centraliza porem preciso saber quantos caracteres tem
print(menu.center(14))

#printa centraliza não preciso saber quantos caracteres tem
print(menu.center(13,"#"))

#printa separadinho por traço
print("-".join(menu))