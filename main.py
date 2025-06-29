from dao.entrenador_dao import EntrenadorDAO
from dao.jugador_dao import JugadorDAO
from dao.asistencia_dao import AsistenciaDAO
import os

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    usuario = None
    while True:
        limpiar_pantalla()
        if not usuario:
            print("=== ELITEBASKET ===")
            print("1. Iniciar sesión")
            print("2. Registrar entrenador")
            print("3. Salir")
            opcion = input("Opción: ").strip()

            if opcion == "1":
                usuario = EntrenadorDAO.iniciar_sesion()
            elif opcion == "2":
                EntrenadorDAO.registrar()
            elif opcion == "3":
                print("¡Hasta pronto!")
                break
        else:
            print(f"=== MENÚ ({usuario}) ===")
            print("1. Registrar jugador")
            print("2. Buscar jugador")
            print("3. Modificar jugador")
            print("4. Registrar asistencia")
            print("5. Listar jugadores")
            print("6. Eliminar jugador")
            print("7. Cerrar sesión")

            opcion = input("Opción: ").strip()
            if opcion == "1":
                limpiar_pantalla()
                JugadorDAO.registrar(usuario)
            elif opcion == "2":
                limpiar_pantalla()
                criterio = input("Ingrese cédula o nombre completo: ").strip()
                jugador = JugadorDAO.buscar(usuario, criterio)
                if jugador:
                    print(jugador)
                else:
                    print("No encontrado")
            elif opcion == "3":
                limpiar_pantalla()
                JugadorDAO.modificar(usuario)
            elif opcion == "4":
                limpiar_pantalla()
                AsistenciaDAO.registrar(usuario)
            elif opcion == "5":
                limpiar_pantalla()
                JugadorDAO.listar(usuario)
            elif opcion == "6":
                limpiar_pantalla()
                JugadorDAO.eliminar(usuario)
            elif opcion == "7":
                usuario = None

        input("\nPresione Enter para continuar...")
main()