import random
vehiculos = []

def grabar():
    rows = int(input("¿Cuántos vehículos desea ingresar?"))
    for i in range(rows):
        vehiculo = {}
        vehiculo["tipo"] = input("Ingrese el tipo de vehículo: ")
        vehiculo["patente"] = input("Ingrese la patente del vehículo: ").lower()
        while len(vehiculo["patente"]) < 6 or len(vehiculo["patente"]) > 6:
            print("La patente ingresada es inválida, inténtelo nuevamente")
            vehiculo["patente"] = input("Ingrese la patente del vehículo: ").lower()
        vehiculo["marca"] = input("Ingrese la marca del vehículo (entre 2 y 15 carácteres): ")
        while len(vehiculo["marca"]) < 2 or len(vehiculo["marca"]) > 15:
            print("La marca ingresada está fuera de rango, inténtelo nuevamente ")
            vehiculo["marca"] = input("Ingrese la marca del vehículo (entre 2 y 15 carácteres): ")
        vehiculo["precio"] = int(input("Ingrese el precio del vehículo (Debe ser superior a $5.000.000): "))
        while vehiculo["precio"] <= 5000000:
            print("El precio del vehículo es muy bajo, inténtelo nuevamente")
            vehiculo["precio"] = int(input("Ingrese el precio del vehículo (Debe ser superior a $5.000.000): "))
        while True:
            multas = []
            tiene_multas = input("¿El vehículo posee multas? (si/no) ").lower()
            if tiene_multas == "si":
                filas = int(input("¿Cuántas multas tiene el vehículo? "))
                for x in range(filas):
                    multa = {}
                    multa["monto"] = int(input(f"Ingrese el valor de la multa #{x+1}: "))
                    multa["fecha"] = input(f"Ingrese la fecha de la multa #{x+1}: ")
                    multas.append(multa)
                vehiculo["multas"] = multas
                break
            elif tiene_multas == "no":
                break
            else:
                print("El valor ingresado no corresponde, inténtelo nuevamente")
        #vehiculo["emision"] = random.randint(1500,3500) 
        #vehiculo["anotacion"] = random.randint(1500,3500)
        vehiculo["fecha"] = input("Ingrese la fecha de registro del vehículo: ")
        vehiculo["duenyo"] = input("Ingrese el nombre del dueño del vehículo: ")
        print(f"Vehículo #{i+1} guardado con éxito")
        vehiculos.append(vehiculo)

def buscar():
    find_pat = input("Ingrese la patente del vehículo que desea buscar: ").lower()
    for vehiculo in vehiculos:
        if vehiculo["patente"] == find_pat:
            print("Información del vehículo")
            print("Tipo de vehículo:", vehiculo["tipo"])
            print("Patente del vehículo:", vehiculo["patente"])
            print("Marca del vehículo:", vehiculo["marca"])
            print("Precio del vehículo:", vehiculo["precio"])
            print("Fecha de registro de vehículo:", vehiculo["fecha"])
            print("Dueño del vehículo:", vehiculo["duenyo"])
            return
    print("La patente especificada no se ha encontrado")
    
def imp_cert():
    precio_multas = random.randint(1500,3500)
    precio_emision = random.randint(1500,3500)
    precio_anotacion = random.randint(1500,3500)
    find_pat1 = input("Ingrese la patente del vehículo que desea buscar: ").lower()
    for vehiculo in vehiculos:
        if vehiculo["patente"] == find_pat1:
            if "multas" in vehiculo and len(vehiculo["multas"]) > 0:
                print("Certificado de Multas",end="\n_____________________\n")
                c = 1
                for z in vehiculo["multas"]:
                    print(f"Monto multa #{c}:", z["monto"])
                    print(f"Fecha multa #{c}:", z["fecha"])
                    c += 1
                print("Dueño del vehículo:", vehiculo["duenyo"])
                print("Patente del vehículo:", vehiculo["patente"])
                print(f"Precio del certificado: ${precio_multas}")
                print("")
            else:
                print("El vehículo no posee multas para hacer un certificado de estas.")
                print("")
            cumple_emision = random.randint(1,2)
            if cumple_emision == 1:
                print("Certificado de Emisión de contaminantes", end="\n__________________________\n")
                print("El vehículo está dentro de los márgenes de la ley")
                print("Dueño del vehículo:", vehiculo["duenyo"])
                print("Patente del vehículo:", vehiculo["patente"])
                print(f"Precio del certificado: ${precio_emision}")
                print("")
            else:
                print("El vehículo no cumple con los requerimientos mínimos para el certificado de emisión de contaminantes")
                print("")
            print("Certificado de anotaciones Vigentes", end="\n__________________________\n")
            print("Dueño del vehículo:", vehiculo["duenyo"])
            print("Patente del vehículo:", vehiculo["patente"])
            print(f"Precio del certificado: ${precio_anotacion}")
            print("")
            return
    print("La patente especificada no se ha encontrado")          
                  
def menu():
    print("Bienvenido a la aplicación de la automotora 'Auto Seguro'")
    while True:
        try:
            print("1.-Grabar Vehículo\n2.-Buscar Vehículo\n3.-Imprimir Certificados\n4.-Salir")
            op = int(input("Seleccione una opción: "))
            if op == 1:
                grabar()
            elif op == 2:
                buscar()
            elif op == 3:
                imp_cert()
            elif op == 4:
                print("Gracias por utilizar mi aplicación\nPrograma hecho por X X\nVersión 1.0.0.1 ")
                break
            else:
                print("Opción no existente, inténtelo nuevamente")
        except ValueError:
            print("El valor ingresado no es aceptable, por favor ingrese números") 

menu()           


#Randint sirve para generar números aleatorios de valor entero, se suele utilizar la función randint()
