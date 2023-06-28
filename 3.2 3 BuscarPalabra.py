#Buscar palabras
sw = 1
listaPalabra = []

print("Presione 1 para ingresar las palabras ")
print("Presione cualquier tecla para salir ")
op=int(input("Seleccione opción "))
if (op == 1):
    while sw==1:
        try:
            print("--------------------------------------------------------")
            palabra=input("Ingrese su palabra, si desea buscar las palabras ingresadas, presione 0: ")
            if(palabra != "0"):
                listaPalabra.append(palabra)
                print(f"Sus palabras cargadas son: {listaPalabra}")
                print(f"Cantidad de palabras cargadas: {len(listaPalabra)}")
            else:
                buscar = input("Escriba la palabra a buscar: ")
                contador = 0
                for i in listaPalabra:
                    if i == buscar:
                        contador = contador + 1
                if contador == 0:
                    print("No se encuentra la palabra")
                elif contador >= 1:
                    print(f"La palabra {buscar} aparece: {contador} veces")
                sw=0
        except:
            print("Ingreso erróneo")
else:
    print("Adiós")
