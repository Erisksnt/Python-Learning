#Trabalhando com timedelta que serve para estimar um tempo de acordo a
from datetime import datetime, timedelta
carros = str(input("Qual tamanho do carro que acabou de entrar:"))

#estimativa de tempo de acordo com tempo do carro
tempo_pequeno = 50
tempo_medio = 60
tempo_grande = 120
hora_atual = datetime.today()

if carros == "P":
    data_estimada = hora_atual + timedelta(minutes=tempo_pequeno)
    print(f"O carro chegou: {hora_atual} e ficará pronto às {data_estimada}")

elif carros == "M":
     data_estimada = hora_atual + timedelta(minutes=tempo_pequeno)
     print(f"O carro chegou: {hora_atual} e ficará pronto às {data_estimada}")
elif carros == "G":
    data_estimada = hora_atual + timedelta(minutes=tempo_pequeno)
    print(f"O carro chegou: {hora_atual} e ficará pronto às {data_estimada}")