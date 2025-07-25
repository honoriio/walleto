from src.models.gastos import Gasto
from src.database.gasto_repository import inserir_gasto, criar_tabela, listar_gastos, excluir_gastos


def main():
    criar_tabela()
    valor, categoria, descricao, data = Gasto.entradas()
    novo_gasto = Gasto(valor, categoria, descricao, data)
    inserir_gasto(novo_gasto)
    listar_gastos()

if __name__ == "__main__":
    main()
    