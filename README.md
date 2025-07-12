# RETO 10
## Ejercicio 1
Para este primer ejercicio hice un programa que pide dos matrices del mismo tamaño y luego las suma y las resta. Lo importante acá era asegurarme de que las matrices tuvieran las mismas dimensiones antes de hacer cualquier operación, porque si no, no tiene sentido matemáticamente. Usé funciones separadas para leer las matrices, sumarlas, restarlas y mostrarlas, para que todo quedara más ordenado y fácil de entender.

```
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

# Programa principal
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

```

## Ejercicio 2
En este punto quise hacer el típico producto de matrices que uno ve en álgebra. La clave aquí es que el número de columnas de la primera matriz debe coincidir con el número de filas de la segunda, así que verifiqué eso antes de hacer la multiplicación. El programa pide ambas matrices, revisa si se pueden multiplicar y luego va elemento por elemento haciendo la suma de productos correspondiente. Aunque es un poco más largo que los otros, lo hice paso a paso para que fuera claro.

```
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

# Programa principal
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

```

## Ejercicio 3
Este fue más sencillo. Lo que hice fue crear un programa que toma una matriz y devuelve su transpuesta, es decir, cambiar las filas por columnas. Me pareció interesante porque no se necesita hacer operaciones matemáticas complejas, solo cambiar el orden de los elementos. Usé un ciclo que recorre las columnas primero y luego las filas, y con eso ya se arma la transpuesta.

```
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

# Programa principal
filas = int(input("Ingrese el número de filas de la matriz: "))
columnas = int(input("Ingrese el número de columnas de la matriz: "))

print("Ingrese los valores de la matriz:")
matriz = leer_matriz(filas, columnas)

print("\nMatriz transpuesta:")
imprimir_matriz(transponer_matriz(matriz))

```

## Ejercicio 4
Acá la idea fue tomar una matriz y permitirle al usuario escoger una columna específica para sumar todos los valores de esa columna. Lo que hice fue recorrer cada fila y tomar el valor que está justo en la posición de la columna que el usuario eligió. Verifiqué que la columna que se ingresa esté dentro del rango correcto, por si acaso.

```
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

# Programa principal
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

```

## Ejercicio 5
Este último punto es parecido al anterior, pero ahora sumamos una fila completa. En este caso no hace falta recorrer toda la matriz, solo tomar directamente la fila que se quiere sumar y usar sum() para obtener el resultado. También verifiqué que el índice de la fila ingresada fuera válido. Es de los ejercicios más simples, pero igual es útil para practicar.

```
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

# Programa principal
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

```

Muchas gracias.
