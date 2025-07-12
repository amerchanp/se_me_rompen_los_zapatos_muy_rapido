def leer_matriz(filas, columnas):
    matriz = []
    for i in range(filas):
        fila = []
        for j in range(columnas):
            valor = float(input(f"Ingrese el valor en la posición ({i}, {j}): "))
            fila.append(valor)
        matriz.append(fila)
    return matriz

def multiplicar_matrices(m1, m2):
    filas_m1 = len(m1)
    columnas_m1 = len(m1[0])
    columnas_m2 = len(m2[0])
    
    resultado = []
    for i in range(filas_m1):
        fila_resultado = []
        for j in range(columnas_m2):
            suma = 0
            for k in range(columnas_m1):
                suma += m1[i][k] * m2[k][j]
            fila_resultado.append(suma)
        resultado.append(fila_resultado)
    return resultado

def dimensiones_validas_para_producto(m1, m2):
    return len(m1[0]) == len(m2)

def imprimir_matriz(m):
    for fila in m:
        print(fila)

#programa principal
filas1 = int(input("Ingrese el número de filas de la primera matriz: "))
columnas1 = int(input("Ingrese el número de columnas de la primera matriz: "))

print("Ingrese los valores de la primera matriz:")
matriz1 = leer_matriz(filas1, columnas1)

filas2 = int(input("Ingrese el número de filas de la segunda matriz: "))
columnas2 = int(input("Ingrese el número de columnas de la segunda matriz: "))

print("Ingrese los valores de la segunda matriz:")
matriz2 = leer_matriz(filas2, columnas2)

if dimensiones_validas_para_producto(matriz1, matriz2):
    print("\nProducto de matrices:")
    resultado = multiplicar_matrices(matriz1, matriz2)
    imprimir_matriz(resultado)
else:
    print("No se puede realizar el producto. El número de columnas de la primera matriz debe ser igual al número de filas de la segunda matriz.")
