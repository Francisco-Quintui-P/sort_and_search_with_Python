import random

def busqueda_binaria(lista, inicio, final, objetivo):

    print(f'buscando {objetivo} entre {inicio} y {final}')

    if inicio > final or (inicio + final) // 2 == len(lista):
        print('No lo pudimos encontrar :(')
        return False

    indice  = (inicio + final) // 2
    print(indice)
    if lista[indice] == objetivo:
        return True
    elif lista[indice] < objetivo:
        return busqueda_binaria(lista, indice + 1, final, objetivo)
    else:
        return busqueda_binaria(lista, inicio, indice - 1, objetivo)


if __name__ == '__main__':
    tamano_lista = int(input('De que tamano es la lista: '))
    objetivo = int(input('Que numero quieres encontrar? '))

    lista = sorted([random.randint(0, 100) for i in range(tamano_lista)])

    encontrado = busqueda_binaria(lista, 0, len(lista), objetivo)

    print(lista)
    print(f'El elemento {objetivo} {"esta " if encontrado else "no esta"} en la lista')
