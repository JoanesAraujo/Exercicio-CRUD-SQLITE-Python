import sqlite3
from sqlite3.dbapi2 import Cursor

banco = sqlite3.connect("banco_de_dados_teste.db")

Cursor = banco.cursor()

#Cursor.execute("CREATE TABLE pessoas (nome text, idade number, telefone number)")
Cursor.execute("INSERT INTO pessoas  VALUES ('Caligula', 37, 81987585574)")

banco.commit()
banco.close()