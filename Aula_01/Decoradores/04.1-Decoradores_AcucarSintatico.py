def meu_decorador(funcao):
    def envelope():
        print('Faz algo antes de executar...')
        funcao()
        print('Faz algo depois de executar...')
    return envelope

#Ao utilizar @ estou dizendo para executar a função antes da função 'ola_mundo'
@meu_decorador #Esse nome é o nome que voce dará a função decoradora
def ola_mundo():
    print('Olá mundo!')
    return None

ola_mundo()