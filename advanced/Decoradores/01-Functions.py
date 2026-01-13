def mensagem(nome):
    print('execeutando nome')
    return f'Oi {nome}'

def mensagem_longa(nome):
    print('Executando mensagem longa')
    return f'Ola {nome}, tudo bem com voce?'

def executar(funcao, nome):
    print('Executando "executar"')
    return funcao(nome)

nome = input("Digite seu nome:")
print(executar(mensagem, nome))
print(executar(mensagem_longa, nome))
