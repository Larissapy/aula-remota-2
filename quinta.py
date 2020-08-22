def a_vista(preco):
    return preco - (preco * 0.09)

def a_prazo(preco):
    return preco / 5

def juros(preco):
    return ((preco * 0.17) + preco) / 10

def main():
    valor = float(input('Digite o valor: '))

    desconto = a_vista(valor)
    parcela = a_prazo(valor)
    c_juros = juros(valor)

    print(f'Valor para pagamento à vista: {desconto:.2f}')
    print(f'Valor para pagamento dividido em 5x: {parcela:.2f}')
    print(f'Valor para pagamento dividido em 10x: {c_juros:.2f}')

if __name__ == "__main__":
    main()
