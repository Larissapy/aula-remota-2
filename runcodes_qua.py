def maior(a,b,c,d,e):
    return max(a,b,c,d,e)

def menor(a,b,c,d,e):
    return min(a,b,c,d,e)

def media(a,b,c,d,e):
    return (a + b + c + d + e) / 5

def main():
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())

    mai = maior(a,b,c,d,e)
    men = menor(a,b,c,d,e)
    med = media(a,b,c,d,e)        

    print(f'{mai}')
    print(f'{men}')
    print(f'{med}')              

if __name__ == "__main__":
    main()

