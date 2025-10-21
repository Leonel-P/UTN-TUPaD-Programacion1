# 1. Crear archivo inicial con productos
with open('productos.txt', 'w') as archivo:
    archivo.write("Lapicera,120.5,30\n")
    archivo.write("Cuaderno,250.0,50\n")
    archivo.write("Mochila,3500.0,10\n")

# 2 y 4. Leer y mostrar productos, y cargar en lista de diccionarios
productos = []

with open('productos.txt','r') as archivo:
    for linea in archivo:
        nombre, precio, cantidad = linea.strip().split(',')
        producto = {
            "nombre": nombre,
            "precio": float(precio),
            "cantidad": int(cantidad)
        }
        productos.append(producto)

print("\n--- Lista de Productos ---")
for p in productos:
    print(f"Producto: {p['nombre']} | Precio: ${p['precio']} | Cantidad: {p['cantidad']}")
print("--------------------------\n")

# 3. Agregar productos desde teclado
while True:
    try:
        cantidad_nueva = int(input("Ingrese la cantidad de productos que desea agregar: "))
        break
    except ValueError:
        print("Error, debe ingresar un numero valido.")

with open('productos.txt','a') as archivo:
    for i in range(cantidad_nueva):
        nombre = input(f"Ingrese nombre del producto {i+1}/{cantidad_nueva}: ")
        while True:
            try:
                precio = float(input(f"Ingrese precio del producto {i+1}/{cantidad_nueva}: "))
                break
            except ValueError:
                print("Error, debe ingresar un numero valido para el precio.")
        while True:
            try:
                stock = int(input(f"Ingrese cantidad en stock del producto {i+1}/{cantidad_nueva}: "))
                break
            except ValueError:
                print("Error, debe ingresar un numero entero para la cantidad.")

        archivo.write(f"{nombre},{precio},{stock}\n")
        productos.append({"nombre": nombre, "precio": precio, "cantidad": stock})

print("\nProductos agregados correctamente.\n")

# 5. Buscar producto por nombre
busqueda = input("Ingrese el nombre del producto a buscar: ").lower()
encontrado = False
for p in productos:
    if p['nombre'].lower() == busqueda:
        print(f"Producto encontrado: {p['nombre']} | Precio: ${p['precio']} | Cantidad: {p['cantidad']}")
        encontrado = True
        break

if not encontrado:
    print("Error: producto no encontrado.")

# 6. Guardar productos actualizados (sobrescribir archivo)
with open('productos.txt','w') as archivo:
    for p in productos:
        archivo.write(f"{p['nombre']},{p['precio']},{p['cantidad']}\n")

print("\nArchivo actualizado con los productos actuales.")