from src.models.gastos import Gasto
import sys
import time
from src.views.colors import Cores
from src.models.utils.input_utils import coletar_dados_edicao
from src.views.tela import limpar_tela
from src.database.gasto_repository import inserir_gasto, criar_tabela, listar_gastos, excluir_gastos, editar_gastos, filtrar_gastos_data, calcular_gastos, filtrar_gasto_valor, filtrar_gastos_categoria, filtrar_gastos_nome
from src.views.menu import cabecalho, menu_escolha, menu_login, sub_menu_escolha, menu_filtro
PRETO, VERMELHO, VERDE, AMARELO, AZUL, MAGENTA, CIANO, BRANCO,PRETO_CLARO, VERMELHO_CLARO, VERDE_CLARO, AMARELO_CLARO, AZUL_CLARO,MAGENTA_CLARO, CIANO_CLARO, BRANCO_CLARO, RESET = Cores()



def main():
    while True:
        cabecalho()
        print(f'{VERDE}-{RESET}' * 60)
        opc = menu_escolha()
        
        match opc:
            case 1: # --> opção de adiconar os gastos ( o usuario insere os gastos que deseja.)
                criar_tabela()
                nome, valor, categoria, descricao, data = Gasto.entradas()
                novo_gasto = Gasto(nome, valor, categoria, descricao, data)
                inserir_gasto(novo_gasto)

            case 2: # --> opção de ver os gastos inseridos.
                limpar_tela()
                print('=' * 60)
                listar_gastos()
                sub_opc = sub_menu_escolha()

                match sub_opc:
                    case 1: # --> opção de editar os dados
                        dados = coletar_dados_edicao()
                        editar_gastos(dados)
                        print('=' * 60)
                        listar_gastos()

                    case 2: # --> opção de excluir um gasto
                        gasto_id = int(input('Informe o ID do gasto: '))
                        excluir_gastos(gasto_id)
                        listar_gastos()

                    case 3: # --> submenu d e filtros
                        opc_filtro = menu_filtro()
                        match opc_filtro:
                            case 1: # --> filtra os gastos por data/periodo
                                data_inicio = input('Inicio: ')
                                data_final = input('Final: ')
                                filtrar_gastos_data(data_inicio, data_final)

                            case 2:# --> filtra os gastos por valor, o mesmo recebe dois valores e filtra os gastos entre os intervalos incluindo os valores informados.
                                valor_min = input('Valor Minimo: ')
                                valor_max = input('Valo Maximo: ')
                                filtrar_gasto_valor(valor_min, valor_max)
                    case 4: # --> volta ao menu anterior.
                        pass
                    
                    case 5: # --> encerra o programa
                        limpar_tela()
                        print('=' * 60) 
                        print(f'{VERMELHO}PROGRAMA ENCERRADO...{RESET}'.center(60))
                        print('=' * 60)
                        time.sleep(2)
                        limpar_tela()
                        sys.exit()
            
            case 3: # --> Fecha o programa.
                limpar_tela()
                print('=' * 60) 
                print(f'{VERMELHO}PROGRAMA ENCERRADO...{RESET}'.center(60))
                print('=' * 60)
                time.sleep(2)
                limpar_tela()
                sys.exit()


if __name__ == "__main__":   
    main()
    