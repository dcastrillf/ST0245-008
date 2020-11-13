# Punto 8


import pandas as pd


class Companero:
    def __init__(self, nombre, edad, carrera, gustos):
        self.nombre = nombre
        self.edad = edad
        self.carrera = carrera
        self.gustos = gustos

    def __str__(self):
        return self.nombre + '. ' + str(self.edad) + '. ' + self.carrera + '. ' + self.gustos + '.'


class Nodo:
    def __init__(self, datos):
        self.datos = datos
        self.siguiente = None


def readFile(file):
    final = pd.read_csv(file, sep=';', header=None)
    return final


def printData(head):
    while head is not None:
        print('------------------------------------------'
              '------------------------------------------')
        print(head.datos)
        head = head.siguiente


def convertToSingleLinkedList(pandasFile):
    matrix = pd.DataFrame(pandasFile).to_numpy()
    node = Nodo(Companero(matrix[0][0], matrix[0][1], matrix[0][2], matrix[0][3]))
    aux = node
    cont = 0
    cont2 = 1

    for j in range(1, len(matrix)):
        node.siguiente = Nodo(Companero(matrix[cont2][cont], matrix[cont2][cont + 1],
                                        matrix[cont2][cont + 2], matrix[cont2][cont + 3]))
        node = node.siguiente
        cont2 += 1
    return aux


def main():
    archivo = readFile('Compañeros.csv')
    data = convertToSingleLinkedList(archivo)
    printData(data)


if __name__ == '__main__':
    main()
