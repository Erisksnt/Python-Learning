def meu_decorador(funcao):
    def envelope(*args, **kwargs): #Acrescenta o Argumento para adicionar na função
        print('Faz algo antes de executar...')
        funcao(*args, **kwargs) #Acrescenta o Argumento para adicionar na função
        print('Faz algo depois de executar...')
    return envelope

#Ao utilizar @ estou dizendo para executar a função antes da função 'ola_mundo'
@meu_decorador #Esse nome é o nome que voce dará a função decoradora
def ola_mundo(nome):
    print(f'Olá mundo de {nome}!')
    return None

ola_mundo('Erick')