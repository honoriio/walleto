# Local destinado as importações   
import datetime
import re
from decimal import Decimal, InvalidOperation


def validar_entrada(valor):
    valor = valor.strip().replace(',', '.')
    if not valor:
        return False, "O valor não pode estar em branco"
    
    try:
        valor = Decimal(valor)
    except InvalidOperation:
        return False, "Valor inválido, informe apenas números"
    
    if valor <= 0:
        return False, "O valor deve ser maior que zero"
    
    return True, valor


def validar_data(data):
    # Tenta converter a string no formato 'dd/mm/aaaa' para um objeto date.
    # Retorna a data convertida se for válida, senão retorna None.
    try:
        data = datetime.datetime.strptime(data, "%d/%m/%Y").date()
        return data.strftime("%d/%m/%Y")
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