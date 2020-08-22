def nome(Larissa):
    return len(Larissa)
def main():
    name = input('Digite um nome: ')

    caracteres = nome(name)

    print(f'O nome possui {caracteres} caracterres')

if __name__ == "__main__":
    main()
    
