#exemplo while
opcao = -1

while opcao != 3:
    opcao =int(input("[1] Sacar \n[2] Extrato, \n[3] Sair\n"))

    if opcao == 1:
        print("sacando")
    elif opcao == 2:
        print("Saindo extrato...")

print()

#exemplo while break
while True: 
    opcao =int(input("Informe um numero: "))

    if opcao == 10:
        break
  
print()
