#conceito de encapsulamento:
#deve usar-se "_" em atributos que devem ser privados como boa pratica

class conta:
    def __init__(self,nro_agencia,saldo=0):
        self._saldo = saldo
        self.nro_agencia = nro_agencia

    def depositar(self, valor):
        #... (isso apenas simula como se houvesse mais codigo aqui)
        self._saldo += valor
    
    def sacar(self, valor):
        #...
        self._saldo -= valor

    def mostrar_saldo(self):
        #...
        return self._saldo

conta = conta("0001", 200)
conta.depositar(100)

#acesso a recursos publicos
print(conta.nro_agencia)

#acesso a recursos privados, deve se criar uma def para isso
print(conta.mostrar_saldo())