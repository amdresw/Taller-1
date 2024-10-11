#ejericio 1 
# Enunciado: Escribe un programa que verifique si un número es par o impar utilizando if .
# Andrés Araque, grupo J1
numero= int( input("ingrese un numero entero: "))
if numero %2==0 : #%2 divide el numero introducido en 2
 print(numero,"es par.")
else: 
 print(numero,"es impar.")

from board_manager import *
from list_manager import *
from card_manager import *
from data_persistence import *

def MostrarMenu():
    print("Bienvenido a CampusTask")
    print("1. Crear Tablero")
    print("2. Ver Tableros")
    print("3. Actualizar Tablero")
    print("4. Eliminar Tablero")
    print("5. Crear Lista")
    print("6. Ver Listas")
    print("7. Actualizar Lista")
    print("8. Eliminar Lista")
    print("9. Crear Tarjeta")
    print("10. Ver Tarjetas")
    print("11. Actualizar Tarjeta")
    print("12. Eliminar Tarjeta")
    print("0. Salir")

def main():
    datos = CargarDatos('campustask.json')
    
    while True:
        MostrarMenu()
        opcion = int(input("Elige una opción: "))
        
        if opcion == 1:
            nombre = input("Nombre del tablero: ")
            datos = CrearTablero(nombre, datos)
        
        elif opcion == 2:
            tableros = VerTableros(datos)
            for tablero in tableros:
                print(f"Tablero {tablero['id']}: {tablero['nombre']}")
        
        elif opcion == 3:
            tablero_id = int(input("ID del tablero: "))
            nuevo_nombre = input("Nuevo nombre: ")
            datos = ActualizarTablero(tablero_id, nuevo_nombre, datos)
        
        elif opcion == 4:
            tablero_id = int(input("ID del tablero: "))
            datos = EliminarTablero(tablero_id, datos)

        # Similar lógica para las listas y tarjetas, llamando las funciones respectivas
        
        elif opcion == 0:
            GuardarDatos(datos, 'campustask.json')
            break

if __name__ == "__main__":
    main()
