#controle de validade do estoque

import csv
import datetime

def lista_produtos():

	with open(nome_criar_final, "w", newline='') as csv_out:
		csv_writer = csv.writer(csv_out)

		for i in range(len(lista)):

			lista_aux = list()
			lista_aux.append(lista[i])

			csv_writer.writerow(lista_aux)

def criar():

	while (True):

		d['Produto'] = str(input('Produto: '))

		print('Para a validade: ')
		dia = int(input('Digite o dia: '))
		mes = int(input('Digite o mes: '))
		ano = int(input('Digite o ano: '))
		data= datetime.date(ano, mes, dia)
		data_2 = data.strftime('%d/%m/%Y')
		
		d['Validade'] = data_2

		lista.append(d.copy())

		while(True):
			resp = str(input('Continue? [S/N]'))
			if resp in 'SN':
				break
			print('ERRO, digite S ou N')
		if resp == 'N':
			break

	lista_produtos()

def abrir():

	nome_abrir = input('Digite o nome do arquivo: ')
	nome_abrir_final = nome_abrir+'.txt'

	try:
		with open(nome_abrir_final) as csv_abrindo:
			csv_reader = csv.reader(csv_abrindo)

			for linha in csv_reader:
				print(linha)

	except:
		print('NOME INVALIDO')

if __name__ == "__main__":

	lista = []
	d = {}

	print('1 - Criar estoque')
	print('2 - Abrir estoque')
	comando = input('Digite o numero do comando: ')

	if comando == str(1):
		nome_criar = input('Digite o nome do arquivo: ')
		nome_criar_final = nome_criar+'.txt'
		criar()

	elif comando == str(2):
		abrir()
		
	else:
		print('COMANDO INVALIDO')