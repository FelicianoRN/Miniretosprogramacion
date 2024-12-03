import random

def crear_arbol(altura, estrella=True):
    arbol = []
    for i in range(altura):
        nivel = ' ' * (altura - i - 1) + '*' * (2 * i + 1)
        arbol.append(nivel)
    tronco = ' ' * (altura - 2) + '|||'
    arbol.append(tronco)
    arbol.append(tronco)
    if estrella:
        arbol[0] = ' ' * (altura - 1) + '@'
    return arbol

def mostrar_arbol(arbol):
    for linea in arbol:
        print(linea)

def agregar_bolas(arbol, cantidad):
    for _ in range(cantidad):
        while True:
            fila = random.randint(1, len(arbol) - 3)
            columna = random.randint(0, len(arbol[fila]) - 1)
            if arbol[fila][columna] == '*':
                arbol[fila] = arbol[fila][:columna] + 'o' + arbol[fila][columna + 1:]
                break

def eliminar_bolas(arbol, cantidad):
    bolas = sum(linea.count('o') for linea in arbol)
    if bolas == 0:
        print("No hay bolas para eliminar.")
        return False
    for _ in range(cantidad):
        while True:
            fila = random.randint(1, len(arbol) - 3)
            columna = random.randint(0, len(arbol[fila]) - 1)
            if arbol[fila][columna] == 'o':
                arbol[fila] = arbol[fila][:columna] + '*' + arbol[fila][columna + 1:]
                break
    return True

def agregar_luces(arbol, cantidad):
    for _ in range(cantidad):
        while True:
            fila = random.randint(1, len(arbol) - 3)
            columna = random.randint(0, len(arbol[fila]) - 1)
            if arbol[fila][columna] == '*':
                arbol[fila] = arbol[fila][:columna] + '+' + arbol[fila][columna + 1:]
                break

def eliminar_luces(arbol, cantidad):
    luces = sum(linea.count('+') for linea in arbol)
    if luces == 0:
        print("No hay luces para eliminar.")
        return False
    for _ in range(cantidad):
        while True:
            fila = random.randint(1, len(arbol) - 3)
            columna = random.randint(0, len(arbol[fila]) - 1)
            if arbol[fila][columna] == '+':
                arbol[fila] = arbol[fila][:columna] + '*' + arbol[fila][columna + 1:]
                break
    return True

def encender_luces(arbol):
    for i in range(1, len(arbol) - 2):
        arbol[i] = arbol[i].replace('*', '+')

def apagar_luces(arbol):
    for i in range(1, len(arbol) - 2):
        arbol[i] = arbol[i].replace('+', '*')

def main():
    altura = int(input("Introduce la altura del árbol: "))
    arbol = crear_arbol(altura)
    mostrar_arbol(arbol)
    
    while True:
        print("\nOpciones:")
        print("1. Añadir estrella")
        print("2. Eliminar estrella")
        print("3. Añadir bolas")
        print("4. Eliminar bolas")
        print("5. Añadir luces")
        print("6. Eliminar luces")
        print("7. Encender luces")
        print("8. Apagar luces")
        print("9. Salir")
        
        opcion = int(input("Selecciona una opción: "))
        
        if opcion == 1:
            arbol = crear_arbol(altura, estrella=True)
        elif opcion == 2:
            arbol = crear_arbol(altura, estrella=False)
        elif opcion == 3:
            agregar_bolas(arbol, 2)
        elif opcion == 4:
            if not eliminar_bolas(arbol, 2):
                continue
        elif opcion == 5:
            agregar_luces(arbol, 3)
        elif opcion == 6:
            if not eliminar_luces(arbol, 3):
                continue
        elif opcion == 7:
            encender_luces(arbol)
        elif opcion == 8:
            apagar_luces(arbol)
        elif opcion == 9:
            break
        else:
            print("Opción no válida.")
        
        mostrar_arbol(arbol)

if __name__ == "__main__":
    main()