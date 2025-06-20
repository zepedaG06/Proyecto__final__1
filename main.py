import os
from models.jugadores import registrar_jugador, buscar_jugador, modificar_jugador
from models.asistencias import registrar_asistencia, listar_asistencias

from models.entrenadores import registrar_entrenador, iniciar_sesion
from models.jugadores import registrar_jugador, buscar_jugador, modificar_jugador, eliminar_jugador


def login():
    while True:
        print("=== Bienvenido a EliteBasket ===")
        print("1. Iniciar sesión")
        print("2. Registrar nuevo entrenador")
        print("3. Salir")
        opcion = input("Seleccione una opción: ").strip()
        if opcion == "1":
            usuario = iniciar_sesion()
            if usuario:
                return usuario  
        elif opcion == "2":
            registrar_entrenador()
        elif opcion == "3":
            exit()
        else:
            print("Opción inválida.")



def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrar_jugador(entrenador_usuario, cedula_o_nombre):
    cedula, jugador = buscar_jugador(entrenador_usuario, cedula_o_nombre)
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
        
        if 'imc' in jugador:
            print(f"Índice de masa corporal (IMC): {jugador['imc']}")
        else:
            print("Índice de masa corporal (IMC): no registrado")
    else:
        print("Jugador no encontrado.")



def listar_jugadores(entrenador_usuario):
    import shelve
    from models.jugadores import DB_JUGADORES
    with shelve.open(DB_JUGADORES) as db:
        if entrenador_usuario not in db or len(db[entrenador_usuario]) == 0:
            print("\nNo hay jugadores registrados para este entrenador.")
            return
        print("\n--- JUGADORES REGISTRADOS ---")
        for cedula in db[entrenador_usuario]:
            j = db[entrenador_usuario][cedula]
            print(f"Cédula: {cedula} | Nombre: {j['nombre']} {j['apellido']}")


def mostrar_menu():
    print("""
=== MENÚ ELITEBASKET ===
1. Registrar nuevo jugador
2. Buscar jugador
3. Modificar jugador
4. Registrar asistencia
5. Listar todos los jugadores
6. Eliminar jugador
7. Salir
""")


def main(usuario_actual):
    limpiar_pantalla()
    print(f"¡Bienvenido al Sistema EliteBasket, {usuario_actual}!")

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            limpiar_pantalla()
            print("--- Registro de nuevo jugador ---")
            registrar_jugador(usuario_actual)

        elif opcion == "2":
            limpiar_pantalla()
            print("--- Buscar jugador ---")
            busqueda = input("Ingrese cédula o nombre completo: ").strip()
            mostrar_jugador(usuario_actual, busqueda)

        elif opcion == "3":
            limpiar_pantalla()
            print("--- Modificar jugador ---")
            modificar_jugador(usuario_actual)

        elif opcion == "4":
            limpiar_pantalla()
            print("--- Registrar asistencia ---")
            cedula = input("Ingrese cédula del jugador: ").strip()
            registrar_asistencia(usuario_actual, cedula)

        elif opcion == "5":
            limpiar_pantalla()
            listar_jugadores(usuario_actual)

        elif opcion == "6":
            limpiar_pantalla()
            print("--- Eliminar jugador ---")
            eliminar_jugador(usuario_actual)
            
        elif opcion == "7":
         print("\n¡Gracias por usar EliteBasket! Hasta pronto.")
         break
        
        else:
            print("Opción no válida. Intente nuevamente.")

        input("\nPresione Enter para continuar...")
        limpiar_pantalla()

if __name__ == "__main__":
    usuario_actual = login()
    main(usuario_actual)