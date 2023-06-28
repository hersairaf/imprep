cola = []
print()
print("Se llena la cola")
for numero in range (1, 11):
    cola.insert(0,numero) 
print(cola)

print()
print("Se atiende a los clientes")
for numero in range (1, 11):
    print(cola.pop(), "Es atendido")

print()
print("Contenido de la cola")
print(cola)
print()