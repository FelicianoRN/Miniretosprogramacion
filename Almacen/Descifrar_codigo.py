import random

def generar_codigo_secreto():
    letras = ['A', 'B', 'C','D', 'E']
    numeros = ['1', '2', '3', '4', '5']
    caracteres = letras + numeros
    codigo_secreto = random.sample(caracteres, 5)
    return ''.join(codigo_secreto)

def obtener_pistas(codigo_secreto, intento):
    pistas = []
    for i in range(5):
        if intento[i] == codigo_secreto[i]:
            pistas.append('Correcto')
        elif intento[i] in codigo_secreto:
            pistas.append('Presente')
        else:
            pistas.append('Incorrecto')
    return pistas

def validar_intento(intento):
    if len(intento) != 5:
        return False
    for char in intento:
        if char not in 'ABCDE12345':
            return False
    return True

def main():
    codigo_secreto = generar_codigo_secreto()
    print("¡Bienvenido al juego de descifrado de códigos de Amazon!")
    print("Debes adivinar el código secreto de 5 caracteres (A-E, 1-5).")
    print("Tienes 10 intentos. ¡Buena suerte!")

    intentos_restantes = 10

    while intentos_restantes > 0:
        intento = input("Introduce tu intento: ").upper()
        
        if not validar_intento(intento):
            print("Intento inválido. Asegúrate de que el código tenga 5 caracteres y solo contenga A, B, C, D, E 1, 2, 3, 4, 5.")
            continue

        pistas = obtener_pistas(codigo_secreto, intento)
        print("Pistas:", pistas)

        if intento == codigo_secreto:
            print("¡Felicidades! Has descifrado el código secreto.")
            return

        intentos_restantes -= 1
        print(f"Te quedan {intentos_restantes} intentos.")

    print(f"Lo siento, has agotado todos tus intentos. El código secreto era: {codigo_secreto}")

if __name__ == "__main__":
    main()