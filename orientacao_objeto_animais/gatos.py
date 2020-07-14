from animais import Animais

class gatos(Animais):

	def __init__(self, nome, idade, raca, sexo):
		
		Animais.__init__(self, nome, 'gato', idade, raca, sexo)
