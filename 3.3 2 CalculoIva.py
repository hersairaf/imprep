def calculoIva(valor):
    iva = round(valor * 19 / 100) #línea ? 1
    return iva

def bruto(valor):
    iva = calculoIva(valor) #línea ? 2
    bruto = valor + iva
    return bruto

def descuento(neto, porcentaje):
    total = neto - round(neto * porcentaje / 100) #línea ? 3
    return total

print()
neto = int(input("Ingrese el total de la compra: "))
porcentajeDescuento = int(input("Ingrese el total del descuento: "))
print()
print(f"Total neto: {neto}")
conDescuento = descuento(neto, porcentajeDescuento)
print(f"Total con descuento: {conDescuento}")
print(f"Impuesto: {calculoIva(conDescuento)}")
print(f"Total bruto: {bruto(conDescuento)}")
print()