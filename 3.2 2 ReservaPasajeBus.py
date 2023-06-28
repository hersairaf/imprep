#Reserva pasaje bus
sw = 1
listaAsiento = [1,2,3,4,5,6,7,8,9,10]
listaAsientoReservado = []

print("Presione 1 para reservar su pasaje de bus")
print("Presione cualquier tecla para salir")
op=int(input("Seleccione opción"))
if (op == 1):
    while sw == 1:
        try:
            print("-------------------------------------------------------")
            print(f"Los asientos disponibles son: {listaAsiento}")
            asiento=int(input("Ingrese el número del asiento a reservar o presione 0 para salir: "))
            if (asiento != 0):
                listaAsiento.remove(asiento)
                listaAsientoReservado.append(asiento)
                print(f"Asiento {asiento} reservado, quedan disponibles: {listaAsiento}")
            else:
                print(f"Los asientos reservados son: {listaAsientoReservado} Muchas gracias")
                sw = 0
        except:
            print("Ingreso erróneo")
else:
    print("Adiós")
