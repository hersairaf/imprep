#Validación  user y pass
user = input("Ingrese su user: ")
pwd = input("Ingrese su pass: ")

if user == "duoc" and pwd == "123duoc":
    print("Bienvenido")
else:
    print("Error en contraseña")