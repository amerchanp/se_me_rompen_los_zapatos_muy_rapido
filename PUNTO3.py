def leer_matriz(filas, columnas):
    matriz = []
    for i in range(filas):
        fila = []
        for j in range(columnas):
            valor = float(input(f"Ingrese el valor en la posición ({i}, {j}): "))
            fila.append(valor)
        matriz.append(fila)
    return matriz

def transponer_matriz(m):
    filas = len(m)
    columnas = len(m[0])
    transpuesta = []
    for j in range(columnas):
        nueva_fila = []
        for i in range(filas):
            nueva_fila.append(m[i][j])
        transpuesta.append(nueva_fila)
    return transpuesta

def imprimir_matriz(m):
    for fila in m:
        print(fila)

#programa pricipal
filas = int(input("Ingrese el número de filas de la matriz: "))
columnas = int(input("Ingrese el número de columnas de la matriz: "))

print("Ingrese los valores de la matriz:")
matriz = leer_matriz(filas, columnas)

print("\nMatriz transpuesta:")
imprimir_matriz(transponer_matriz(matriz))