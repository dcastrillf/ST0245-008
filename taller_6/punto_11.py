from random import randrange

def quick_sort(lista):
    izquierda = []
    derecha = []
    centro = []
    if len(lista) > 1:
        pivote = lista[0]
        for i in lista:
            if i < pivote:
                izquierda.append(i)
            elif i == pivote:
                centro.append(i)
            else:
                derecha.append(i)
        return quick_sort(izquierda) + centro + quick_sort(derecha)
    else:
        return lista


def crear_lista(n):
    lista = []
    for i in range(n):
        lista.append(randrange(101))
    return lista


lista_A = crear_lista(100)
lista_B = crear_lista(60)

lista_A = quick_sort(lista_A)
lista_B = quick_sort(lista_B)

lista_C = []
lista_C.extend(lista_A)
lista_C.extend(lista_B)
quick_sort(lista_C)

print(lista_C)
