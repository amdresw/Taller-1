#Ejercicio 20
#Enunciado: Escribe un programa que convierta una calificación numérica en una letra de acuerdo a un sistema de calificación específico, usando match .
# Andrés Araque, grupo J1.


CalificacionNumerica = int(input("Ingrese la calificación numérica (0-100): "))

match CalificacionNumerica:
    case Calificacion if 90 <= Calificacion <= 100:
        CalificacionLetra = 'A'
    case Calificacion if 80 <= Calificacion <= 89:
        CalificacionLetra = 'B'
    case Calificacion if 70 <= Calificacion <= 79:
        CalificacionLetra = 'C'
    case Calificacion if 60 <= Calificacion <= 69:
        CalificacionLetra = 'D'
    case Calificacion if 0 <= Calificacion <= 59:
        CalificacionLetra = 'F'
    case _:
        CalificacionLetra = 'Calificación no válida'
print(f"La calificación obtenida es una: {CalificacionLetra}")
