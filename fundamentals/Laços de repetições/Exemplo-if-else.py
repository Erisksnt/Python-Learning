maior_idade=18
idoso = 60
idade = int(input("Informe sua idade: "))

#if = condição se verdadeira
if idade >= idoso:
    print ("Inss ta chamado")
    
#elif = mais uma condição para verificar se é verdadeira
elif idade >= maior_idade:
    print ("adulto")

#else = após if/elif se condição for falsa
else:
    print ("menor de idade")
#//////////////////////////////////////////////////////////////////////#

conta_normal = False
conta_universitaria = False

saldo = 2000
saque = 2450
cheque_especial = 450

if conta_normal:
    if saldo >= saque:
        print("saque realiado")
    elif saque <= (saldo + cheque_especial):
        print("saque feito usando cheque")
    else:
        print("saldo insuficiente mesmo com cheque")
elif conta_universitaria:
    if saldo >= saque:
        print("saque realizado com sucesso")
    else:
        print("saldo insuficiente")
else:
    print("conta nao encontrada")
