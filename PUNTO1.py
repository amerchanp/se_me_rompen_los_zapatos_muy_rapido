def leer_matriz(filas, columnas):
    matriz = []
    for i in range(filas):
        fila = []
        for j in range(columnas):
            valor = float(input(f"Ingrese el valor en la posición ({i}, {j}): "))
            fila.append(valor)
        matriz.append(fila)
    return matriz

def sumar_matrices(m1, m2):
    filas = len(m1)
    columnas = len(m1[0])
    resultado = []
    for i in range(filas):
        fila = []
        for j in range(columnas):
            fila.append(m1[i][j] + m2[i][j])
        resultado.append(fila)
    return resultado

def restar_matrices(m1, m2):
    filas = len(m1)
    columnas = len(m1[0])
    resultado = []
    for i in range(filas):
        fila = []
        for j in range(columnas):
            fila.append(m1[i][j] - m2[i][j])
        resultado.append(fila)
    return resultado

def son_mismas_dimensiones(m1, m2):
    return len(m1) == len(m2) and len(m1[0]) == len(m2[0])

def imprimir_matriz(m):
    for fila in m:
        print(fila)

#progama principal
filas = int(input("Ingrese el número de filas de las matrices: "))
columnas = int(input("Ingrese el número de columnas de las matrices: "))

print("Ingrese los valores de la primera matriz:")
matriz1 = leer_matriz(filas, columnas)

print("Ingrese los valores de la segunda matriz:")
matriz2 = leer_matriz(filas, columnas)

if son_mismas_dimensiones(matriz1, matriz2):
    print("\nMatriz suma:")
    imprimir_matriz(sumar_matrices(matriz1, matriz2))

    print("\nMatriz resta:")
    imprimir_matriz(restar_matrices(matriz1, matriz2))
else:
    print("Las matrices no tienen las mismas dimensiones. No se puede realizar la operación.")
