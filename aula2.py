import sqlite3
from sqlite3.dbapi2 import Cursor

banco = sqlite3.connect("banco_de_dados_teste.db")

Cursor = banco.cursor()

Cursor.execute("SELECT * FROM pessoas WHERE nome = 'Joanes' ")

values = Cursor.fetchall()


print(values)