import random
import time

def ordenamiento_burbuja(lista):
    n = len(lista)

    for i in range(n):
        for j in range(0, n-i-1):#el -1 es pq n es el tamaño y estamos utilizando indices
            if lista[j] > lista[j + 1]:

                if lista[j] > lista [j + 1]:
                    lista[j], lista[j +1] = lista[j +1], lista[j]
    return lista

if __name__ == '__main__':
    tamano_lista = int(input('De que tamano es la lista: '))

    lista = [random.randint(0, 100) for i in range(tamano_lista)]
    print(lista)
    comienzo = time.time()
    lista_ordenada = ordenamiento_burbuja(lista)
    final = time.time()
    print(final - comienzo)
    print(lista_ordenada)