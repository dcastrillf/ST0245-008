def negativos(lista):
    resul = []
    for elem in lista:
        if elem < 0:
            resul.append(elem)
    return resul


n = int(input("Cuantos elementos va a ingresar: "))
lista1 = []
for i in range(n):
    x = int(input("Numero: "))
    lista1.append(x)

lista2 = negativos(lista1)
print(lista2)
