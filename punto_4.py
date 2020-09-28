def ordenamiento_de_shell(lista):
    cont = 1
    contador_sublistas = len(lista)//2
    while contador_sublistas > 0:
        print("Pasada #" + str(cont))
        for posicion_inicio in range(contador_sublistas):
            brecha_incercion(lista, posicion_inicio, contador_sublistas)
        contador_sublistas = contador_sublistas//2
        cont += 1
    return lista


def brecha_incercion(lista, inicio, brecha):
    for i in range(inicio + brecha, len(lista), brecha):
        valor_actual = lista[i]
        pos = i
        if lista[pos - brecha] <= valor_actual:
            print("Comparamos:", lista[pos-brecha], "y", valor_actual)
        while pos >= brecha and lista[pos-brecha] > valor_actual:
            print("Comparamos:", lista[pos - brecha], "y", valor_actual)
            print("Intercambio de:", lista[pos-brecha], "y", valor_actual)
            lista[pos] = lista[pos-brecha]
            pos -= brecha
        lista[pos] = valor_actual
        print(lista)


lista1 = [8, 43, 17, 6, 40, 16, 18, 97, 11, 7]
print(ordenamiento_de_shell(lista1))

# Como se demostró con el anterior codigo se termina en 3 pasadas y los respectivos
# cambios se ven al ejecutar el mismo
