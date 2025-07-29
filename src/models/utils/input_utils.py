# Area destinada as importações


# Preciso criar um tratamento para a coleta de dados para a edição dos gastos. 
def coletar_dados_edicao(): # Função criada para editar os gastos.
    id = input("Informe o id da edição: ")

    nome = input("Nome do gasto: ")
    valor = input("valor R$: ").strip().replace(',', '.')
    categoria = input("Categoria: ").strip()
    descricao = input("Descrição: ").strip()
    data = input("Informe a Data: ")


    valor = float(valor)

    return {
        "id": id,
        "nome": nome if nome else None,
        "valor": valor if valor else None,
        "categoria": categoria if categoria else None,
        "descricao": descricao if descricao else None,
        "data": data if data else None
    }
