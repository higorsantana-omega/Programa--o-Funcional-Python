from math import sqrt

# Map é uma função para cada elemento

lista1 = [1, 4, 9]
lista2 = map(sqrt, lista1)
print(list(lista2))

# sem map

lista2 = (sqrt(x) for x in lista1)
print(list(lista2))