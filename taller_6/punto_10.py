import numpy as np

n = int(input("Que numero desea buscar: "))

matriz = np.random.randint(20, size=(4, 6))

if n in matriz:
    print("El", n, "si esta en la matriz")
else:
    print("El", n, "no está en la matriz")

print(matriz)