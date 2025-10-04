print("Ejercicio 1:\n")
def imprimir_hola_mundo():
    return "Hola Mundo!"

print(imprimir_hola_mundo())

print("\nEjercicio 2:\n")
def saludar_usuario(nombre):
    return f"Hola {nombre}!"

nombre_usuario = input("Ingrese su nombre: ")
print(saludar_usuario(nombre_usuario))

print("\nEjercicio 3:\n")
def informacion_personal(nombre, apellido, edad, residencia):
    return f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}"

nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
residencia = input("Ingrese su lugar de residencia: ")
print(informacion_personal(nombre, apellido, edad, residencia))

print("\nEjercicio 4:\n")
import math
def calcular_area_circulo(radio):
    return math.pi * radio**2

def calcular_perimetro_circulo(radio):
    return 2 * math.pi * radio

radio = float(input("Ingrese el radio de la circunferencia para calcular el area y el perimetro: "))
area = calcular_area_circulo(radio)
perimetro = calcular_perimetro_circulo(radio)
print(f"Área: {area:.2f}\nPerímetro: {perimetro:.2f}")

print("\nEjercicio 5:\n")
def segundos_a_horas(segundos):
    return segundos / 3600

segundos = int(input("Ingrese la cantidad de segundos que desea pasar a horas: "))
print(f"Equivale a {segundos_a_horas(segundos):.2f} horas.")

print("\nEjercicio 6:\n")
def tabla_multiplicar(numero):
    tabla = []
    for i in range(1, 11):
        tabla.append(f"{numero} x {i} = {numero*i}")
    return tabla

numero = int(input("Ingrese un número para ver su tabla de multiplicar: "))
for linea in tabla_multiplicar(numero):
    print(linea)

print("\nEjercicio 7:\n")
def operaciones_basicas(a, b):
    division = a / b if b != 0 else "Indefinida"
    return a+b, a-b, a*b, division

num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
suma, resta, multiplicacion, division = operaciones_basicas(num1, num2)
print(f"{num1} + {num2} = {suma}")
print(f"{num1} - {num2} = {resta}")
print(f"{num1} * {num2} = {multiplicacion}")
print(f"{num1} / {num2} = {division}")

print("\nEjercicio 8:\n")
def calcular_imc(peso, altura):
    return peso / (altura**2)

peso = float(input("Peso (kg): "))
altura = float(input("Altura (m): "))
print(f"IMC: {calcular_imc(peso, altura):.2f}")

print("\nEjercicio 9:\n")
def celsius_a_fahrenheit(celsius):
    return (celsius * 1.8) + 32

celsius = float(input("Ingrese grados Celsius: "))
print(f"{celsius}°C equivalen a {celsius_a_fahrenheit(celsius):.2f}°F")

print("\nEjercicio 10:\n")
def calcular_promedio(a, b, c):
    return (a+b+c)/3

num1 = float(input("Número 1: "))
num2 = float(input("Número 2: "))
num3 = float(input("Número 3: "))
print(f"Promedio: {calcular_promedio(num1, num2, num3):.2f}")