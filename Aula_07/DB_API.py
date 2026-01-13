import sqlite3 # Chamar o SQL
from pathlib import Path # Colocar o caminho

ROOT_PATH = Path(__file__).parent

conexao = sqlite3.connect(ROOT_PATH / "meu_banco.sqlite")
cursor = conexao.cursor()

def criar_tabela(conexao, cursor): # Comando CREATE TABLE
    cursor.execute("""
    CREATE TABLE clientes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome VARCHAR(100),
        email VARCHAR(150)
    )
    """)
    conexao.commit()

def insert_into(conexao, cursor, nome, email): # Comando INSERT INTO
    data = (nome, email)
    cursor.execute(" INSERT INTO clientes (nome, email) VALUES(?,?);", data)
    conexao.commit()

def update_table(conexao, cursor, nome, email, id):# Comando UPDATE
    data = (nome, email, id)
    cursor.execute("UPDATE clientes SET nome=?, email=? WHERE id=?", data)
    conexao.commit()

def delete_info(conexao, cursor, id): # Comando DELETE
    data = (id,)
    cursor.execute("DELETE FROM clientes WHERE id=?;", data)
    conexao.commit()

def insert_many(conexao, cursor, dados): # Comando INSERT INTO porem com mais de uma linha 
    cursor.executemany(" INSERT INTO clientes (nome, email) VALUES(?,?);", dados)
    conexao.commit()

def select_from(cursor, id): # Comando SELECT 
    cursor.execute("SELECT * FROM clientes WHERE id=?", (id,))
    return cursor.fetchone()

cliente = select_from(cursor, 1)
print(cliente)

def select_all(cursor,): # Comando SELECT "ALL"
    return cursor.execute("SELECT * FROM clientes")

clientes = select_all(cursor)
for cliente in clientes:
    print(cliente)


# dados = [
#    ("Brunno", "email@Bruno.com"),
#    ("Guilherme", "email@guilherme.com"),
#    ("Garcibinha", "email@garciba")
#]

# insert_many(conexao, cursor, dados)
# update_table(conexao, cursor, "Erick Sagat", "test@test.com", 1)    
# delete_info(conexao, cursor, 2)