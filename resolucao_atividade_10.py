import sqlite3
from sqlite3 import Error

def cria_coneccao(diretorio):
	coneccao = None
	try:
		coneccao = sqlite3.connect(diretorio)
		print("Coneccao realizada com o Banco de Dados")
	except Error as e:
		print(f"O erro '{e}' ocorreu.")
	return coneccao

def execucao_query(coneccao, query):
	cursor = coneccao.cursor()
	try:
		cursor.execute(query)
		coneccao.commit()
		print("Query realizada")
	except Error as e:
		print(f"O erro '{e}' ocorreu.")

def execucao_leitura_query(coneccao, query):
	cursor = coneccao.cursor()
	result = None
	try:
		cursor.execute(query)
		result = cursor.fetchall()
		return result
	except Error as e:
		print(f"O erro '{e}' ocorreu.")


if __name__ == "__main__":

	# Cria coneccao
	coneccao = cria_coneccao("rede_social.sqlite")

	# Cria tabela de comentarios
	cria_tabela_comments = """
	CREATE TABLE IF NOT EXISTS comments (
	id INTEGER NOT NULL,
	titulo TEXT NOT NULL,
	texto TEXT NOT NULL,
	usuario_id INTEGER NOT NULL,
	post_id INTEGER NOT NULL, 
	FOREIGN KEY (usuario_id) REFERENCES usuarios (id)
	FOREIGN KEY (post_id) REFERENCES posts (id)
	);
	"""
	execucao_query(coneccao, cria_tabela_comments)
