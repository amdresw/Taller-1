#Ejercicio 17
#Enunciado: Escribe un programa que calcule la calificación final de un estudiante basándose en su calificación y si ha hecho tareas adicionales.
# Las tareas adicionales pueden darle un extra de puntos, pero el máximo de puntos no puede exceder 100.
# Andrés Araque, grupo J1 


Calificacion = float(input("Ingrese la calificación del estudiante: "))

#El método .strip().lower() asegura que la entrada sea tratada de forma uniforme (sin espacios adicionales y en minúsculas).
#Para evitar que el usuario rompa el programa tambien quitamos la "´" del si, aunque sea gramaticalmente incorrecto.
TareasAdicionales = input("¿Ha hecho tareas adicionales? (si/no): ").strip().lower() 


if TareasAdicionales == "si":
    
    CalificacionFinal = Calificacion * 1.05 # Añadir un 5% extra a la calificación
    
    if CalificacionFinal > 100:
        CalificacionFinal = 100
else:
   
    CalificacionFinal = Calificacion


print(f"La calificación final del estudiante es: {CalificacionFinal:.2f}") #aplicamos el mismo proceso para imprimir que el ejercicio anterior.
