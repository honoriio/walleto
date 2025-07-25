# Area destinada as importações
from src.database.connection import get_connection


def criar_tabela(): # Cria a tabela gastos para armazenar os dados.
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS gastos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            valor REAL NOT NULL,
            categoria TEXT,
            descricao TEXT,
            data TEXT
        )
    """)

    conn.commit()
    cursor.close()
    conn.close()


def inserir_gasto(gasto): # insere os valores informados pelo usuario a tabela gastos 
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO gastos (valor, categoria, descricao, data) VALUES (?, ?, ?, ?)", 
        (gasto.valor, gasto.categoria, gasto.descricao, gasto.data)
    )

    conn.commit()

    cursor.close()
    conn.close()


def excluir_gastos(id): # exclui o gasto com base no ID informado pelo usuario 
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM gastos WHERE id = ?", (id,))
    resultado = cursor.fetchone()

    if resultado is None:
        print("Nenhum gasto encontrado com esse ID.")
    else:
        cursor.execute(" DELETE FROM gastos WHERE id = ?", (id,))
        conn.commit()
        print(f"Gasto com ID {id} foi excluído com sucesso.")


    cursor.close()
    conn.close()



def editar_gastos(): # Edita o gasto criado pelo usuario
    conn = get_connection()
    cursor = conn.cursor()
    pass





def listar_gastos(): # Lista os gastos que estão no banco de dados do usuario.
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM gastos")
    resultados = cursor.fetchall()


    for id, valor, categoria, descricao, data in resultados:
        print(f"ID: {id} Valor: R${valor}, Categoria: {categoria}, Descrição: {descricao}, Data: {data} ")

    cursor.close()
    conn.close()
    return resultados