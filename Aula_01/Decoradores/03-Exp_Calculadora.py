def calculadora(operacao):
    def soma(a, b):
        return a + b
    def sub(a, b):
        return a - b
    def mult(a, b):
        return a * b
    def div(a, b):
        return a / b
    
    match operacao:
        case '+':
            return soma #Retornando função interna 'soma'
        case '-':
            return sub #Retornando função interna 'sub'
        case '*':
            return mult #Retornando função interna 'mult'
        case '/':
            return div #Retornando função interna 'div'

#Exemplo passando os valores que serão calculados
op = calculadora("+")
print(op(2,2))
op = calculadora("-")
print(op(2,2))
op = calculadora("*")
print(op(2,2))
op = calculadora("/")
print(op(2,2))

#Exemplo com input (para calculadora baisca, operações apenas com numeros inteiros)
entrada = input("Digite o cálculo: ").split()
if len(entrada) != 3:
    print("Formato invalido. Use no 'NUMERO' 'OPERAÇÃO' 'NUMERO'")
else:
    a, operacao, b = float(entrada[0]), entrada[1], float(entrada[2])
    funcao = calculadora(operacao)
    print(f"O resultado do cálculo é: {funcao(a, b):.2f}")

