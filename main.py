from src.models.gastos import Gasto
from src.models.utils.input_utils import coletar_dados_edicao
from src.database.gasto_repository import inserir_gasto, criar_tabela, listar_gastos, excluir_gastos, editar_gastos, filtrar_gastos_data


def main():
    criar_tabela()
    nome, valor, categoria, descricao, data = Gasto.entradas()
    novo_gasto = Gasto(nome, valor, categoria, descricao, data)
    inserir_gasto(novo_gasto)
    listar_gastos()
    dados = coletar_dados_edicao()
    editar_gastos(dados)
    decisao = input('Filtrar Gastos? ').upper()
    if decisao == "SIM":
        inicio = input('inicio: ')
        fim = input('fim: ')
        filtrar_gastos_data(inicio, fim) # Criar a logica de coleta para os filtros


if __name__ == "__main__":
    main()
    