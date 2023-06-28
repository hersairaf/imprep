#Promedio de notas
sw = 1
listaNotas = []

print("Presione 1 para ingresar a sus notas")
print("Presione cualquier tecla para salir")
op=int(input("Seleccione opción"))
if(op == 1):
    while sw == 1:
        try:
            print("-----------------------------------------------------")
            nota = int(input("Incorpore su nota, si desea salir, presione 0: ")) #podría cambiarse por float
            if(nota != 0):
                listaNotas.append(nota)
                print(f"Sus notas cargadas son: {listaNotas}")
                print(f"Cantidad de notas cargadas: {len(listaNotas)}")
                print(f"Su promedio de notas es: {sum(listaNotas)/len(listaNotas)}")
            else:
                print("Adiós")
                sw = 0
        except:
            print("Ingreso erróneo")
else:
    print("Adiós")
















