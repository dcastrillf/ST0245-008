futbolistasTup = [(1, "Casillas"), (15, "Ramos"), (3, "Pique"), (5, "Puyol"), (11, "Capdevila"),
                  (14, "Xabi Alonso"), (16, "Busquets"), (8, "Xavi Hernandez"), (18, "Pedrito"),
                  (6, "Iniesta"), (7, "Villa")]

# Parte a)
futbolistasTup.sort(key=lambda futbolista: futbolista[0])
print(futbolistasTup)

# Parte b)
futbolistasTup.sort(key=lambda futbolista: futbolista[1])
print(futbolistasTup)

# Parte c)
lista1 = [4, 7, 11, 4, 9, 5, 11, 7, 3, 5]
lista2 = [47, 3, 21, 32, 56, 92]
lista3 = [8, 43, 17, 6, 40, 16, 18, 97, 11, 7]

print("")

try:
    lista1.sort(key=lambda x: x[0])
    lista2.sort(key=lambda y: y[0])
    lista3.sort(key=lambda z: z[0])
except Exception as ex:
    print(ex)

try:
    lista1.sort(key=lambda x: x)
    lista2.sort(key=lambda y: y)
    lista3.sort()
except Exception as ex:
    print(ex)

print("")

print(lista1)
print(lista2)
print(lista3)

# Parte d)
mejores_inventos = [("HTC Vive Pro Eye", 100), ("Mookkie", 70), ("Botcare", 87), ("Ovis", 75), ("Google Assistant", 90)]
mejores_inventos.sort(key=lambda x: x[1])
print("")
print(mejores_inventos)