# Exercicio 1

'''
temperatura = []
meses = ['Janeiro','Fevereiro','Março','Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
media = 0
acima_media_meses = []
acima_media_temperaturas = []

for i in range(len(meses)):
	temperatura.append(float(input('Informe a Temperatura media de ' + meses[i] + ':\n')))
	media += temperatura[i]
media = round(media/len(meses),2)

print('Média das temperaturas:' + str(media))
print('Meses com temperatura superior a média:')


for i in range(len(meses)):
	if(temperatura[i] > media):
		print(str(i) + '-' + meses[i] + ': ' + str(temperatura[i]))
'''

# Exercicio 2

'''
res = []
res.append(input("Telefonou para a vítima? 1/Sim ou 0/Não: "))
res.append(input("Esteve no local do crime? 1/Sim ou 0/Não: "))
res.append(input("Mora perto da vítima? 1/Sim ou 0/Não: "))
res.append(input("Devia para a vítima? 1/Sim ou 0/Não: "))
res.append(input("Já trabalhou com a vítima? 1/Sim ou 0/Não: "))

soma_respostas = 0

for i in res: # soma o número de respostas
	soma_respostas += int(i)

if (soma_respostas < 2):
 print("Inocente")
elif (soma_respostas == 2):
 print("Suspeita")
elif (3 <= soma_respostas <= 4):
 print("Cúmplice")
elif (soma_respostas == 5):
 print("Assassino")
'''

 # Exercicio 3

'''
valores = []
soma = 0
out_valores = ''

while(True):
	
	valor = float(input('Informe a valor: '))

	if valor == float(-1):
		break
	else:
		valores.append(valor)
		out_valores += str(valor) + ' '
		soma += valor

print('Quantidade de valores que foram lidos: {}'.format(len(valores)))

print('Valores que foram lidos: {}'.format(out_valores))

valores.reverse()
print('Valores que foram lidos na ordem inversa:')
for valor in valores:
	print(valor)

print('Soma dos valores: {}'.format(soma))

media = soma/len(valores)
print('Média dos valores: {}'.format(media))

print('Valores acima da média:')
acima_media = 0

for i in range(len(valores)):
	if valores[i] > media:
		print(valores[i])
		acima_media += 1


print('Quantidade de valores acima da média: {}'.format(acima_media))


print('Valores acima de 7:')
acima_sete = 0

for i in range(len(valores)):
	if valores[i] < 7:
		print(valores[i])
		acima_sete += 1


print('Quantidade de valores abaixo de sete: {}'.format(acima_sete))


print('FIM')
'''
