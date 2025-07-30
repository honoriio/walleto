from src.models.gastos import Gasto
from src.models.utils.input_utils import coletar_dados_edicao
from src.database.gasto_repository import inserir_gasto, criar_tabela, listar_gastos, excluir_gastos, editar_gastos


def main():
    criar_tabela()
    nome, valor, categoria, descricao, data = Gasto.entradas()
    novo_gasto = Gasto(nome, valor, categoria, descricao, data)
    inserir_gasto(novo_gasto)
    listar_gastos()
    dados = coletar_dados_edicao()
    editar_gastos(dados)


if __name__ == "__main__":
    main()
    