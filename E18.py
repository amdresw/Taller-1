#Ejercicio 18
#Enunciado: Escribe un programa que calcule el número de créditos totales de un estudiante en base a lasmaterias cursadas y el puntaje obtenido en cada una.
# El puntaje debe ser evaluado como aprobado o no aprobado.
# Andrés Araque, grupo J1.


NumMaterias = int(input("Ingrese el número de materias que ha cursado: "))

# Inicializar el contador de créditos
CreditosTotales = 0

# Ciclo para evaluar cada materia (repasar este bloque, sigue siendo confuso).
# El ciclo for con (i) se usa para repetir un bloque de código un número específico de veces.
# 'i' es la variable que toma el valor de cada número en el rango (0, 1, 2,... hasta el límite - 1). En este caso el límite de i está determinado por el valor de NumMaterias.
# En cada iteración, 'i' cambia su valor, comenzando desde 0 y avanzando hasta el número anterior al límite dado.

for i in range(NumMaterias):
    # Solicitar el puntaje de la materia
    Puntaje = float(input(f"Ingrese el puntaje de la materia {i+1}: "))
    
    
    if Puntaje >= 60:
        print("Materia aprobada.")
        # Añadir 3 créditos por materia aprobada
        CreditosTotales += 3
    else:
        print("Materia no aprobada.")

print(f"El número total de créditos obtenidos es: {CreditosTotales}")
