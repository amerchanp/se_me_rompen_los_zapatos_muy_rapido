def leer_matriz(filas, columnas):
    matriz = []
    for i in range(filas):
        fila = []
        for j in range(columnas):
            valor = float(input(f"Ingrese el valor en la posición ({i}, {j}): "))
            fila.append(valor)
        matriz.append(fila)
    return matriz

def suma_columna(matriz, columna):
    suma = 0
    for fila in matriz:
        suma += fila[columna]
    return suma

def imprimir_matriz(m):
    for fila in m:
        print(fila)

#programa principal
filas = int(input("Ingrese el número de filas de la matriz: "))
columnas = int(input("Ingrese el número de columnas de la matriz: "))

print("Ingrese los valores de la matriz:")
matriz = leer_matriz(filas, columnas)

col = int(input(f"Ingrese el índice de la columna a sumar (0 a {columnas - 1}): "))

if 0 <= col < columnas:
    resultado = suma_columna(matriz, col)
    print(f"La suma de la columna {col} es: {resultado}")
else:
    print("Índice de columna no válido.")




