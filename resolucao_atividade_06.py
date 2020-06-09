# Resolucao atividade 06

# Exercicio 1
'''
string_1 = 'Brasil Hexa 2006'
string_2 = 'Brasil! Hexa 2006!'

len_string_1 = len(string_1)
len_string_2 = len(string_2)

print('Tamanho de "{}": {} caracteres'.format(string_1, len_string_1))
print('Tamanho de "{}": {} caracteres'.format(string_2, len_string_2))

if len_string_1 == len_string_2:
	print('As duas strings são de tamanhos iguais')
else:
	print('As duas strings são de tamanhos diferentes')

if string_1 == string_2:
	print('As duas strings tem conteúdos iguais')
else:
	print('As duas strings não tem conteúdos iguais')
'''

# Exercicio 2

'''
n = 44444
n = str(n)
n = list(n)

d = 4
d = str(d)

soma = 0 
for n_string in n:
	if n_string == d:
		soma += 1
print(soma)
'''			

# Resolucao com metodo

n = 444444
n = str(n)

d = 4
d = str(d)

soma = n.count(d)

print(soma)
