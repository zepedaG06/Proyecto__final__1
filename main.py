from models.jugadores import registrar_jugador, buscar_jugador, jugadores_registrados
from models.asistencias import registrar_asistencia, asistencias_registradas
import os

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrar_jugador(jugador):
    if jugador:
        print("\n--- DATOS DEL JUGADOR ---")
        print(f"Nombre: {jugador['nombre']}")
        print(f"Asistencias: {jugador['asistencias']}")
        if jugador['asistencias'] > 0:
            print(f"Última asistencia: {asistencias_registradas.get(cedula, ['No registrada'])[-1]}")
    else:
        print("Jugador no encontrado.")

def mostrar_menu():
    print("\n=== MENÚ ELITEBASKET ===")
    print("1. Registrar nuevo jugador")
    print("2. Buscar jugador")
    print("3. Registrar asistencia")
    print("4. Ver todos los jugadores")
    print("5. Salir")

def ver_jugadores():
    if not jugadores_registrados:
        print("\nNo hay jugadores registrados.")
        return
    
    print("\n=== JUGADORES REGISTRADOS ===")
    for cedula, datos in jugadores_registrados.items():
        print(f"\nCédula: {cedula}")
        print(f"Nombre: {datos['nombre']}")
        print(f"Asistencias: {datos['asistencias']}")

if __name__ == "__main__":
    limpiar_pantalla()
    print("¡Bienvenido al Sistema EliteBasket!")
    
    while True:
        mostrar_menu()
        opcion = input("\nSeleccione una opción: ")

        if opcion == "1":
            limpiar_pantalla()
            print("--- REGISTRO DE NUEVO JUGADOR ---")
            registrar_jugador()
        
        elif opcion == "2":
            limpiar_pantalla()
            print("--- BUSCAR JUGADOR ---")
            cedula = input("Ingrese cédula a buscar: ")
            mostrar_jugador(buscar_jugador(cedula))
        
        elif opcion == "3":
            limpiar_pantalla()
            print("--- REGISTRO DE ASISTENCIA ---")
            cedula = input("Ingrese cédula del jugador: ")
            if buscar_jugador(cedula):
                registrar_asistencia(cedula)
                print(f"Asistencia registrada exitosamente para {jugadores_registrados[cedula]['nombre']}")
            else:
                print("Error: El jugador no está registrado.")
        
        elif opcion == "4":
            limpiar_pantalla()
            ver_jugadores()
        
        elif opcion == "5":
            print("\n¡Gracias por usar EliteBasket! Hasta pronto.")
            break
        
        else:
            print("Opción no válida. Intente nuevamente.")
        
        input("\nPresione Enter para continuar...")
        limpiar_pantalla()