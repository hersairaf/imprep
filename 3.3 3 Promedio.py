import random

def promedio(lista):
    suma = 0
    for numero in lista:
        suma += numero #línea ? 1
    return suma / len (lista)

def maximo(lista):
    max = lista[0]
    for x in lista:
        if x > max: #línea ? 2
            max = x
    return max

def minimo(lista):
    min = lista[0]
    for x in lista:
        if x < min: #línea ? 3
            min = x
    return min

lista = []

for i in range(100):
    aleatorio = random.randint(1000,100000)
    lista.append(aleatorio)

print()
print(lista)
print()
print("Promedio: {:,}".format(promedio(lista)))
print("Máximo: {:,}".format(maximo(lista)))
print("Mínimo: {:,}".format(minimo(lista)))
print()
