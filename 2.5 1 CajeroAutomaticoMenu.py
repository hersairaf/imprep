#Cajero automático
sw = 1
while sw == 1:
    print("1. Ver mi saldo")
    print("2. Retirar dinero")
    print("3. Salir")
    op = int(input("Seleccione una opción: "))
    try:
        if (op > 0 and op < 4):
            if op == 1:
                print("Tiene un saldo de $500.000")
                continu = int(input("Presione 1) para volver atrás, presione 2) para salir"))
                if continu == 2:
                    print("Cierre de sesión exitoso, adiós")
                    sw = 0
            if op == 2:
                print("Transferencia realizada")
                continu = int(input("Presione 1) para volver atrás, presione 2) para salir"))
                if continu == 2:
                    print("Cierre de sesión exitoso, adios")
                    sw = 0
            if op == 3:
                print("Cierre de sesión exitoso, adios")
                sw = 0
        else:
            print("Selección fuera de rango")
    except:
        print("Ingreso erróneo")