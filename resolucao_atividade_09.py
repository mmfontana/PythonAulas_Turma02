# Resolucao atividade 9

from datetime import date
from dateutil.relativedelta import relativedelta, SA

# Funcao para encontrar segundo sabado dos meses de um determinado ano
def segundo_sabado_mes(ano):
	# Lista para as datas dos segundos sabados dos meses de um determinado ano
	segundo_sabados = []
	# For loop para o meses
	for mes in range(1,13):
		# Criando o primeiro dia do mes
		dia = date(ano, mes, 1)
		# Utilizando .relativedelta para procurar segundo sabado do determinado mes
		segundo_sabado = (dia + relativedelta(day=1, weekday=SA(2)))
		segundo_sabados.append(segundo_sabado)
	return segundo_sabados

if __name__ == '__main__':
	segundo_sabados = segundo_sabado_mes(2020)
	print(segundo_sabados)