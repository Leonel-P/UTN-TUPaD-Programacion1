
titulos = []
ejemplares = []

opcion = 0

while opcion != 9:
    print("===== MENÚ BIBLIOTECA =====")
    print("1. Ingresar lista de títulos")
    print("2. Ingresar lista de ejemplares disponibles")
    print("3. Mostrar catálogo con stock")
    print("4. Consultar disponibilidad de un título")
    print("5. Listar títulos agotados")
    print("6. Agregar nuevo título")
    print("7. Actualizar ejemplares (préstamo/devolución)")
    print("8. Ver catálogo completo")
    print("9. Salir")

    entrada = input("Seleccione una opción: ")

    if not entrada.isdigit():
        print("Error: ingrese un número válido.")
        continue
    opcion = int(entrada)

    # 1. Ingresar lista de títulos
    if opcion == 1:
        cantidad = input("¿Cuántos títulos desea ingresar?: ")
        if not cantidad.isdigit():
            print("Error: debe ingresar un número entero.")
            continue
        cantidad = int(cantidad)
        for i in range(cantidad):
            titulo = input(f"Ingrese título {i+1}: ").strip()
            if titulo == "":
                print("Error: el título no puede estar vacío.")
                continue
            if titulo in titulos:
                print(f"El título '{titulo}' ya existe. No se agregó.")
            else:
                titulos.append(titulo)
                ejemplares.append(0)  # por defecto 0 ejemplares

    # 2. Ingresar lista de ejemplares
    elif opcion == 2:
        if len(titulos) == 0:
            print("No hay títulos en el catálogo.")
        else:
            for i in range(len(titulos)):
                cantidad = input(f"Ingrese cantidad de ejemplares para '{titulos[i]}': ")
                if cantidad.isdigit():
                    ejemplares[i] = int(cantidad)
                else:
                    print("Error: debe ingresar un número entero. Se dejó en 0.")

    # 3. Mostrar catálogo con stock
    elif opcion == 3:
        if len(titulos) == 0:
            print("No hay títulos cargados.")
        else:
            for i in range(len(titulos)):
                print(f"{titulos[i]}: {ejemplares[i]} copias")

    # 4. Consultar disponibilidad de un título
    elif opcion == 4:
        buscar = input("Ingrese el título a consultar: ").strip()
        if buscar in titulos:
            indice = titulos.index(buscar)
            print(f"'{buscar}': {ejemplares[indice]} copias disponibles")
        else:
            print("Título no encontrado.")

    # 5. Listar títulos agotados
    elif opcion == 5:
        agotados = False
        for i in range(len(titulos)):
            if ejemplares[i] == 0:
                print(f"'{titulos[i]}' está agotado")
                agotados = True
        if not agotados:
            print("No hay títulos agotados.")

    # 6. Agregar nuevo título
    elif opcion == 6:
        nuevo = input("Ingrese el nuevo título: ").strip()
        if nuevo == "":
            print("Error: el título no puede estar vacío.")
        elif nuevo in titulos:
            print("El título ya existe en el catálogo.")
        else:
            cant = input(f"Ingrese la cantidad de ejemplares de '{nuevo}': ")
            if cant.isdigit():
                titulos.append(nuevo)
                ejemplares.append(int(cant))
                print(f"'{nuevo}' agregado con {cant} ejemplares.")
            else:
                print("Error: cantidad inválida.")

    # 7. Actualizar ejemplares (préstamo / devolución)
    elif opcion == 7:
        titulo = input("Ingrese el título a actualizar: ").strip()
        if titulo in titulos:
            indice = titulos.index(titulo)
            print("1. Registrar préstamo")
            print("2. Registrar devolución")
            accion = input("Seleccione: ")

            if accion == "1":
                cant = input("¿Cuántos ejemplares desea prestar?: ")
                if cant.isdigit():
                    cant = int(cant)
                    if cant <= ejemplares[indice] and cant > 0:
                        ejemplares[indice] -= cant
                        print(f"Se prestaron {cant} ejemplares de '{titulo}'.")
                    else:
                        print("Error: cantidad inválida o stock insuficiente.")
                else:
                    print("Error: ingrese un número válido.")

            elif accion == "2":
                cant = input("¿Cuántos ejemplares desea devolver?: ")
                if cant.isdigit():
                    cant = int(cant)
                    if cant >= 1:
                        ejemplares[indice] += cant
                        print(f"Se devolvieron {cant} ejemplares de '{titulo}'.")
                    else:
                        print("Error: debe devolver al menos 1.")
                else:
                    print("Error: ingrese un número válido.")
            else:
                print("Opción inválida.")
        else:
            print("El título no existe en el catálogo.")

    # 8. Ver catálogo completo
    elif opcion == 8:
        print("===== CATÁLOGO COMPLETO =====")
        if len(titulos) == 0:
            print("No hay libros registrados.")
        else:
            for i in range(len(titulos)):
                print(f"{titulos[i]}: {ejemplares[i]} ejemplares")

    # 9. Salir
    elif opcion == 9:
        print("Saliendo")
    else:
        print("Opción inválida.")
