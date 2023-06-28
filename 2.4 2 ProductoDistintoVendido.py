contador = 0
total = 0

print("")
productosDistintos = int(input("Ingrese el número de productos distintos vendidos: ")) 
productosVendidos = int(input("Ingrese el número de productos vendidos en total: ")) 

while contador < productosDistintos:
    contador = contador + 1
    print(f"Ingrese precio del producto {contador}:")
    precio = float(input())
    print(f"Ingrese el número de unidades vendidas del producto {contador}: ")
    porcentaje = float(input())
    total = total + (precio*porcentaje/productosVendidos)
print("")
print("El precio promedio ponderado fue de: {:,}".format(total))
print("")
