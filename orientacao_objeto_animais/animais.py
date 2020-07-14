class Animais():

	tipo = 'Pet'

	def __init__(self, nome, idade, especie, raca, sexo):

		self.nome = nome
		self.idade = idade
		self.especie = especie
		self.raca = raca
		self.sexo = sexo

	def valida_idade(self):

		if type(self.idade) != int:
			raise('Idade deve ser um inteiro!')

			
