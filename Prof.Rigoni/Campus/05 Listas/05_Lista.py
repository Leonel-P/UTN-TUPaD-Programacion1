#---------- Ejercicio 1
print("Ejercicio 1: ")

lista= list(range(4,101,4))
print(lista)

#---------- Ejercicio 2
print("\nEjercicio 2: ")

lista= [1,2,3,4,5]
print(f"Lista: {lista}")
print(lista[-2])

#---------- Ejercicio 3
print("\nEjercicio 3: ")

lista_vacia=[]
for i in range(3):
    elemento=input("Ingrese una palabra: ")
    lista_vacia.append(elemento)
print(f"Lista:{lista_vacia}")

#---------- Ejercicio 4
print("\nEjercicio 4: ")

lista_animales= ["perro","gato","conejo","pez"]
print(f"Lista original: {lista_animales}")
lista_animales[1]= "loro"
lista_animales[-1]="oso"
print(f"Lista modificada: {lista_animales}")

#---------- Ejercicio 5
print("\nEjercicio 5: ")

print("Primero: 'max(numeros)' busca el mayor de la lista 'numeros'")
print("Segundo: Una vez localizado el mayor de la lista, busca la primera aparicion (en este caso solo hay un 22) y lo elimina")
print("Por ultimo: Muestra por pantalla la lista 'numeros' sin el valor '22'")

#---------- Ejercicio 6
print("\nEjercicio 6: ")
lista_numeros=[]

for i in range(10,31,5):
    lista_numeros.append(i)
print(lista_numeros)
print(f"Primer numero: {lista_numeros[0]}")
print(f"Segundo numero: {lista_numeros[1]}")

#---------- Ejercicio 7
print("\nEjercicio 7: ")

autos=["sedan","polo","suran","gol"]
print(f"Lista original: {autos}")

for i in range(1,3):
    autos[i]= input(f"Ingrese un nuevo valor para la lista en la posicion {i+1}: ")
print(f"Lista modificada: {autos}")

#---------- Ejercicio 8
print("\nEjercicio 8: ")

dobles=[]
dobles.append(5*2)
dobles.append(10*2)
dobles.append(15*2)
print(dobles)

#---------- Ejercicio 9
print("\nEjercicio 9: ")

compras= [["pan","leche"],["arroz","fideos","salsa"],["agua"]]
print(f"Lista original: {compras}")
compras[2].append("jugo")
compras[1][1]="tallarines"
pan=compras[0]
pan.remove("pan")
print(f"Lista modificada: {compras}")

#---------- Ejercicio 10
print("\nEjercicio 10: ")

lista_anidada= [15,True,[25.5,57.9,30.6],False]
print(f"Lista anidada: {lista_anidada}")