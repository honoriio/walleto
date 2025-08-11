from src.models.gastos import Gasto
from src.models.utils.input_utils import coletar_dados_edicao
from src.database.gasto_repository import inserir_gasto, criar_tabela, listar_gastos, excluir_gastos, editar_gastos, filtrar_gastos_data, calcular_gastos
from src.views.menu import menu

def main():
    menu()
    decisao = input('Filtrar Gastos? ').upper()
    if decisao == "SIM":
        inicio = input('inicio: ')
        fim = input('fim: ')
        resultado = filtrar_gastos_data(inicio, fim) # Criar a logica de coleta para os filtros
        total = calcular_gastos(resultado)
        print(total)

if __name__ == "__main__":   
    main()
    