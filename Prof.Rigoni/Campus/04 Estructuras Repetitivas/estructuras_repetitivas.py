#---------- Ejercicio 1
print("Ejercicio 1: ")

for i in range(101):
    print(i)

print("")
#---------- Ejercicio 2
print("Ejercicio 2: ")

cant_digitos = 0
num=int(input("Ingrese un numero entero para devolver su longitud: "))
num=str(num)

for i in range(len(num)):
    cant_digitos += 1
print(cant_digitos)

print("")
#---------- Ejercicio 3
print("Ejercicio 3: ")

num_1=int(input("Ingrese el primer numero entero: "))
num_2=int(input("Ingrese el segundo numero entero: "))
suma = 0
for i in range(num_1-1,num_2,1):
    suma += i
print(suma)

print("")

#---------- Ejercicio 4
print("Ejercicio 4: ")

num_sumar=1
num = 0
while num_sumar != 0 :
    num_sumar=int(input("Ingrese un numero para sumar, o ingrese '0' para terminar: "))
    num+= num_sumar

print(f"Total acumulado: {num}")

print("")

#---------- Ejercicio 5
print("Ejercicio 5: ")

import random
intentos= 1
num_aleatorio = random.randint(0,9)
num_usuario = int(input("Adivina el numero aleatorio entre 0 y 9: "))
while num_aleatorio != num_usuario:
    num_usuario= int(input("Numero incorrecto, vuelva a intentarlo: "))
    intentos+= 1
print(f"Acertaste!!!\nIntentos neceasarios: {intentos}")

print("")

#---------- Ejercicio 6
print("Ejercicio 6: ")

for i in range(100,-1,-2):
    print(i)

print("")

#---------- Ejercicio 7
print("Ejercicio 7: ")
suma=0
num_usuario=int(input("Ingrese un numero entero positivo: "))
for i in range(0,num_usuario+1):
    suma+= i
print(f"Resulatado de la suma: {suma}")

print("")

#---------- Ejercicio 8
print("Ejercicio 8: ")

num_defecto= 10
pares = 0
impares = 0
negativos = 0
positivos = 0
for i in range(num_defecto):
    num=int(input(f"Ingrese un numero entero ({i+1}/{num_defecto}): "))
    if num % 2 == 0:
        pares+=1
    else:
        impares+=1
    if num < 0:
        negativos+=1
    elif num > 0: 
        positivos+=1
print(f"Numeros pares ingresados: {pares}")
print(f"Numeros impares ingresados: {impares}")
print(f"Numeros positivos ingresados: {positivos}")
print(f"Numeros negativos ingresados: {negativos}")

print("")

#---------- Ejercicio 9
print("Ejercicio 9: ")

num_defecto= 10
suma= 0
for i in range(num_defecto):
    num=int(input(f"Ingrese {num_defecto} numeros para calcular su media ({i+1}/{num_defecto}): "))
    suma+=num
media= suma / num_defecto
print(f"La media calculada fue: {media}")

print("")

#---------- Ejercicio 10
print("Ejercicio 10: ")

num_original = int(input("Ingrese un numero para invertir su orden: "))
num_string=str(num_original)
num_invertido= ""
for i in num_string:
    num_invertido= i + num_invertido
print(f"Numero invertido: {num_invertido}")