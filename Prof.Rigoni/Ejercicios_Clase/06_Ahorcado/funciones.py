def validar_letra(letras_usadas):
    while True:
        print(f"Letras ya ingresadas: {', '.join(letras_usadas) if letras_usadas else 'ninguna'}")
        letra = input("Ingrese una letra: ").lower()
        if not letra.isdigit():
            if len(letra) == 1:
                if letra in [".", ","]:
                    print("No se aceptan puntos ni comas.")
                elif letra in letras_usadas:
                    print("La letra ya fue usada anteriormente.")
                else:
                    letras_usadas.append(letra)
                    return letra
            else:
                print("Ingrese una letra a la vez.")
        else:
            print("Solo puede ingresar letras.")

def comprobar_letra(letra, palabra, ahorcado, intentos):
    if letra in palabra:
        for i in range(len(palabra)):
            if palabra[i] == letra:
                ahorcado[i] = letra
        print(f"¡Bien! La letra '{letra}' está en la palabra.")
        return intentos
    else:
        intentos -= 1
        print(f"¡Ups! La letra '{letra}' no está. Te quedan {intentos} intentos.")
        return intentos