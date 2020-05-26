# Exercicio 3

notas = []
out_notas = ''

while(True):

	nota = float(input('Informe a nota: '))

	if nota == float(-1):
	
		break
	
	else:
		
		notas.append(nota)
		out_notas += str(nota) + ' '


print('Quantidade de notas lidas: {}'.format(len(notas)))

print('Notas que foram lidas: {}'.format(out_notas))

notas.reverse()
print('Notas que foram lidas na ordem inversa:')
for nota in notas:
	print(nota)

soma = 0
for nota in notas:
	soma += nota
print('Soma das notas {}'.format(soma))

media = soma/len(notas)
print('Média das notas {}'.format(media))


print('Valores acima da média: ')
acima_media = 0

for i in range(len(notas)):
	
	if notas[i] > media:
		print(notas[i])
		acima_media += 1

print('Quantidade de notas acima da média {}'.format(acima_media))


print('Valores abaixo de sete: ')
abaixo_sete = 0

for i in range(len(notas)):
	
	if notas[i] < 7:
		print(notas[i])
		abaixo_sete += 1

print('Quantidade de notas abaixo da sete {}'.format(abaixo_sete))

print('FIM')
