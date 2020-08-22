def maior(a,b,c,d,e):
    return max(a,b,c,d,e)

def menor(a,b,c,d,e):
    return min(a,b,c,d,e)

def media(a,b,c,d,e):
    return (a + b + c + d + e) / 5

def main():
    a = int(input('Digite o primeiro número: '))
    b = int(input('Digite o segundo número: '))
    c = int(input('Digite o terceiro número: '))
    d = int(input('Digite o quarto número: '))
    e = int(input('Digite o quinto número: '))

    mai = maior(a,b,c,d,e)
    men = menor(a,b,c,d,e)
    med = media(a,b,c,d,e)        

    print(f'O maior número lido: {mai}')
    print(f'O menor número lido: {men}')
    print(f'A média aritimética dos números lidos: {med}')              

if __name__ == "__main__":
    main()

