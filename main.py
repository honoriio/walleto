from src.models.gastos import Gasto


def main():
    valor, categoria, descricao, data = Gasto.entradas()
    novo_gasto = Gasto(valor, categoria, descricao, data)

    print(novo_gasto.valor)
    print(novo_gasto.categoria)
    print(novo_gasto.descricao)
    print(novo_gasto.data)


if __name__ == "__main__":
    main()
    