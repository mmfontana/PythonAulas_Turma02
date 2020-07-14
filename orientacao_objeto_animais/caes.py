from animais import Animais

class caes(Animais):

	def __init__(self, nome, idade, raca, sexo):
		
		Animais.__init__(self, nome, 'cão', idade, raca, sexo)

