import functools #Necessario importar biblioteca

def meu_decorador(funcao):
    @functools.wraps(funcao) #Faz com que a função não perca a capacidade de instrospecção
    def envelope(*args, **kwargs): 
        print('Faz algo antes de executar...')
        funcao(*args, **kwargs) 
        print('Faz algo depois de executar...')
    return envelope


@meu_decorador 
def ola_mundo(nome):
    print(f'Olá mundo de {nome}!')
    return None


print(ola_mundo.__name__)