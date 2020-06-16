# Resolucao atividade 6 funcoes

def recebe_usuario():

	continuar = True	

	valor_prestacao = float(input("Valor da prestação: "))

	if valor_prestacao != float(0):
		dias_atraso = float(input("Dias em atraso: "))
	else:
		continuar = False
		dias_atraso = 0

	return valor_prestacao, dias_atraso, continuar


def valor_pagamento(valor_prestacao, dias_atraso):

	multa = valor_prestacao * 0.03
	juro = valor_prestacao * ((0.001) ** dias_atraso)
	valor_final = valor_prestacao + multa + juro

	print("Valor final a ser pago com juros: R$ {}".format(valor_final))

	return valor_final


if __name__ == "__main__":

	n_prestacoes = 0
	soma_prestacoes = 0

	while(True):

		valor_prestacao, dias_atraso, continuar = recebe_usuario()

		if continuar == False:
			print("Foram pagas {} prestações no valor total de R$ {}".format(n_prestacoes, soma_prestacoes))
			break
		else:
			valor_final = valor_pagamento(valor_prestacao, dias_atraso)
			n_prestacoes += 1
			soma_prestacoes += valor_final