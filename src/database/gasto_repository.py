# Area destinada as importações
from src.database.connection import get_connection
from decimal import Decimal


def criar_tabela(): # Cria a tabela gastos para armazenar os dados.
    with get_connection() as conn:
        cursor = conn.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS gastos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT,
                valor NUMERIC NOT NULL,
                categoria TEXT,
                descricao TEXT,
                data TEXT
            )
        """)

        conn.commit()



def inserir_gasto(gasto): # insere os valores informados pelo usuario a tabela gastos 
    with get_connection() as conn:
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO gastos (nome, valor, categoria, descricao, data) VALUES (?, ?, ?, ?, ?)", 
            (gasto.nome, float(gasto.valor), gasto.categoria, gasto.descricao, gasto.data)
        )

        conn.commit()



def excluir_gastos(id): # exclui o gasto com base no ID informado pelo usuario 

    with get_connection() as conn:
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM gastos WHERE id = ?", (id,))
        resultado = cursor.fetchone()

        if resultado is None:
            print("Nenhum gasto encontrado com esse ID.")
        else:
            cursor.execute(" DELETE FROM gastos WHERE id = ?", (id,))
            conn.commit()
            print(f"Gasto com ID {id} foi excluído com sucesso.")


# Preciso entender o que foi feito aqui 
def editar_gastos(dados):
    with get_connection() as conn:
        cursor = conn.cursor()

        # Buscar dados antigos
        cursor.execute("SELECT nome, valor, categoria, descricao, data FROM gastos WHERE id = ?", (dados["id"],))
        resultado = cursor.fetchone()

        if not resultado:
            print("Gasto não encontrado.")
            return

        nome_antigo, valor_antigo, categoria_antiga, descricao_antiga, data_antiga = resultado

        # Substituir somente se o novo valor foi informado
        nome = dados["nome"] if dados["nome"] else nome_antigo
        valor = float(dados["valor"]) if dados["valor"] else valor_antigo
        categoria = dados["categoria"] if dados["categoria"] else categoria_antiga
        descricao = dados["descricao"] if dados["descricao"] else descricao_antiga
        data = dados["data"] if dados["data"] else data_antiga

        # Agora faz o UPDATE com segurança
        cursor.execute("""
            UPDATE gastos
            SET nome = ?, valor = ?, categoria = ?, descricao = ?, data = ?
            WHERE id = ?
        """, (nome, valor, categoria, descricao, data, dados["id"]))

        conn.commit()




def listar_gastos(): # Lista os gastos que estão no banco de dados do usuario.
    with get_connection() as conn:
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM gastos")
        resultados = cursor.fetchall()


        for id, nome, valor, categoria, descricao, data in resultados:

            valor = Decimal(valor) # Causa erro
            valor = f"R$ {valor:,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.')

            print(f"ID: {id} | Nome Do Gasto: {nome} | Valor: {valor} | Categoria: {categoria} | Descrição: {descricao} | Data: {data} ")
            print('-' * 160)

        return resultados
    

# Refatorar a função  PAUSA PARA ESTUDO, AINDA NÃO APRENDI O SUFICIENTE DE SQL PARA PROCEGUIR
# Adicionar filtragem por usuario para tornar essa aplicação multiusuario....
def filtrar_gastos_data(data_inicio, data_final):
    with get_connection() as conn:
        cursor  = conn.cursor()

        cursor.execute("SELECT * FROM gastos WHERE data BETWEEN ? AND ?", (data_inicio, data_final))
        resultados = cursor.fetchall()

        for id, nome, valor, categoria, descricao, data in resultados:

            valor = Decimal(valor)
            valor = f"R$ {valor:,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.')

            # Retirar isso depois e manter somente o return
            print(f"ID: {id} Nome Do Gasto: {nome}, Valor: R${valor}, Categoria: {categoria}, Descrição: {descricao}, Data: {data} ")

        return resultados

# Adicionar filtragem por usuario para tornar essa aplicação multiusuario....
def filtrar_gasto_valor(valor_min, valor_max):
    with get_connection() as conn:
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM gastos WHERE valor BETWEEN ? AND ?", (valor_min, valor_max))
        resultados = cursor.fetchall()

        for id, nome, valor, categoria, descricao, data in resultados:
            valor = Decimal(valor)
            valor = f"R$ {valor:,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.')

            # Retirar isso depois e manter somente o return
            print(f"ID: {id} Nome Do Gasto: {nome}, Valor: R${valor}, Categoria: {categoria}, Descrição: {descricao}, Data: {data} ")

        return resultados

# Adicionar filtragem por usuario para tornar essa aplicação multiusuario....
def filtrar_gastos_categoria(categoria):
    with get_connection() as conn:
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM gastos WHERE categoria = ?", (categoria,))
        resultados = cursor.fetchall()

        for id, nome, valor, categoria, descricao, data in resultados:
            valor = Decimal(valor)
            valor = f"R$ {valor:,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.')

            # Retirar isso depois e manter somente o return
            print(f"ID: {id} Nome Do Gasto: {nome}, Valor: R${valor}, Categoria: {categoria}, Descrição: {descricao}, Data: {data} ")

        return resultados

# Adicionar filtragem por usuario para tornar essa aplicação multiusuario....
def filtrar_gastos_nome(nome):
    with get_connection() as conn:
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM gastos WHERE nome = ?", (nome,))
        resultados = cursor.fetchall()

        for id, nome, valor, categoria, descricao, data in resultados:
            valor = Decimal(valor)
            valor = f"R$ {valor:,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.')

            # Retirar isso depois e manter somente o return
            print(f"ID: {id} Nome Do Gasto: {nome}, Valor: R${valor}, Categoria: {categoria}, Descrição: {descricao}, Data: {data} ")

        return resultados

# Função criada para calcular o total gasto por filtro
def calcular_gastos(valor):
    total = sum(linha[2] for linha in valor)
    return total
