#FUNCIONES:
#---OPCION 1
def guardar_objeto(mochila):
    while True:
        nombre = input("Ingrese el nombre del objeto mágico a guardar: ").strip()
        if nombre == "":
            print("\nError: el nombre no puede estar vacío.\n")
        else:
            break
    
    while True:
        try:
            posicion = int(input(f"Ingresa la posición en la que desea guardar el objeto mágico (0/{len(mochila)-1}): "))
            if mochila[posicion] != 0:
                print("Error, el espacio indicado ya se encuentra ocupado. ")
                continue
            try:
                mochila[posicion] = nombre
                print("El objeto mágico se guardó correctamente. ")
                break
            except IndexError:
                print("\nError: la posición indicada no existe en la mochila. \n")
        except ValueError:
            print("Error: la posición debe ser indicada con un número entero. ")

#---OPCION 2
def ver_mochila(mochila):
    if all(x == 0 for x in mochila):
        print("\n--- MOCHILA VACÍA ---\n")
    else:
        print("\n--- CONTENIDO DE LA MOCHILA ---")
        for i, objeto in enumerate(mochila):
            if objeto == 0:
                print(f"Espacio {i}: --- vacío ---")
            else:
                print(f"Espacio {i}: {objeto}")



#---CREACION MOCHILA
while True:
    try:
        espacio_mochila = int(input("Ingresa la cantidad de espacios que desea tener en su mochila: "))
        break
    except ValueError:
        print("\nError: debe indicar la cantidad con un número entero.\n")
mochila = list()
for i in range(espacio_mochila):
    mochila.append(0)
print(mochila)
#---MENU
while True:
    print("\n------ MENU ------\n1. Guardar objeto\n2. Ver mochila\n3. Salir\n")
    try:
        opcion = int(input("Ingrese la opción que desee: "))
        if not (1<= opcion <=3):
            print("Error: debe indicar la opción con un número entre 1 y 3. ")
            continue
    except ValueError:
        print("Error: debe indicar la opcion con el número que corresponda a la opción deseada. ")
        continue

    match opcion:
        case 1:
            print("\nOPCIÓN 1: \n")
            guardar_objeto(mochila)
        case 2:
            print("\nOPCIÓN 2: \n")
            ver_mochila(mochila)
        case 3:
            print("Saliendo...")
            break

