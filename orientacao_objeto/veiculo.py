class Veiculos():

	nacionalidade = 'Brasil'

	def __init__(self, n_rodas, marca, cor, volume_combustivel):

		self.n_rodas = n_rodas
		self.marca = marca
		self.cor = cor
		self.tanque = volume_combustivel


	def abastecer(self, volume_combustivel):

		self.tanque += volume_combustivel
