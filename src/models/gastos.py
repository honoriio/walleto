# Local destinado para importações 

class Gasto:
    def __init__(self, valor, categoria, descricao, data):
        self.valor = valor
        self.categoria = categoria
        self.descricao = descricao
        self.data = data


    @staticmethod
    def cadastrar_gasto():
        valor = input('Informe o Valor: R$ ')
        categoria = input('Categoria: ')
        descricao = input('Descrição: ')
        data = input('Informe a data: ')

        return valor, categoria, descricao, data
    
    