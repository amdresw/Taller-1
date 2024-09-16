#Ejercicio 16
#Enunciado: Escribe un programa que calcule el tiempo que tarda en llegar un automóvil a su destino.
# Andrés Araque, grupo J1 

Distancia= float(input("Ingrese la distancia a recorrer (km): "))
Velocidad= float(input("Ingrese la velocidad promedio del automóvil (km/h) "))

tiempoHoras = Distancia / Velocidad

# Convertir el tiempo de viaje a horas y minutos
horas = int(tiempoHoras)
minutos = int((tiempoHoras - horas) * 60)

# La 'f' al inicio de la cadena permite insertar variables directamente dentro de la cadena usando llaves {}.
# Los corchetes {} se utilizan para colocar las variables dentro de la cadena y mostrarlas en el formato deseado.
#Esto facilita la inclusión de variables en la cadena sin necesidad de concatenar(unir varias partes de texto en una sola cadena) y convierte el código en algo más limpio y legible.
print(f"Tiempo estimado de viaje: {horas} horas y {minutos} minutos")

if Velocidad > 120:
    print("Advertencia: La velocidad promedio es mayor a 120 km/h. Conduzca con precaución.")
    