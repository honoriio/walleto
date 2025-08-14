from src.views.colors import Cores
from getpass import getpass

PRETO, VERMELHO, VERDE, AMARELO, AZUL, MAGENTA, CIANO, BRANCO,PRETO_CLARO, VERMELHO_CLARO, VERDE_CLARO, AMARELO_CLARO, AZUL_CLARO, MAGENTA_CLARO, CIANO_CLARO, BRANCO_CLARO, RESET = Cores()

TM = 160 # --> Variavel destinada a alterar os tamanhos das linhas no programa

versao = '1.0.1-V1'
def cabecalho(): # --> cabeçalho principal do programa
    print('=' * TM)
    print(f'{VERDE}WALLETO{RESET}{AZUL} - {versao}{RESET}'.center(160))
    print('=' * TM)


def menu_escolha(): # --> menu principal do programa, que levara o usuario onde ele desejar 
    print('=' * TM)
    print('[1] - Adicionar Gastos')
    print('[2] - Ver Gastos')
    print('[3] - Sair')
    print('=' * TM)

    opc = int(input('Escolha: '))

    return opc


def sub_menu_escolha():
    print('=' * TM)
    print('[1] - Editar Gastos')
    print('[2] - Excluir Gasto')
    print('[3] - Filtrar Gastos')
    print('[4] - Voltar')
    print('[5] - Sair')
    print('=' * TM)

    sub_opc = int(input('Escolha: '))

    return sub_opc


def menu_login(): # --> menu criado para o login do usuario, em breve irei implementar o login 
    print('=' * TM)
    print('LOGIN WALLETO'.center(TM))
    print('=' * TM) 
    usuario = input('Informe o usuario ou email: ')
    senha = getpass('Digite sua senha: ') # --> oculta a senha informada pelo usuarik


    return usuario, senha


def menu_filtro():
    print('=' * TM)
    print('[1] - Filtrar Por Periodo')
    print('[2] - Filtrar Por Valor')
    print('[3] - Filtrar Por Categoria')
    print('[4] - Filtrar por Nome')
    print('[5] - Sair')
    print('=' * TM)

    opc_filtro = int(input('Escoha: '))

    return opc_filtro


def cabecalho_gastos():
    print('=' * TM)
    print(f'{VERDE}HISTÓRICO DE GASTOS{RESET}'.center(TM))
    print('=' * TM)


def cabecalho_inserir_gastos():
    print('=' * TM)
    print(f'{AZUL}CADASTRAR GASTOS{RESET}'.center(TM))
    print('=' * TM)
    pass