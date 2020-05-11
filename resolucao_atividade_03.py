# Exercicio 1 

'''
print('Lojas Quase Dois - Tabela de Preços')

for quantidade in range(1,51):

	resultado = quantidade * 1.99

	print('{} - R$ {:0.2F}'.format(quantidade, resultado))

'''

# Exercicio 2 

'''
while(True):

	preco_produto = -999
	quantidade_produto = 1
	valor_total = 0 

	print('Loja Tabajara')
	
	while(preco_produto != 0):

		preco_produto = float(input(('Produto {}: R$ '.format(quantidade_produto))))

		quantidade_produto += 1

		valor_total += round(preco_produto, 2)

	print('Total: R$ {}'.format(valor_total))
	valor_recebido = float(input('Dinheiro: R$: '))
	print('Troco: R$ {}'.format(valor_recebido-valor_total))
'''


# Exercicio 3


'''
quantidade_temperatura = 1
soma_temperatura = 0


print('Temperaturas - Metereologia')

temperatura_in = float(input('Temperatura {}:'.format(quantidade_temperatura)))
temperatura_max = temperatura_in
temperatura_min = temperatura_in



while(True):

	temperatura_in = float(input('Temperatura {}:'.format(quantidade_temperatura)))

	if temperatura_in != -999:

		if temperatura_in > temperatura_max:
			temperatura_max = temperatura_in

		if temperatura_in < temperatura_min:
			temperatura_min = temperatura_in

		# Media
		soma_temperatura += temperatura_in
		quantidade_temperatura += 1

	else:

		temperatura_media = (soma_temperatura/quantidade_temperatura)

		print('Máximo {}'.format(temperatura_max))
		print('Minimo {}'.format(temperatura_min))
		print('Media {}'.format(temperatura_media))
'''