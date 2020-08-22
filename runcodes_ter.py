def hora(s):
    return s // 3600

def minuto(s):
    return (s % 3600) // 60

def segundo(s):
    return (s % 3600) % 60

def main():
    s = int(input())

    HH = hora(s)
    MM = minuto(s)
    SS = segundo(s)

    print(f'{HH}:{MM}:{SS}')
            
if __name__ == "__main__":
    main()
