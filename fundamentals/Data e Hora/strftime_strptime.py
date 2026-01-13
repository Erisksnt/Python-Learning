from datetime import datetime

data_hora_atual = datetime.today()
data_hora_str = "2025-05-05 21:50"
mascara_hora = "%H:%M %d-%m-%Y" #%d retorna o dia, %m retorna o mes, %Y retorna o ano, %a retorna o dia da semana      

print(data_hora_atual.strftime(mascara_hora))

#data_convertida = datetime.strptime(data_hora_str, mascara_hora)
#print(data_convertida)