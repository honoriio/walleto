# Local destinado as importações   
import datetime


def validar_entrada(valor):
    # Tenta converter o valor informado em float.
    # Retorna o número em ponto flutuante se for válido, senão retorna None.
    try:
        return float(valor)
    except ValueError:
        return None



def validar_data(data):
    # Tenta converter a string no formato 'dd/mm/aaaa' para um objeto date.
    # Retorna a data convertida se for válida, senão retorna None.
    try:
        return datetime.datetime.strptime(data, "%d/%m/%Y").date()
    except ValueError:
        return None

