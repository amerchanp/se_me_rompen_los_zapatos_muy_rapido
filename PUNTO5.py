def leer_matriz(filas, columnas):
    matriz = []
    for i in range(filas):
        fila = []
        for j in range(columnas):
            valor = float(input(f"Ingrese el valor en la posición ({i}, {j}): "))
            fila.append(valor)
        matriz.append(fila)
    return matriz

def suma_fila(matriz, fila):
    return sum(matriz[fila])

def imprimir_matriz(m):
    for fila in m:
        print(fila)

#programa principal
filas = int(input("Ingrese el número de filas de la matriz: "))
columnas = int(input("Ingrese el número de columnas de la matriz: "))

print("Ingrese los valores de la matriz:")
matriz = leer_matriz(filas, columnas)

fila = int(input(f"Ingrese el índice de la fila a sumar (0 a {filas - 1}): "))

if 0 <= fila < filas:
    resultado = suma_fila(matriz, fila)
    print(f"La suma de la fila {fila} es: {resultado}")
else:
    print("Índice de fila no válido.")


