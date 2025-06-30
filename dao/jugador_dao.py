import pickle
import os
from models.jugador import Jugador
from models.validaciones import (
    validar_cedula, validar_nombre, validar_apellido,
    validar_edad, validar_telefono, validar_peso,
    validar_altura, validar_antecedentes, validar_posicion, formatear_posicion, formatear_cedula
)

JUGADORES_FILE = "jugadores.bin"

class JugadorDAO:

    @staticmethod
    def cargar_jugadores():
        if os.path.exists(JUGADORES_FILE):
            with open(JUGADORES_FILE, "rb") as f:
                jugadores = pickle.load(f)
                for entrenador in jugadores:
                    jugadores_entrenador = jugadores[entrenador]
                    ceds_correctas = {}
                    for cedula, jugador in jugadores_entrenador.items():
                        cedula_formateada = formatear_cedula(cedula)
                        ceds_correctas[cedula_formateada] = jugador
                    jugadores[entrenador] = ceds_correctas
                return jugadores
        return {}

    @staticmethod
    def guardar_jugadores(jugadores):
        with open(JUGADORES_FILE, "wb") as f:
            pickle.dump(jugadores, f)

    @staticmethod
    def registrar_jugador(entrenador_usuario):
        jugadores = JugadorDAO.cargar_jugadores()
        if entrenador_usuario not in jugadores:
            jugadores[entrenador_usuario] = {}

        while True:
            cedula = input("Cédula: ").strip()
            cedula = formatear_cedula(cedula) 
            if validar_cedula(cedula) and cedula not in jugadores[entrenador_usuario]:
                break
            print("Cédula no válida o ya existente.")

        while True:
            nombre = input("Nombre: ").strip()
            if validar_nombre(nombre):
                break
            print("Nombre no válido.")

        while True:
            apellido = input("Apellido: ").strip()
            if validar_apellido(apellido):
                break
            print("Apellido no válido.")

        while True:
            edad = input("Edad: ").strip()
            if validar_edad(edad):
                edad = int(edad)
                break
            print("Edad no válida.")

        while True:
            telefono = input("Teléfono (8 dígitos): ").strip()
            if validar_telefono(telefono):
                break
            print("Teléfono no válido.")

        while True:
            peso = input("Peso (kg): ").strip()
            if validar_peso(peso):
                peso = float(peso.replace(',', '.'))
                break
            print("Peso no válido.")

        while True:
            altura = input("Altura (m o cm): ").strip()
            if validar_altura(altura):
                altura = float(altura.replace(',', '.'))
                if altura < 10:
                    altura *= 100
                break
            print("Altura no válida.")

        antecedentes = input("Antecedentes de lesión (si/no o descripción): ").strip()
        if not validar_antecedentes(antecedentes):
            print("Antecedentes inválidos. Se guardará como 'No especificado'.")
            antecedentes = "No especificado"

        while True:
            posicion_ingresada = input("Posición (Base, Escolta, Alero, Ala-Pívot, Pívot): ").strip()
            posicion_formateada = formatear_posicion(posicion_ingresada)
            if posicion_formateada:
                posicion = posicion_formateada
                break
            print("Posición no válida. Intente de nuevo.")
        jugador = Jugador(cedula, nombre, apellido, edad, telefono, peso, altura, antecedentes, posicion)
        jugadores[entrenador_usuario][cedula] = jugador
        JugadorDAO.guardar_jugadores(jugadores)
        print("Jugador registrado correctamente.")

    @staticmethod
    def buscar_jugador(entrenador_usuario):
        from dao.asistencia_dao import AsistenciaDAO  
        jugadores = JugadorDAO.cargar_jugadores()
        if entrenador_usuario not in jugadores:
            print("No hay jugadores registrados.")
            input("Presione Enter para continuar...")
            return None

        consulta = input("Ingrese cédula o nombre completo: ").strip().lower()
        for cedula, jugador in jugadores[entrenador_usuario].items():
            nombre_completo = f"{jugador.nombre} {jugador.apellido}".lower()
            if cedula.lower() == consulta or nombre_completo == consulta:
                print("\n=== DATOS DEL JUGADOR ===")
                print(f"Cédula: {jugador.cedula}")
                print(f"Nombre: {jugador.nombre} {jugador.apellido}")
                print(f"Edad: {jugador.edad} años | Teléfono: {jugador.telefono}")
                print(f"Peso: {jugador.peso}kg | Altura: {jugador.altura}cm")
                print(f"Posición: {jugador.posicion}")
                print(f"IMC: {jugador.imc:.2f}")

                total_asistencias, ultima_fecha = AsistenciaDAO.obtener_asistencias_y_ultima(entrenador_usuario, cedula)
                if ultima_fecha:
                    print(f"Asistencias: {total_asistencias} (última: {ultima_fecha})")
                else:
                    print(f"Asistencias: {total_asistencias}")

                print(f"Antecedentes: {jugador.antecedentes}")
                print("==============================\n")
                input("Presione Enter para continuar...")
                return jugador

        print("Jugador no encontrado.")
        input("Presione Enter para continuar...")
        return None

    @staticmethod
    def modificar_jugador(entrenador_usuario):
        jugadores = JugadorDAO.cargar_jugadores()
        if entrenador_usuario not in jugadores:
            print("No hay jugadores registrados.")
            input("Presione Enter para continuar...")
            return

        cedula = input("Ingrese cédula del jugador a modificar: ").strip()
        cedula = formatear_cedula(cedula) 
        if cedula not in jugadores[entrenador_usuario]:
            print("Jugador no encontrado.")
            input("Presione Enter para continuar...")
            return

        jugador = jugadores[entrenador_usuario][cedula]

        nuevo_telefono = input(f"Teléfono actual ({jugador.telefono}): ").strip()
        if nuevo_telefono and validar_telefono(nuevo_telefono):
            jugador.telefono = nuevo_telefono

        nuevo_peso = input(f"Peso actual ({jugador.peso} kg): ").strip()
        if nuevo_peso and validar_peso(nuevo_peso):
            jugador.peso = float(nuevo_peso.replace(',', '.'))

        nueva_altura = input(f"Altura actual ({jugador.altura} cm): ").strip()
        if nueva_altura and validar_altura(nueva_altura):
            altura_f = float(nueva_altura.replace(',', '.'))
            if altura_f < 10:
                altura_f *= 100
            jugador.altura = altura_f

        antecedentes = input(f"Antecedentes actuales ({jugador.antecedentes}): ").strip()
        if antecedentes and validar_antecedentes(antecedentes):
            jugador.antecedentes = antecedentes

        nueva_posicion = input(f"Posición actual ({jugador.posicion}): ").strip()
        if nueva_posicion and validar_posicion(nueva_posicion):
            jugador.posicion = nueva_posicion

        jugador.imc = jugador.calcular_imc()

        JugadorDAO.guardar_jugadores(jugadores)
        print("Datos actualizados correctamente.")
        input("Presione Enter para continuar...")

    @staticmethod
    def eliminar_jugador(entrenador_usuario):
        jugadores = JugadorDAO.cargar_jugadores()
        if entrenador_usuario not in jugadores:
            print("No hay jugadores registrados.")
            input("Presione Enter para continuar...")
            return

        cedula = input("Ingrese la cédula del jugador a eliminar: ").strip()
        cedula = formatear_cedula(cedula) 
        if cedula in jugadores[entrenador_usuario]:
            confirmacion = input(f"¿Está seguro de eliminar al jugador {jugadores[entrenador_usuario][cedula].nombre}? (s/n): ").strip().lower()
            if confirmacion == "s":
                del jugadores[entrenador_usuario][cedula]
                JugadorDAO.guardar_jugadores(jugadores)
                print("Jugador eliminado correctamente.")
        else:
            print("Jugador no encontrado.")
        input("Presione Enter para continuar...")


    @staticmethod
    def listar(entrenador_usuario):
        jugadores = JugadorDAO.cargar_jugadores()
        if entrenador_usuario not in jugadores or not jugadores[entrenador_usuario]:
            print("No hay jugadores registrados.")
            input("Presione Enter para continuar...")
            return

        print(f"\n=== Lista de jugadores del entrenador {entrenador_usuario} ===")
        for jugador in jugadores[entrenador_usuario].values():
            print(jugador)
            print("-" * 30)
        input("Presione Enter para continuar...")
