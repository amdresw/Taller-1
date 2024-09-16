#Ejercicio 22
#Enunciado: Escribe un programa que calcule el costo de estacionamiento basado en el número de horas, con tarifas progresivas.
# Andrés Araque, grupo J1

Horas = int(input("Ingrese el número de horas de estacionamiento: "))

CostoTotal = 0 #inicializar CostoTotal a 0 es una medida preventiva que ayuda a garantizar que la variable siempre tenga un valor válido.

if Horas <= 0:
    print("El número de horas debe ser positivo.")
elif Horas <= 1:
    CostoTotal = 5  # Costo para la primera hora
elif Horas <= 4:
    CostoTotal = 5 + (Horas - 1) * 4  # Primera hora + $4 por cada hora adicional hasta la cuarta
else:
    CostoTotal = 5 + 3 * (Horas - 4) + 3 * 3  # Primera hora + 3 horas a $4 cada una + horas adicionales a $3 cada una

print(f"El costo total de estacionamiento es: ${CostoTotal}")
