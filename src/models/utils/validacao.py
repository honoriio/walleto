# Local destinado as importações   
import datetime
import re


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

def validar_nome(nome):
    nome = nome.strip()
    
    if not nome:
        return False, "O nome do gasto não pode estar em branco"
    
    if len(nome) < 3:
        return False, "O nome do gasto deve conter pelo menos 3 caracteres"
    
    if len(nome) > 20:
        return False, "O nome do gasto não pode ter mais de 20 caracteres"
    
    if not re.search(r"[a-zA-Z0-9]", nome):
        return False, "O nome do gasto deve conter pelo menos uma letra ou número."

    return True, nome