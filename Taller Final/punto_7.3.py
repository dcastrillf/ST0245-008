# Punto 7.3


class Alumno:
    def __init__(self, nombre, edad, nota):
        self.nombre = nombre
        self.edad = edad
        self.nota = nota

    def __str__(self):
        return self.nombre + ' - ' + str(self.edad) + ' años : ' + str(self.nota)


class Nodo:
    def __init__(self, datos):
        self.datos = datos
        self.siguiente = None


nodo = Nodo(Alumno('Alex', 30, 8.9))
nodo.siguiente = Nodo(Alumno('Pepe', 27, 3.7))

actual = nodo
while actual is not None:
    print(actual.datos)
    actual = actual.siguiente
