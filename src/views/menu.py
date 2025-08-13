from colors import Cores
from getpass import getpass

PRETO, VERMELHO, VERDE, AMARELO, AZUL, MAGENTA, CIANO, BRANCO,PRETO_CLARO, VERMELHO_CLARO, VERDE_CLARO, AMARELO_CLARO, AZUL_CLARO, MAGENTA_CLARO, CIANO_CLARO, BRANCO_CLARO, RESET = Cores()

versao = '1.0.1-V1'
def cabecalho(): # --> cabeçalho principal do programa
    print('=' * 60)
    print(f'{VERDE}WALLETO{RESET}{AZUL} - {versao}{RESET}'.center(60))
    print('=' * 60)


def menu_escolha(): # --> menu principal do programa, que levara o usuario onde ele desejar 
    print('=' * 60)
    print('[1] - Ver gastos')
    print('[2] - Adicionar gastos')
    print('[3] - Editar Gasto')
    print('[4] - Excluir Gasto')
    print('[5] - Sair')
    print('=' * 60)

    opc = input('Escolha: ')

    return opc


def menu_login(): # --> menu criado para o login do usuario, em breve irei implementar o login 
    print('=' * 60)
    print('LOGIN WALLETO'.center(60))
    print('=' * 60) 
    usuario = input('Informe o usuario ou email: ')
    senha = getpass('Digite sua senha: ') # --> oculta a senha informada pelo usuarik


    return usuario, senha



