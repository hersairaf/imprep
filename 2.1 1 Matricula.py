import os

rut = input("Ingrese rut apoderado: ")
nomAlum = input("Ingrese el nombre del alumno: ")
curso = input("Ingrese curso al cual el alumno debe matricularse: ")
matricula = int(25000)
mensualidad = int(30000)
resultadoAnual = (mensualidad*10)+matricula
os.system("cls")

print(f"NOMBRE ALUMNO: {nomAlum}")
print(f"RUT APODERADO: {rut}")
print(f"CURSO MATRICULADO: {curso}")

print(f"-----Detalle Anualidad Colegio-----")
print(f"VALOR MATRÍCULA: {matricula}")
print(f"VALOR MENSUALIDAD: {mensualidad}")
print(f"VALOR TOTAL A PAGAR: {resultadoAnual}")


