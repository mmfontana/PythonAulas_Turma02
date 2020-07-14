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
	# Cria tabela de usuarios
	cria_tabela_usuarios = """
	CREATE TABLE IF NOT EXISTS usuarios (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	nome TEXT NOT NULL,
	idade INTEGER,
	sexo TEXT,
	cidade TEXT
	);
	"""
	execucao_query(coneccao, cria_tabela_usuarios)
	cria_tabela_posts = """
	CREATE TABLE IF NOT EXISTS posts (
	id INTEGER NOT NULL,
	titulo TEXT NOT NULL,
	texto TEXT NOT NULL,
	usuario_id INTEGER NOT NULL,
	FOREIGN KEY (usuario_id) REFERENCES usuarios (id)
	);
	"""
	execucao_query(coneccao, cria_tabela_posts)
	# Cria usuarios
	cria_usuarios = """
	INSERT INTO
		usuarios (nome, idade, sexo, cidade)
	VALUES
		('Maycon', 27, 'M', 'Florianopolis'),
		('Jaque', 12, 'F', 'Florianopolis'),
		('Marcos', 6, 'M', 'Florianopolis')
	"""
	# execucao_query(coneccao, cria_usuarios)
	# Cria posts
	cria_posts = """
	INSERT INTO
		posts (id, titulo, texto, usuario_id)
	VALUES
		(1, 'Como fazer um append numa lista?', 'Use o metodo .append', 1),
		(2, 'Problema no Sublime', 'Sublime nao executa', 3)
	"""
	# execucao_query(coneccao, cria_posts)
	selecionar_usuarios = "SELECT * from usuarios"
	usuarios = execucao_leitura_query(coneccao, selecionar_usuarios)
	print(type(usuarios))

	for usuario in usuarios:
		print(usuario[1])
