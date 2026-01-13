#Desafio Dio

menu = """

    [1] Depositar
    [2] Saque
    [3] Extrato
    [4] Sair

"""

saldo = 0
limite = 500
limite_saque = 3
num_saques = 0
extrato = ""

while True:
    opcao = input(menu)

    if opcao == "1" :
        valor = float(input("Qual valor do deposito?: "))
        if valor > 0:
            saldo += valor
            extrato += f"Deposito: R$ {valor:.2f}\n"
           
        else:
            print("Valor invalido")

    elif opcao == "2":
        valor = float(input("Qual valor do saque?: "))

        if valor > limite:
                valor = print(input("O limite de para saque é 500, digite um valor valido: "))
        else:
            if num_saques >= limite_saque:
                    print("Voce excedeu a quatidade de saques permitida.")
            else:
                if valor <= 0 or valor > saldo:
                        valor = print(input("Digite um valor valido: "))
                        
                else:
                    saldo -= valor
                    num_saques += 1
                    extrato += f"Saque: R$ {valor:.2f}\n"

    elif opcao == "3":
         print(extrato)
         print(f"Seu saldo é de: R$ {saldo:.2f}")
    
    elif opcao == "4":
         print("Obrigado volte sempre!")
         break
    
    else:
         print("Digite uma opção valida")
