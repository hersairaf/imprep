#Puntos acumulados
sw = 1
puntos = 100000
while sw == 1:
    print("1.- Ver mis puntos")
    print("2.- Gastar mis puntos")
    print("3.- Salir")
    op = int(input("Seleccione una opción: "))
    try:
        if(op > 0 and op < 4):
            if op == 1:
                print(f"Tiene un total de {puntos} puntos")
                continu = int(input("Presione 1) para volver atrás, presione 2) para salir "))
                if continu == 2:
                    print("Cierre de sesión exitoso")
                    sw=0
            if op == 2:
                if(puntos >= 10000):
                    print("Seleccione el producto a canjear")
                    print("1.- Gift Card de $10.000, valor de 10.000 puntos")
                    print("2.- Secador de pelo, valor de 25.000 puntos")
                    print("3.- Disco duro portátil, valor de 30.000 puntos")
                    continu = int(input("Seleccione la opción: "))
                    if continu == 1:
                        puntos = puntos - 10000
                        print(f"Canje exitoso, le quedan: ${puntos} puntos")
                    if continu == 2:
                        puntos = puntos - 25000
                        print(f"Canje exitoso, le quedan: ${puntos} puntos")
                    if continu == 3:
                        puntos = puntos - 30000
                        print(f"Canje exitoso, le quedan: ${puntos} puntos")
                else:
                    print("No le quedan puntos disponibles")
            if op == 3:
                print("Muchas gracias por ocupar el servicio, adiós")
                sw=0
        else:
            print("Selección fuera de rango")
    except:
        print("Ingreso erróneo")