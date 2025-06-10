from models.jugadores import registrar_jugador, buscar_jugador
from models.asistencias import registrar_asistencia

if __name__ == "__main__":
    registrar_jugador()

def mostrar_menu():
    print("\n--- MENÚ ELITEBASKET ---")
    print("1. Registrar jugador")
    print("2. Buscar jugador")
    print("3. Registrar asistencia")
    print("4. Salir")

if __name__ == "__main__":
    while True:
        mostrar_menu()
        opcion = input("Opción: ")
        
        if opcion == "1":
            registrar_jugador()
        elif opcion == "2":
            cedula = input("Ingrese cédula a buscar: ")
            jugador = buscar_jugador(cedula)
            print(jugador if jugador else "Jugador no encontrado.")
        elif opcion == "3":
            cedula = input("Ingrese cédula del jugador: ")
            registrar_asistencia(cedula)
        elif opcion == "4":
            print("¡Hasta pronto!")
            break
        else:
            print("Opción inválida.")