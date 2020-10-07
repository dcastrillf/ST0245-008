class Node:
    def __init__(self, elem):
        self.elem = elem
        self.next = None


class SingleLinkedList:
    def __init__(self, this):
        self.this = this

    def insert(self, data, position):
        new_node = Node(data)
        if position == 0:
            new_node.next = self.this
            self.this = new_node
        else:
            current = self.this
            k = 1
            while current.next is not None and k < position:
                current = current.next
                k += 1
            new_node.next = current.next
            current.next = new_node

    def lenght(self):
        current = self.this
        if current is not None:
            cont = 1
            while current is not None:
                cont += 1
                current = current.next
            return cont
        else:
            return 0

    def show(self):
        dato = self.this
        while dato is not None:
            print(dato.elem, end=" ")
            dato = dato.next
        print("")

    def reverse_reto(self, k):
        for j in range(k):
            prev = None
            current = self.this
            aux = self.this
            while current.next is not None:
                prev = current
                current = current.next
            self.this = current
            self.this.next = aux
            prev.next = None


lista = SingleLinkedList(Node(0))
for i in range(1, 6):
    lista.insert(i, i)

lista.show()
v = int(input("Cuantas rotaciones va a hacer: "))
lista.reverse_reto(v)
lista.show()
