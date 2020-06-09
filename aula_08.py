# Aula funcoes

# Funcoes

def saudacao():
	print('Olá')

def soma_dois_numeros(num1, num2):
	return num1 + num2

def calcula_idade(ano_nascimento, ano_atual):

	idade = ano_atual - ano_nascimento

	print(idade)

	return idade

def eleva_numero(base, expoente):
	return base ** expoente, base

def calculo(a, b, c=3):

	media = (a+b+c)/3

	resultado = media + (a/b)

	return resultado


resultado = calculo(b=4,a=16,c=8)
print(resultado)

'''
saudacao()
soma = soma_dois_numeros(3, 7)
print(soma)


ano_nascimento = 1970
ano_atual = 2020

idade = calcula_idade(ano_nascimento, ano_atual)


metade_idade = idade/2
print(metade_idade)

resultado, base = eleva_numero(2, 2)

print(resultado)
print(base)
'''
