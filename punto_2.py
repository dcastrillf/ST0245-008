import numpy as np
import time


# Creamos una funcion para eliminar los duplicados suponiendo que le va a entrar
# como parametro un vector ya ordenado
def eliminar_duplicados(array):
    resultante = []  # 1 asignación
    visto = None  # 1 asignación
    for i in array:  # n iteraciones
        if visto == i:  # n commparaciones
            continue
        else:
            visto = i  # n asignaciones
            resultante.append(i)  # Incerción
    resultante = np.array(resultante)
    return resultante
# 1 + 1 + n + n = 2 + 2n


# Creamos un vector ya ordenado
vector = np.array([3, 4, 4, 5, 5, 7, 7, 9, 11, 11])

start_time = time.time()

# Igualamos la lista a la función aplicada a esta misma para que se nos modifique
# la inicial y no sea solo mostrarla sin los duplicados
vector = eliminar_duplicados(vector)

# Imprimimos el tiempo de ejecución
print("Tiempo de ejecución", "{:.10f}".format(time.time() - start_time))

# Imprimimos el vector ya modificado
print(vector)
print(type(vector))
