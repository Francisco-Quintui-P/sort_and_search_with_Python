import random
import time

def ordenamiento_insercion(lista):
    tamaño = len(lista)
    
    for i in range(0, tamaño):
        valor_actual = lista[i]
        posicion = i

        while posicion_actual > 0 and lista[posicion_actual - 1] > valor_actual:
            lista[posicion_actual] = lista[posicion_actual - 1]
            posicion_actual -= 1

        lista[posicion_actual] = valor_actual


if __name__ == '__main__':
    tamano_lista = int(input('De que tamano es la lista: ')) 
    lista = [random.randint(0, 100) for i in range(tamano_lista)]
    print(lista)
    comienzo = time.time()
    lista_ordenada = ordenamiento_insercion(lista)
    final = time.time()
    print(final - comienzo)
    print(lista_ordenada)