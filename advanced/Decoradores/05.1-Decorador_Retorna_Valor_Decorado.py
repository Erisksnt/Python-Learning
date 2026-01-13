def meu_decorador(funcao):
    def envelope(*args, **kwargs):
        print('Faz algo antes de executar...')
        resultado = funcao(*args, **kwargs)
        print('Faz algo depois de executar...')
        return resultado
    return envelope

#Ao utilizar @ estou dizendo para executar a função antes da função 'ola_mundo'
@meu_decorador #Esse nome é o nome que voce dará a função decoradora
def ola_mundo(nome):
    print(f'Olá mundo de {nome}!')
    return nome.upper()

resultado = ola_mundo('Erick')
print(resultado) #DEVE RETORNAR 'NOME.UPPER'