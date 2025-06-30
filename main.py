# Importar las clases DAO para manejar datos de entrenadores
from dao.entrenador_dao import EntrenadorDAO
# Importar las clases DAO para manejar datos de jugadores
from dao.jugador_dao import JugadorDAO
# Importar las clases DAO para manejar datos de asistencias
from dao.asistencia_dao import AsistenciaDAO
# Importar módulo del sistema operativo para limpiar pantalla
import os

# Función para limpiar la pantalla de la consola
def limpiar_pantalla():
    # Ejecutar comando 'cls' en Windows o 'clear' en Unix/Linux/Mac
    os.system('cls' if os.name == 'nt' else 'clear')

# Función principal del programa
def main():
    # Variable para almacenar el usuario logueado (None = no hay sesión activa)
    usuario = None
    # Bucle principal del programa que se ejecuta indefinidamente
    while True:
        # Limpiar la pantalla antes de mostrar el menú
        limpiar_pantalla()
        # Verificar si no hay usuario logueado
        if not usuario:
            # Mostrar el menú de inicio (sin sesión activa)
            print("=== ELITEBASKET ===")
            print("1. Iniciar sesión")
            print("2. Registrar entrenador")
            print("3. Salir")
            # Leer la opción del usuario y quitar espacios en blanco
            opcion = input("Opción: ").strip()

            # Evaluar la opción seleccionada
            if opcion == "1":
                # Intentar iniciar sesión y guardar el usuario si es exitoso
                usuario = EntrenadorDAO.iniciar_sesion()
            elif opcion == "2":
                # Registrar un nuevo entrenador
                EntrenadorDAO.registrar()
            elif opcion == "3":
                # Mostrar mensaje de despedida y salir del programa
                print("¡Hasta pronto!")
                break
        else:
            # Mostrar el menú principal (con sesión activa)
            print(f"=== MENÚ ({usuario}) ===")
            print("1. Registrar jugador")
            print("2. Buscar jugador")
            print("3. Modificar jugador")
            print("4. Registrar asistencia")
            print("5. Listar jugadores")
            print("6. Eliminar jugador")
            print("7. Cerrar sesión")

            # Leer la opción del usuario y quitar espacios en blanco
            opcion = input("Opción: ").strip()
            # Evaluar la opción seleccionada en el menú principal
            if opcion == "1":
                # Limpiar pantalla y registrar un nuevo jugador
                limpiar_pantalla()
                JugadorDAO.registrar_jugador(usuario)
            elif opcion == "2":
                # Limpiar pantalla y buscar un jugador específico
                limpiar_pantalla()
                jugador = JugadorDAO.buscar_jugador(usuario)
            elif opcion == "3":
                # Limpiar pantalla y modificar datos de un jugador
                limpiar_pantalla()
                JugadorDAO.modificar_jugador(usuario)
            elif opcion == "4":
                # Limpiar pantalla y registrar asistencias
                limpiar_pantalla()
                AsistenciaDAO.registrar(usuario)
            elif opcion == "5":
                # Limpiar pantalla y mostrar lista de todos los jugadores
                limpiar_pantalla()
                JugadorDAO.listar(usuario)
            elif opcion == "6":
                # Limpiar pantalla y eliminar un jugador
                limpiar_pantalla()
                JugadorDAO.eliminar_jugador(usuario)
            elif opcion == "7":
                # Cerrar sesión poniendo usuario en None
                usuario = None    
# Ejecutar la función principal del programa
main()
