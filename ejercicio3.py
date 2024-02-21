import random

def busqueda_binaria(l: list[int], a: int, init: int = 0, end: int = None) -> int:
    if init == end and l[init] == a:
        return init
    if init == end and l[init] != a:
        return None
    if end is None:
        end = len(l) - 1
    pivote = (end - init) // 2 + init
    if a <= l[pivote]:
        return busqueda_binaria(l, a, init, pivote)
    else:
        return busqueda_binaria(l, a, pivote + 1, end)

def main():
    digitos_a: list[int] = [1,2,4]
    digitos_b: list[int] = [1,2,3,4,6]
    digitos_c: list[int] = [1,3,4,5,7,8,9]
    digitos_d: list[int] = [i for i in range(0,10000,2)]
    a = random.randint(0,max(digitos_d))
    posicion = busqueda_binaria(digitos_d, a)
    print(a)
    print(posicion)
    if posicion is not None:
        print(digitos_d[posicion])

if __name__  == "__main__":
    main()