import time

def digitos_de_un_numero(a:int) -> int:
    count = 1
    while a >=10:
        a = a // 10
        count = count + 1
        if a < 10:
            return count
    return 1

def aislar_digitos_de_un_numero(a:int) -> list[int]:
    lista = []
    while a > 0:
        lista.append(a % 10)
        a = a // 10
    return lista

def crear_numero_al_reves(a:int) -> int:
    n_digitos: int = digitos_de_un_numero(a)
    digitos: list[int] = aislar_digitos_de_un_numero(a)
    suma = 0
    for digito in digitos:
        n_digitos = n_digitos - 1
        suma = suma + digito * 10**n_digitos
    return suma

def es_palindromo(a:int) -> bool:
    return a == crear_numero_al_reves(a)

def main():
    count = 1
    while True:
        if es_palindromo(count):
            print(count)
            time.sleep(1)
        count += 1

if __name__  == "__main__":
    main()