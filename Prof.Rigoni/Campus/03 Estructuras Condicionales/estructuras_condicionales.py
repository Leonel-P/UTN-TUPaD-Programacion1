#---------- Ejercicio 1
print("Ejercicio 1: ")
edad = int(input("Ingrese su edad: "))
if edad >= 18 :
    print("Es mayor de edad.")
print("")
#---------- Ejercicio 2
print("Ejercicio 2: ")
nota = int(input("Ingrese su nota: "))
if nota >= 6 :
    print("Aprobado.")
else:
    print("Desaprobado.")

#---------- Ejercicio 3
print("Ejercicio 3: ")
num = int(input("Ingrese un numero par: "))
if (num % 2) == 0 :
    print("Ha ingresado un numero par.")
else:
    print("Por favor, ingrese un numero par.")
print("")
#----------- Ejercicio 4
print("Ejercicio 4: ")
categoria = None
edad = int(input("Ingrese su edad: "))
if edad < 12 :
    categoria = "niño/a"
elif edad >=12 and edad < 18 :
    categoria = "Adolescente"
elif edad >= 18 and edad < 30 :
    categoria = "Adulto/a joven"
else:
    categoria = "Adulto"

print(f"Categoria: {categoria}")
print("")
#---------- Ejercicio 5
print("Ejercicio 5: ")
contrasena = input("Ingresa una contrasenia de entre 8 y 14 caracteres: ")
caracteres = len(contrasena)
if caracteres >= 8 and caracteres <= 14 :
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")
print("")
#---------- Ejercicio 6
print("Ejercicio 6: ")
import random
from statistics import mean, median, mode

numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

media = mean(numeros_aleatorios)
mediana = median(numeros_aleatorios)
moda = mode(numeros_aleatorios)

print("Lista de números:", numeros_aleatorios)
print("Media:", media)
print("Mediana:", mediana)
print("Moda:", moda)

if media > mediana > moda:
    print("La distribución tiene sesgo positivo.")
elif media < mediana < moda:
    print("La distribución tiene sesgo negativo.")
elif media == mediana == moda:
    print("La distribución no tiene sesgo.")
else:
    print("Los valores no cumplen con ninguno de los criterios.")
print("")
#---------- Ejercicio 7
print("Ejercicio 7: ")
vocales=["a","e","i","o","u","á","é","í","ó","ú"]
frase = input("Ingrese una palabra o una frase: ")
ult_letra = frase[-1].lower()

if ult_letra in vocales :
    print(frase,"!")
else: 
    print(frase)
print("")
#---------- Ejercicio 8
print("Ejercicio 8: ")

nombre = input("Ingrese su nombre: ")
print("1. Si quiere su nombre en mayúsculas.")
print("2. Si quiere su nombre en minúscula.")
print("3. Si quiere su nombre con la primera letra mayúscula.")
opcion = int(input("Ingrese la opción que desee: "))

if opcion == 1:
    print(nombre.upper())
elif opcion == 2:
    print(nombre.lower())
elif opcion == 3:
    print(nombre.title())
else: 
    print("Error, valor ingresado incorrecto.")
print("")
#---------- Ejercicio 9
print("Ejercicio 9:")

# Pedir magnitud del terremoto
magnitud = float(input("Ingrese la magnitud del terremoto: "))

# Clasificar según la escala de Richter
if magnitud < 3:
    print("Muy leve (imperceptible)")
elif 3 <= magnitud < 4:
    print("Leve (ligeramente perceptible)")
elif 4 <= magnitud < 5:
    print("Moderado (sentido por personas, pero generalmente no causa daños)")
elif 5 <= magnitud < 6:
    print("Fuerte (puede causar daños en estructuras débiles)")
elif 6 <= magnitud < 7:
    print("Muy Fuerte (puede causar daños significativos)")
elif magnitud >= 7:
    print("Extremo (puede causar graves daños a gran escala)")
print("")
#---------- Ejercicio 10
print("Ejercicio 10: ")
print("Ejercicio 10:")

# Pedir datos
hemisferio = input("Ingrese su hemisferio (N/S): ").upper()
mes = int(input("Ingrese el mes (1-12): "))
dia = int(input("Ingrese el día (1-31): "))

# Hemisferio Norte
if hemisferio == "N":
    if (mes == 12 and dia >= 21) or (mes == 1) or (mes == 2) or (mes == 3 and dia <= 20):
        print("Invierno")
    elif (mes == 3 and dia >= 21) or (mes == 4) or (mes == 5) or (mes == 6 and dia <= 20):
        print("Primavera")
    elif (mes == 6 and dia >= 21) or (mes == 7) or (mes == 8) or (mes == 9 and dia <= 20):
        print("Verano")
    elif (mes == 9 and dia >= 21) or (mes == 10) or (mes == 11) or (mes == 12 and dia <= 20):
        print("Otoño")
# Hemisferio Sur
elif hemisferio == "S":
    if (mes == 12 and dia >= 21) or (mes == 1) or (mes == 2) or (mes == 3 and dia <= 20):
        print("Verano")
    elif (mes == 3 and dia >= 21) or (mes == 4) or (mes == 5) or (mes == 6 and dia <= 20):
        print("Otoño")
    elif (mes == 6 and dia >= 21) or (mes == 7) or (mes == 8) or (mes == 9 and dia <= 20):
        print("Invierno")
    elif (mes == 9 and dia >= 21) or (mes == 10) or (mes == 11) or (mes == 12 and dia <= 20):
        print("Primavera")
else:
    print("Hemisferio incorrecto")