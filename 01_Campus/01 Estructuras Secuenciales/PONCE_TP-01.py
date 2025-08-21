#Ejercicio 1
print("Hola Mundo!")

#Ejercicio 2
nombre = input("A continuación, ingrese su nombre: ")
print(f"Hola {nombre}!")

#Ejercicio 3
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
lugar_residencia = input("Por último, ingrese su lugar de residencia: ")
print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {lugar_residencia}")

#Ejercicio 4
radio = float(input("Para calcular el área y el perímetro del círculo, ingrese el radio: "))
PI = 3.14
area = PI * (radio**2)
perimetro = 2 * PI * radio
print(f"El área es de: {area}, mientras que su perímetro es de: {perimetro}")

#Ejercicio 5
seg = int(input("A continuación, ingrese una cantidad de segundos: "))
horas = seg / 3600
print(f"{seg} segundos equivalen a: {horas} horas")

#Ejercicio 6
num = int(input("Ingrese un número para mostrar por pantalla la tabla de multiplicar de dicho número: "))
print(f"{num} x 1 = {num}")
print(f"{num} x 2 = {num * 2}")
print(f"{num} x 3 = {num * 3}")
print(f"{num} x 4 = {num * 4}")
print(f"{num} x 5 = {num * 5}")
print(f"{num} x 6 = {num * 6}")
print(f"{num} x 7 = {num * 7}")
print(f"{num} x 8 = {num * 8}")
print(f"{num} x 9 = {num * 9}")
print(f"{num} x 10 = {num * 10}")

#Ejercicio 7
numero_1 = int(input("Ingrese un número distinto al cero: "))
numero_2 = int(input("Ingrese un último número distinto al cero: "))
suma = numero_1 + numero_2
resta = numero_1 - numero_2
division = numero_1 / numero_2
multiplicacion = numero_1 * numero_2
print("A continuación se muestran las operaciones correspondientes: ")
print(f"Suma: {suma}")
print(f"Resta: {resta}")
print(f"División: {division}")
print(f"Multiplicación: {multiplicacion}")

#Ejercicio 8
peso = float(input("A continuación ingrese su peso en 'KG': "))
altura = float(input("Por último, ingrese su altura en metros: "))
imc = peso / (altura**2)
print(f"Su índice de masa corporal actualmente es: {imc}")

#Ejercicio 9
grados_celsius = float(input("Ingrese una temperatura en grados Celsius para luego pasarla a Fahrenheit: "))
fahrenheit = 9/5 * grados_celsius + 32
print(f"{grados_celsius}°C equivalen a {fahrenheit}°F")

#Ejercicio 10
num_1 = int(input("Para calcular un promedio, ingrese el primer número: "))
num_2 = int(input("Ingrese el segundo número: "))
num_3 = int(input("Por último, ingrese el tercer número: "))
promedio = (num_1 + num_2 + num_3) / 3
print(f"El promedio calculado fue: {promedio}")