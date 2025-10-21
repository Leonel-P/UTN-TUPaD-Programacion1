#Ejercicio 1
print('Ejercicio 1: \n')

precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 
1450} 
print(f'\nDiccionario original: {precios_frutas}')
precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300
print(f'\nDiccionario modificado: {precios_frutas}')

#Ejercicio 2
print('\nEjercicio 2: \n')
print('Modificacion de precios en "Banana", "Manzana", y "Melon": \n')
precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melon'] = 2800
print(precios_frutas)

#Ejercicio 3
print('\nEjercicio 3: \n')
print('Creamos una lista con los nombres de las frutas (claves): \n')
lista_precios_frutas = list(precios_frutas.keys())
print(lista_precios_frutas)

#Ejercicio 4
print('\nEjercicio 4: \n')

numeros_telefonos = {}
for i in range(5):
    while True:
        nombre = input('Ingrese el nombre: ').lower()
        if nombre.isdigit() :
            print('El nombre del contacto no puede ser un numero. ')
        elif nombre in numeros_telefonos:
            print('El nombre del contacto ya se encuentra agendado. Por favor, intente con otro nombre. ')
        else:
            break
    while True:
        try:
            numero = int(input('Ingrese el numero de telefono: '))
            if numero in numeros_telefonos.values():
                print('El numero ya se encuentra agendado.')
            else:
                break
        except ValueError:
            print('El formato del numero no es correcto.')
            continue
    numeros_telefonos[nombre] = numero
print('\nLISTA DE CONTACTOS :\n')
for nombre, numero in numeros_telefonos.items():
    print(f'-{nombre.capitalize()}:{numero}')
#busqueda
nombre_buscado = input('Ingrese el nombre que desea buscar: ').lower()
if nombre_buscado in numeros_telefonos:
    print(numeros_telefonos[nombre_buscado])
else:
    print('El nombre no se encuentra agendado. ')

#Ejercicio 5
print('\nEjercicio 5: \n')

recuento = {}

frase = input('Ingrese una frase: ').lower()

palabras = frase.split()
palabras_unicas = set(palabras)
print(palabras_unicas)

contador = {}
for palabra in palabras:
    contador[palabra] = contador.get(palabra, 0) + 1
print(contador)

#Ejercicio 6
print('\nEjercicio 6: \n')

print('\nEjercicio 6: \n')

alumnos = {}

for i in range(3):
    nombre = input(f'Ingrese el nombre del alumno ({i+1}/3): ')
    notas = []
    for j in range(3):
        while True:
            try:
                nota = float(input(f'Ingrese la nota {j+1} de {nombre}: '))
                if 0 <= nota <= 10:
                    notas.append(nota)
                    break
                else:
                    print('La nota debe estar entre 0 y 10.')
            except ValueError:
                print('Error: debe ingresar un número válido.')
    
    alumnos[nombre] = tuple(notas)

# Mostrar los promedios
print("\nPromedios de los alumnos:")
for nombre, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"{nombre}: {promedio:.2f}")



#Ejercicio 7
print('\nEjercicio 7: \n')

parcial1 = {"Ana", "Luis", "Leonel", "Ian"}
parcial2 = {"Leonel", "Ian", "Pedro", "Camila"}

#Aprobaron ambos parciales
ambos = parcial1 & parcial2
print("Aprobaron ambos parciales:", ambos)

#Aprobaron solo un parcial
solo_uno = parcial1 ^ parcial2
print("Aprobaron solo uno de los parciales:", solo_uno)

#Aprobaron al menos un parcial
al_menos_uno = parcial1 | parcial2
print("Aprobaron al menos un parcial:", al_menos_uno)

#Ejercicio 8
print('\nEjercicio 8: \n')

stock = {
    'gaseosa' : 2,
    'alfajor' : 8,
    'caramelos' : 30,
    'chocolate' : 10,
}

print('--- MENU ---\n')
print('1. Consultar Stock De Un Producto\n2. Agregar unidades al stock.\n3. Agregar un nuevo producto. ')
while True:
    try:
        opcion = int(input("Ingrese una opcion: "))
        if 1<= opcion <= 3:
            break
        else:
            print("La opcion indicada no existe. ")
    except ValueError:
        print("Error, la opcion debe ser indicada con un numero. ")

match opcion:
    case 1:
        print(stock)
        producto = input('Ingrese el nombre de un producto para consultar su stock: ')
        if producto in stock: 
            print(stock[producto])
        else:
            print('El producto ingresado no se encuentra cargado. ')
    case 2: 
        print(stock)
        producto = input('Ingrese el nombre del producto para modificar su stock: ').lower()
        if producto in stock :
            while True:
                try:
                    cantidad = int(input('Ingrese la cantidad que desea agregar al stock: '))
                    break
                except ValueError:
                    print('Error, la cantidad debe ser indicada con numero entero. ')
            stock[producto] += cantidad
        else:
            print('El producto ingresado no se encuentra cargado en el sistema. ')
    case 3:
        producto = input('Ingesa el nombre del producto que desea agreagar al stock: ').lower()
        if producto in stock: 
            print('El producto ya se encuentra cargado. ')
        else: 
            stock[producto] = 0
            print('Producto cargado exitosamente.')

#Ejercicio 9
print('\nEjercicio 9: \n')
agenda = {
    ('lunes', '12:00'): 'Clase de programacion',
    ('martes','10:00'): 'Clase de ingles',
    ('miercoles', '9:00'): 'Clase de organizacion empresarial',
    ('jueves', '10:00'): 'Clase de arquitectura de sistemas',
    ('viernes', '8:00'): 'Clase de programacion'
}
print(agenda)

dia = input('Ingresa el dia: ')
hora = input('Ingresa la hora: ')

fecha = (dia, hora)
if fecha not in agenda :
    print('No hay ningun evento para la fecha y hora indicada. ')
else:
    print(agenda[(fecha)])

#Ejercicio 10
print('\nEjercicio 10: \n')

paises = {
    'Argentina': 'Buenos Aires',
    'Brasil': 'Brasilia',
    'Francia': 'Paris',
    "Italia": 'Roma'
}

print(f'Diccionario original: {paises}')
capitales = {}

for pais, capital in paises.items():
    capitales[capital] = pais
print(f'Diccionario invertido: {capitales}')

