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

def suma_potencia_digitos(a:int) -> int:
    n_digitos: int = digitos_de_un_numero(a)
    digitos: list[int] = aislar_digitos_de_un_numero(a)
    suma = 0
    for digito in digitos:
        suma += digito**n_digitos
    return suma

def es_narcisista(a:int) -> bool:
    return a == suma_potencia_digitos(a)

def main():
    count = 1
    while True:
        if es_narcisista(count):
            print(count)
        count += 1

if __name__  == "__main__":
    main()