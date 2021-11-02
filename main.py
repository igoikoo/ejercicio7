lista = []
while True:
    nombre = input("Nombre: ")
    if nombre != "fin":
        telefono = input("Telefono: ")
        linea = {}
        linea["Nombre"] = nombre
        linea["Telefono"] = telefono
        lista.append(linea)
        continue
    break
print("Lista nombre:\n",lista)
