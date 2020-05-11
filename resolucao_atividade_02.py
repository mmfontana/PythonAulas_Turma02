# Exercicio Triangulos
# Link utilizado para teoria de triangulos
# https://matematicabasica.net/triangulo/


a = float(input('Entre com a medida a do triângulo em metros: '))
b = float(input('Entre com a medida b do triângulo em metros: '))
c = float(input('Entre com a medida c do triângulo em metros: '))

if (abs(b-c)<a<(b+c)) and (abs(a-c)<b<(a+c)) and (abs(a-b)<c<(a+b)):
	
	if a==b and a==c:
		tipo_triangulo = 'equilatero'
	elif a==b or a==c or b==c:
		tipo_triangulo = 'isoceles'
	else:
		tipo_triangulo = 'escaleno'

	print('As medidas {} m, {} m e {} m formam um triângulo do tipo {}.'.format(a, b, c, tipo_triangulo))	

else:
	print('As medidas {} m, {} m e {} m não formam um triângulo'.format(a, b, c))


# Soma de Gauss

soma = 0
n = 0

while(n<100):

	n += 1
	soma += n

print(soma)












