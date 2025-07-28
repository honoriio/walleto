# Local destinado para importações 
from src.models.utils.validacao import validar_entrada, validar_data, validar_nome
import datetime


class Gasto:
    #Representa um gasto individual com valor, categoria, descrição e data.
    #Fornece método estático para entrada e validação de dados via terminal.
    def __init__(self, nome, valor, categoria, descricao, data):
        self.nome = nome
        self.valor = valor
        self.categoria = categoria
        self.descricao = descricao
        self.data = data


    @staticmethod
    def entradas(): 
    # Coleta e valida os seguintes dados do usuário:
    # - Nome do gasto
    # - Valor do gasto
    # - Categoria do gasto
    # - Descrição do gasto
    # - Data do gasto
    
        global id_atual

        while True:
            entrada = input("Informe o Nome: ")
            valido, resultado = validar_nome(entrada)

            if valido:
                nome = resultado  # nome está validado
                break
            else:
                print(f"Erro: {resultado}")


        while True:
            entrada = input("valor R$: ")
            valido, valor_convertido = validar_entrada(entrada)

            if valido:
                valor = valor_convertido  # Só o valor decimal aqui
                break
            else:
                print('O valor informado está incorreto, por favor, insira o valor novamente.')


        # Solicita a categoria. Se o usuário não digitar nada, define como padrão.
        categoria = input("Categoria: ").strip()
        if categoria == "":
            categoria = "Categoria Não informada"

        # Solicita a Descrição. Se o usuário não digitar nada, define como padrão.
        descricao = input("Descrição: ").strip()
        if descricao == "":
            descricao =  "Descrição Não informada"


        while True:
            data = input("Informe a Data: ")

            # Verifica se o usuário deixou o campo vazio. Caso sim, usa a data atual formatada.
            if data.strip() == "":
                data = datetime.datetime.now().date()
                data = data.strftime("%d/%m/%Y")
                break
        
            data = validar_data(data)
            if data is not None:
                break
            else:
                print('A data inserida esta incorreta.')


        return nome, valor, categoria, descricao, data
