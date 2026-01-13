#Desafio Dio 4 - Utiliando Classes
from datetime import datetime, date, time
from abc import ABC, abstractmethod

class Transacao(ABC):
     def __init__(self, valor, data_hora):
          self.valor = valor
          self.data_hora = data_hora

     @abstractmethod
     def registrar(self, conta: 'Conta'):
          pass
     
class Deposito(Transacao):
     def __init__(self, valor):
          if valor <= 0:
               raise ValueError("Erro, operação não pode ser concluida")
          self._valor = valor
          self.data_hora = data_hora_atual.strftime(mascara_hora)
                         
     @property
     def valor(self):
         return self._valor

     def registrar(self, conta):
          conta.depositar(self._valor)
          
class Saque(Transacao):
     def __init__(self, valor):
          if valor <= 0:
               raise ValueError("Erro, operação não pode ser concluida")
          self._valor = valor
          self.data_hora = data_hora_atual.strftime(mascara_hora)
                         
     @property
     def valor(self):
         return self._valor

     def registrar(self, conta):
          conta.sacar(self._valor)
     
class Historico:
     def __init__(self, transacao=None):
          self._transacao = []
          if transacao is not None:
            self._transacao.append(transacao)
            self.data_hora = data_hora_atual.strftime(mascara_hora)

     @property    
     def extrato(self):
          return self._transacao.copy()

     def adicionar_transacao(self,transacao=None):
          if transacao is not None:
            self._transacao.append(transacao)                     

class Conta:
     def __init__(self, numero, agencia, cliente,saldo: float = 0.0):
          self.saldo = saldo
          self.numero = numero
          self.agencia = agencia
          self.cliente = cliente
          self.historico = Historico()
     
     def depositar(self,valor):
          if valor > 0:
               self.historico.adicionar_transacao(Deposito(valor))
               self.saldo += valor
               return True
          else:
               return False

     def sacar(self, valor):
          if valor <= 0 or valor > self.saldo:
               return False
          self.historico.adicionar_transacao(Saque(valor))
          self.saldo -= valor
          return True

class ContaCorrente(Conta):
     def __init__(self, numero, agencia, cliente, saldo, limite=500, limite_saques=10):
          super().__init__(numero, agencia, cliente, saldo)
          self.limite = limite
          self.limite_saques = limite_saques

     def sacar(self, valor):
          if self.limite_saques <= 0:
               return False
          
          if valor > self.limite: 
               return False
          
          if super().sacar(valor):
               self.limite -= valor
               self.limite_saques -= 1
               return True
          return False

     def depositar(self, valor):
          return super().depositar(valor)

class Cliente:
     def __init__(self, nome, cpf, data_nasc, endereco):
          self.nome = nome
          self.cpf = cpf
          self.data_nasc = data_nasc
          self.endereco = endereco
          self.lista_conta = []
     
     def adicionar_conta(self,conta):
          self.lista_conta.append(conta)

     def realizar_transacao(self, conta, transacao):
          transacao.registrar(conta)

class PessoaFisica(Cliente):
     def __init__(self, nome, cpf, data_nasc, endereco):
          super().__init__(nome, cpf, data_nasc, endereco)   

menu = """
╔====================== Bem vindo ao Erisk Bank ====================╗
║============== Onde seu dinheiro trabalha por você ================║
║                         [1] Depositar                             ║ 
║                         [2] Saque                                 ║
║                         [3] Extrato                               ║
║                         [4] Criar Usuario                         ║
║                         [5] Criar Nova conta                      ║
║                         [6] Sair                                  ║
╚===================================================================╝
"""
data_hora_atual = datetime.today()
data_atual = datetime.today()
mascara_hora = "%H:%M - %d/%m/%Y"
mascara_dia = "%d/%m/%Y - %H:%M"
usuario_logado = None
conta = None

#Cadastro de usuario
usuarios = []
def criar_usuario(usuarios):
    cpf = input("Informe o CPF(Somente numeros):")
    usuario = filtrar_usuarios(cpf, usuarios)

    if usuario:
        print("Já existe usuario vinculado a esse CPF")
        return
    
    nome = input("Informe seu nome completo: ")
    data_nasc = input("Informe sua data de nascimento: ")
    endereco = input("Informe seu endereço: ")

    novo_cliente = PessoaFisica(nome, cpf, data_nasc, endereco)
    usuarios.append(novo_cliente)
    print("Usuario Cadastrado com sucesso!")

def filtrar_usuarios(cpf, usuarios):
     return next((usuario for usuario in usuarios if usuario.cpf == cpf), None)

#Criar conta Corrente
contas_corrente = []

def criar_conta(usuarios, contas_corrente):
     cpf = input("Informe o CPF(Somente numeros):")
     usuario = filtrar_usuarios(cpf, usuarios)

     if not usuario:
        print("Usuário não encontrado! Cadastre primeiro o usuário.")
        return
     
     agencia = "0001"
     numero_conta_corrente = len(contas_corrente) + 1
     nova_conta_corrente = ContaCorrente(numero=numero_conta_corrente, agencia=agencia, cliente=usuario,saldo=0)
     contas_corrente.append(nova_conta_corrente)
     usuario.adicionar_conta(nova_conta_corrente)
     print(f"Conta criada com sucesso para o usuario {usuario.nome}!\nAgencia: {agencia}\nConta: {numero_conta_corrente}")

def filtrar_usuarios(cpf, usuarios):
     return next((usuario for usuario in usuarios if usuario.cpf == cpf), None)

while True:
     opcao = input(menu)
     #Deposito
     if opcao == "1" :
          cpf = input("Informe o CPF(Somente numeros):")
          usuario = filtrar_usuarios(cpf, usuarios)
          
          if not usuario:
             print("Usuário não encontrado! Cadastre primeiro o usuário.")
             continue
          
          if not usuario.lista_conta:
             print("Conta não encontrada") 
             continue
          
          else:
               conta =  usuario.lista_conta[0]
               valor = float(input("Qual valor do deposito?: "))
               if valor > 0:
                   deposito = Deposito(valor)
                   usuario.realizar_transacao(conta, deposito)
                   print("Deposito efetuado com sucesso!", data_hora_atual.strftime(mascara_hora))
                   print(f"Seu saldo é de: R$ {conta.saldo:.2f}")
               else:
                   print("Valor invalido")
     #Saque
     elif opcao == "2":
          cpf = input("Informe o CPF(Somente numeros):")
          usuario = filtrar_usuarios(cpf, usuarios)
    
          if not usuario:
             print("Usuário não encontrado! Cadastre primeiro o usuário.")
             continue
          
          if not usuario.lista_conta:
             print("Conta não encontrada") 
             continue
          else:
               conta =  usuario.lista_conta[0]
               valor = float(input("Qual valor do saque?: "))
               if valor <= conta.saldo:
                   saque = Saque(valor)
                   usuario.realizar_transacao(conta, saque)
                   print("Saque efetuado com sucesso!", data_hora_atual.strftime(mascara_hora))
                   print(f"Seu saldo é de: R$ {conta.saldo:.2f}")
               else:
                   print("Valor invalido")
     #Extrato
     elif opcao == "3":
          print("\n=========================Extrato============================\n")
          if not conta:
               print("Conta não encontrada. Faça login ou cria primeiro uma conta.")
               continue

          if not conta.historico.extrato:
              print("Nenhuma movimentação realizada.")
          else:
              for transacao in conta.historico.extrato:
                  tipo = type(transacao).__name__
                  print(f"{tipo} de R$ {transacao.valor:.2f} às {transacao.data_hora}")

          print(f"\nSeu saldo é de: R$ {conta.saldo:.2f}")
          print(f"Extrato referente ao dia {data_atual.strftime(mascara_dia)}\n")
          print("============================================================")
 
     #Chamar a função criar_usuario
     elif opcao == "4":
          criar_usuario(usuarios)
          continue
     
     #Chamar a função criar_conta
     elif opcao == "5":
          criar_conta(usuarios, contas_corrente)
          continue
     
     #Sair do laço
     elif opcao == "6":
         print("Obrigado volte sempre!")
         break
     else:
         print("Digite uma opção valida")
