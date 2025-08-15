# Area destinada as importações
from src.database.connection import get_connection
from decimal import Decimal
from src.views.colors import Cores

PRETO, VERMELHO, VERDE, AMARELO, AZUL, MAGENTA, CIANO, BRANCO, PRETO_CLARO, VERMELHO_CLARO, VERDE_CLARO, AMARELO_CLARO, AZUL_CLARO, MAGENTA_CLARO, CIANO_CLARO, BRANCO_CLARO, RESET = Cores()

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


# Função que edita os gastos com base no id fornecido para localziar o gastos, e apos isso usa os dados coletados para editar o gasto.
# A função ja tem tratamento de erro e retorno de mensagens de erro.
def editar_gastos(dados):
    try:
        with get_connection() as conn:
            cursor = conn.cursor()

            cursor.execute("SELECT nome, valor, categoria, descricao, data FROM gastos WHERE id = ?", (dados["id"],))
            resultado = cursor.fetchone()

            if not resultado:
                return {"status": "erro", "mensagem": "Gasto não encontrado."}

            nome_antigo, valor_antigo, categoria_antiga, descricao_antiga, data_antiga = resultado

            nome = dados.get("nome", nome_antigo)
            valor = float(dados["valor"]) if dados.get("valor") and str(dados["valor"]).replace(".", "").replace("-", "").isdigit() else valor_antigo
            categoria = dados.get("categoria", categoria_antiga)
            descricao = dados.get("descricao", descricao_antiga)
            data = dados.get("data", data_antiga)

            cursor.execute("""
                UPDATE gastos
                SET nome = ?, valor = ?, categoria = ?, descricao = ?, data = ?
                WHERE id = ?
            """, (nome, valor, categoria, descricao, data, dados["id"]))

            if cursor.rowcount > 0:
                conn.commit()
                return {"status": "sucesso", "mensagem": "Gasto editado com sucesso!"}
            else:
                return {"status": "erro", "mensagem": "Nenhuma alteração realizada."}

    except KeyError as e:
        return {"status": "erro", "mensagem": f"Chave {e} não encontrada nos dados fornecidos."}
    except ValueError as e:
        return {"status": "erro", "mensagem": "Valor inválido para o campo 'valor'. Use um número válido."}
    except Exception as e:
        return {"status": "erro", "mensagem": f"Erro ao editar gasto: {e}"}





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
            print(f"ID: {id} Nome Do Gasto: {nome}, Valor: R${valor}, Categoria: {categoria}, Descrição: {descricao}, Data: {VERDE}{data}{RESET} ")
            print('-' * 160)

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
            print(f"ID: {id} Nome Do Gasto: {nome}, Valor: R${VERDE}{valor}{RESET}, Categoria: {categoria}, Descrição: {descricao}, Data: {data} ")
            print('-' * 160)

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
            print(f"ID: {id} Nome Do Gasto: {nome}, Valor: R${valor}, Categoria: {VERDE}{categoria}{RESET}, Descrição: {descricao}, Data: {data} ")
            print('-' * 160)

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
            print(f"ID: {id} Nome Do Gasto: {VERDE}{nome}{RESET}, Valor: R${valor}, Categoria: {categoria}, Descrição: {descricao}, Data: {data} ")
            print('-' * 160)

        return resultados

# Função criada para calcular o total gasto por filtro
def calcular_gastos(valor):
    total = sum(linha[2] for linha in valor)
    return total
