# Resolucao atividade 05
'''
#1)
nome_aluno = ''
situacao = ''
media_aluno = 0

dict_situacao = dict()

if media_aluno <= 3:
	situacao = 'Reprovado'
elif 3 < media_aluno < 7:
	situacao = 'Recuperação'
else:
	situacao = 'Aprovado'

dict_situacao['Nome'] = nome_aluno
dict_situacao['Media'] = media_aluno
dict_situacao['Situacao'] = situacao
'''

#2) 

out_lista = []
contador = 0
soma_idade = 0

while(True):

	nome = input('Nome: ')
	sexo = input('Sexo: ')
	idade = int(input('Idade: '))

	pessoa_dict = dict()

	pessoa_dict['Nome'] = nome
	pessoa_dict['Sexo'] = sexo.lower()
	pessoa_dict['Idade'] = idade

	out_lista.append(pessoa_dict)

	contador += 1
	soma_idade += idade

	continuar = input('Continuar? (Y/N): ')
	if continuar == 'N' :
		break

media_idade = (soma_idade/contador)

feminina_lista = []
for i in range(len(out_lista)):
	if out_lista[i]['Sexo'] == 'feminino':
		feminina_lista.append(out_lista[i])

acima_media_lista = []
for i in range(len(out_lista)):
	if out_lista[i]['Idade'] > media_idade:
		acima_media_lista.append(out_lista[i])

print('Quantidade cadastrada: {} pessoas'.format(contador))
print('Média de idade cadastrada: {} anos'.format(media_idade))
print('Mulheres cadastradas:')
print(feminina_lista)
print('Pessoas com idade acima da média:')
print(acima_media_lista)
