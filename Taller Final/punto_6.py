# Punto 6

from random import randint


class Node:
    def __init__(self, dato):
        self.left = None
        self.right = None
        self.dato = dato

    def height(self):
        return 1 + max(self.left.height() if self.left is not None else 0,
                       self.right.height() if self.right is not None else 0)


class Arbol:
    def __init__(self):
        self.root = None

    def insert(self, a, dato):
        if a is None:
            a = Node(dato)
        else:
            d = a.dato
            if dato < d:
                a.left = self.insert(a.left, dato)
            else:
                a.right = self.insert(a.right, dato)
        return a

    def buscar(self, dato, a):
        if a is None:
            return None
        else:
            if dato == a.dato:
                return a.dato
            else:
                if dato < a.dato:
                    return self.buscar(dato, a.left)
                else:
                    return self.buscar(dato, a.right)

    def preorder(self, a):
        if a is None:
            return None
        else:
            print(a.dato)
            self.preorder(a.left)
            self.preorder(a.right)


def main():
    tree = Arbol()
    print('... Ingreando datos aleatorios ...', '\n')
    for i in range(1, 11):
        nodo = randint(1, 51)
        if tree.buscar(int(nodo), tree.root) is None:
            tree.root = tree.insert(tree.root, nodo)
    print('Arbol generado en su recorrido preorder:')
    tree.preorder(tree.root)
    print('---------------------')
    print('Su altura es: ', tree.root.height(), sep='')


if __name__ == '__main__':
    main()
