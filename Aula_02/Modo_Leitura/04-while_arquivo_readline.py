#Estrutura para achar o caminho do arquivo é (r"caminho_do_arquivo", "r")
#Esse "r" no começo da estrutura diz para o phyton "Não interprete barras invertidas como comandos especiais".

arquivo = open(
    r"C:\Users\Erick\OneDrive\Documentos\Bootcamp_Santander\Aula_02\lorem.txt", "r"
)
while len(line := arquivo.readline()):  #Exemplo utilizando While (Tras o arquivo todo)
    print(line)
arquivo.close() 