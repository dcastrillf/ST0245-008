import time


# Creamos una funcion que es la que eliminará los dato repetidos
def eliminar_duplicados(lista):
    resultante = []  # 1 asignación
    for i in lista:  # n iteraciones
        if i not in resultante:  # n iteraciones y n comparaciones
            resultante.append(i)  # incerción
    return resultante
# 1 + n + n*n = 1 + n + n^2


# Creamos una lista
lista_1 = [4, 7, 11, 4, 9, 5, 11, 7, 3, 5]

start_time = time.time()

# Igualamos la lista a la función aplicada a esta misma para que se nos modifique
# la inicial y no sea solo mostrarla sin los duplicados
lista_1 = eliminar_duplicados(lista_1)

# Imprimimos el tiempo de ejecución
print("Tiempo de ejecución", "{:.10f}".format(time.time() - start_time))

# Imprimimos la lista modificada
print(lista_1)
