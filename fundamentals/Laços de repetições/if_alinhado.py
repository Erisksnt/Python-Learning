conta_normal = True
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