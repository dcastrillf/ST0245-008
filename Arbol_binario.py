"""
 Se solucionó el problema de ingresar un nodo que ya estaba.
 Sobre el borrado perdoneme profe :c no tuve mucho tiempo
 Desde el viernes y me tocó el domingo y no fui capaz. Me intenté
 Ayudar de una pagina pero no le entendí bien :C
"""

import os


class Node:
    def __init__(self, dato):
        self.left = None
        self.right = None
        self.dato = dato


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

    def inorder(self, a):
        if a is None:
            return None
        else:
            self.inorder(a.left)
            print(a.dato)
            self.inorder(a.right)

    def preorder(self, a):
        if a is None:
            return None
        else:
            print(a.dato)
            self.preorder(a.left)
            self.preorder(a.right)

    def postorder(self, a):
        if a is None:
            return None
        else:
            self.postorder(a.left)
            self.postorder(a.right)
            print(a.dato)

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

    def retornar_nodo(self, dato, a):
        if a is None:
            return None
        else:
            if dato == a.dato:
                return a
            else:
                if dato < a.dato:
                    return self.retornar_nodo(dato, a.left)
                else:
                    return self.retornar_nodo(dato, a.right)

    def min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def delete_node(self, a, dato):
        if a is None:
            return a
        if int(dato) < int(a.dato):
            a.left = self.delete_node(a.left, dato)
        elif int(dato) < int(a.dato):
            a.right = self.delete_node(a.right, dato)
        else:
            if a.left is None:
                temp = a.right
                a = None
                return temp
            elif a.right is None:
                temp = a.left
                a = None
                return temp
            temp = self.min_value_node(a.right)
            a.dato = temp.dato
            a.right = self.delete_node(a.right, temp.dato)
        return a


tree = Arbol()

while True:
    os.system("cls")
    print("Arbol ABB")
    opc = input("\n1.-Insertar nodo \n2.-Inorden \n3.-Preorden \n4.-Postorden \n5.-Buscar \n6.-Salir \n7.-Eliminar nodo \n\nElige una opcion -> ")
    if opc == '1':
        nodo = input("\nIngresa el nodo -> ")
        if tree.buscar(int(nodo), tree.root) is None:
            if nodo.isdigit():
                nodo = int(nodo)
                tree.root = tree.insert(tree.root, nodo)
            else:
                print("\nIngresa solo digitos...")
        else:
            print("Ya existe ese nodo")
    elif opc == '2':
        if tree.root is None:
            print("Vacio")
        else:
            tree.inorder(tree.root)
    elif opc == '3':
        if tree.root is None:
            print("Vacio")
        else:
            tree.preorder(tree.root)
    elif opc == '4':
        if tree.root is None:
            print("Vacio")
        else:
            tree.postorder(tree.root)
    elif opc == '5':
        nodo = input("\nIngresa el nodo a buscar -> ")
        if nodo.isdigit():
            nodo = int(nodo)
            if tree.buscar(nodo, tree.root) is None:
                print("\nNodo no encontrado...")
            else:
                print("\nNodo encontrado -> ", tree.buscar(nodo, tree.root), " si existe...")
        else:
            print("\nIngresa solo digitos...")
    elif opc == '6':
        print("\nElegiste salir...\n")
        os.system("pause")
        break
    elif opc == '7':
        nodo = input("\nIngresa el nodo -> ")
        tree.delete_node(tree.root, nodo)
    else:
        print("\nElige una opcion correcta...")
    print()
    os.system("pause")

print()
