def meu_decorador(funcao):
    def envelope():
        print('Faz algo antes de executar...')
        funcao()
        print('Faz algo depois de executar...')
    return envelope

def ola_mundo():
    print('Olá mundo!')
    return None

#Aqui estou dizendo que quero decorar a função 'ola_mundo'
#Neste caso solicitando para fazer algo antes de executalá e depois.
ola_mundo = meu_decorador(ola_mundo) 
ola_mundo()