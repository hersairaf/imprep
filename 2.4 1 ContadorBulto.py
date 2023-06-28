tieneMasBultos = True #Estaba en False
nroBulto = 1
valorPagarPorKilo = 0

valorPesoLiviano = 1000
valoPesoNormal = 4500

totalLiviano = 0
totalNormal = 0

contadorBultosLivianos = 0
contadorBultosNormales = 0

while tieneMasBultos:
    print("\nIngrese 0 para terminar...")
    try:
        pesoBulto = int(input(f"Ingrese el peso (1 a 10kg del bulto Nro. {nroBulto} :"))
    except:
        print("Peso del bulto debe estar en el rango de 1 y 10kg. Pulse 0 para terminar y pagar")
        continue
    if pesoBulto == 0:
        break
    else:
        if pesoBulto >= 1 and pesoBulto <= 5:
            totalLiviano = totalLiviano + valorPesoLiviano
            contadorBultosLivianos = contadorBultosLivianos + 1 #Se había elimiado esta línea en el quiz
            #...
        elif pesoBulto >= 6 and pesoBulto <= 10:
            totalNormal = totalNormal + valoPesoNormal
            contadorBultosNormales = contadorBultosNormales + 1
        else:
            print("Peso ingresado incorrecto ( 1 - 10kg )")
    nroBulto - nroBulto +1
print(f"{contadorBultosLivianos} bulto(s) Liviano(s): $", totalLiviano)
print(f"{contadorBultosNormales} bulto(s) Normal(es): $", totalNormal)
print(f"Valor total a pagar ${totalLiviano + totalNormal} ")