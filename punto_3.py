def incersion(lista):
    for i in range(1, 3):
        valor_a_ordenar = lista[i]
        while lista[i-1] > valor_a_ordenar and i > 0:
            lista[i], lista[i-1] = lista[i-1], lista[i]
            i -= 1
    return lista


lista1 = [47, 3, 21, 32, 56, 92]
lista1 = incersion(lista1)
print(lista1)
