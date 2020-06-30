from veiculo import Veiculos

class Carros(Veiculos):

	def __init__(self, marca, cor, volume_combustivel):

		Veiculos.__init__(self, 4, marca, cor, volume_combustivel)
