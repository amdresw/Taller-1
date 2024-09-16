#Ejercicio 23
#Enunciado: Escribe un programa que solicite al usuario un número entero positivo n y calcule la suma de los primeros n números enteros. Utiliza un ciclo for para realizar la suma.
#Andrés Araque, grupo J1

n = int(input("Ingrese un número entero positivo: "))


if n <= 0:
    print("El número debe ser positivo.")
else:
    suma = 0
    # El ciclo for con range(1, n + 1) itera desde 1 hasta n, inclusive.
    # El rango generado por range(1, n + 1) incluye el valor inicial (1) y
    # va hasta el valor final (n) sin incluirlo, por eso usamos n + 1 para que
    # el valor de n también sea incluido en la iteración.
    for i in range(1, n + 1):
        suma += i
    
    
    print(f"La suma de los primeros {n} números enteros es: {suma}")
50