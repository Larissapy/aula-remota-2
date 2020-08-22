def codigo_n(a):
    return ord(a)
def main():
    caractere = input('Digite uma letra ou número: ')

    resultado = codigo_n(caractere)

    print(f'O caractere numerico correspondente é {resultado}')

if __name__ == "__main__":
    main()
