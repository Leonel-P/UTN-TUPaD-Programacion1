from funciones import validar_letra, comprobar_letra
import random

palabras = [
    "boca juniors", "river plate", "independiente rivadavia", "racing",
    "gimnasia de la plata", "belgrano", "aldosivi", "banfield", "riestra",
    "estudiantes", "huracan las heras", "instituto", "lanus",
    "newells old boys", "platense", "sarmiento de junin", "talleres",
    "tigre", "union de santa fe", "velez"
]

# Elegir palabra y generar tablero
palabra = list(random.choice(palabras))
ahorcado = []
for i in range(len(palabra)):
    if palabra[i] == " ":
        ahorcado.append(" ")
    else:
        ahorcado.append("_")

letras_usadas = []
intentos_restantes = 6
palabra_adivinada = False

print("\n===== Bienvenido al Juego del Ahorcado =====\n")

# Ciclo principal del juego
while intentos_restantes > 0 and not palabra_adivinada:
    print("\n" + " ".join(ahorcado))  # Mostrar tablero bonito
    print(f"\nIntentos restantes: {intentos_restantes}")
    
    letra = validar_letra(letras_usadas)
    intentos_restantes = comprobar_letra(letra, palabra, ahorcado, intentos_restantes)
    
    if "_" not in ahorcado:
        palabra_adivinada = True

# Mensaje final
print("\n" + " ".join(ahorcado))
if palabra_adivinada:
    print("\n🎉 ¡Felicidades! Adivinaste la palabra secreta!")
else:
    print("\n😢 Te quedaste sin intentos.")
print(f"La palabra era: {''.join(palabra)}")