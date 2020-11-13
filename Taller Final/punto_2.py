from random import randint


# Punto 2
stack = []  # Se crea la pila
for i in range(11):
    stack.append(randint(0, 101))  # Se ingresan valores aleatorios a la pila

average = 0  # Se crea una variable la cual será el resultado de el promedio
long = 0  # Se crea un contador que nos dira cuantos datos tiene la pila ya que si usamos el metodo len es como si lo recorrieramos nuevamente

for i in stack:  # Se recorre la pila y se va sumando a la variable cada dato en esta
    average += i
    long += 1

average = average/long  # A la suma anterior se le divide por la cantidad de datos que tiene la pila

print(stack)
print(average)
