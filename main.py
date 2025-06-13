import os
from models.jugadores import registrar_jugador, buscar_jugador, modificar_jugador
from models.asistencias import registrar_asistencia, listar_asistencias

from models.entrenadores import registrar_entrenador, iniciar_sesion

def login():
    while True:
        print("=== Bienvenido a EliteBasket ===")
        print("1. Iniciar sesión")
        print("2. Registrar nuevo entrenador")
        print("3. Salir")
        opcion = input("Seleccione una opción: ").strip()
        if opcion == "1":
            if iniciar_sesion():
                break
        elif opcion == "2":
            registrar_entrenador()
        elif opcion == "3":
            exit()
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    login()

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrar_jugador(cedula_o_nombre):
    cedula, jugador = buscar_jugador(cedula_o_nombre)
    if jugador:
        print("\n--- DATOS DEL JUGADOR ---")
        print(f"Cédula: {cedula}")
        print(f"Nombre: {jugador['nombre']} {jugador['apellido']}")
        print(f"Edad: {jugador['edad']} años")
        print(f"Teléfono: {jugador['telefono']}")
        print(f"Peso: {jugador['peso']} kg")
        print(f"Altura: {jugador['altura']} cm")
        print(f"Antecedentes de lesión: {jugador['antecedentes']}")
        print(f"Asistencias registradas: {jugador['asistencias']}")
    else:
        print("Jugador no encontrado.")

def listar_jugadores():
    import shelve
    from models.jugadores import DB_JUGADORES
    with shelve.open(DB_JUGADORES) as db:
        if len(db) == 0:
            print("\nNo hay jugadores registrados.")
            return
        print("\n--- JUGADORES REGISTRADOS ---")
        for cedula in db:
            j = db[cedula]
            print(f"Cédula: {cedula} | Nombre: {j['nombre']} {j['apellido']}")

def mostrar_menu():
    print("""
=== MENÚ ELITEBASKET ===
1. Registrar nuevo jugador
2. Buscar jugador
3. Modificar jugador
4. Registrar asistencia
5. Listar todos los jugadores
6. Salir
""")

def main():
    limpiar_pantalla()
    print("¡Bienvenido al Sistema EliteBasket!")

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            limpiar_pantalla()
            print("--- Registro de nuevo jugador ---")
            registrar_jugador()

        elif opcion == "2":
            limpiar_pantalla()
            print("--- Buscar jugador ---")
            busqueda = input("Ingrese cédula o nombre completo: ").strip()
            mostrar_jugador(busqueda)

        elif opcion == "3":
            limpiar_pantalla()
            print("--- Modificar jugador ---")
            modificar_jugador()

        elif opcion == "4":
            limpiar_pantalla()
            print("--- Registrar asistencia ---")
            cedula = input("Ingrese cédula del jugador: ").strip()
            registrar_asistencia(cedula)

        elif opcion == "5":
            limpiar_pantalla()
            listar_jugadores()

        elif opcion == "6":
            print("\n¡Gracias por usar EliteBasket! Hasta pronto.")
            break

        else:
            print("Opción no válida. Intente nuevamente.")

        input("\nPresione Enter para continuar...")
        limpiar_pantalla()

if __name__ == "__main__":
    main()