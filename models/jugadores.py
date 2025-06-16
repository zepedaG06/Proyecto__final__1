import shelve
from .validaciones import (
    validar_cedula, validar_nombre, validar_apellido,
    validar_edad, validar_telefono, validar_peso,
    validar_altura
)

DB_JUGADORES = "data/jugadores_db"

def registrar_jugador():
    with shelve.open(DB_JUGADORES) as db:
        cedula = input("Cédula: ").strip()
        if not validar_cedula(cedula):
            print("Cédula no válida.")
            return
        if cedula in db:
            print("Ya existe un jugador con esa cédula.")
            return

        nombre = input("Nombre: ").strip()
        if not validar_nombre(nombre):
            print("Nombre no válido.")
            return

        apellido = input("Apellido: ").strip()
        if not validar_apellido(apellido):
            print("Apellido no válido.")
            return

        edad = input("Edad: ").strip()
        if not validar_edad(edad):
            print("Edad no válida.")
            return

        telefono = input("Teléfono (8 dígitos): ").strip()
        if not validar_telefono(telefono):
            print("Teléfono no válido.")
            return

        peso = input("Peso (kg): ").strip()
        if not validar_peso(peso):
            print("Peso no válido.")
            return

        altura = input("Altura (cm): ").strip()
        if not validar_altura(altura):
            print("Altura no válida.")
            return

        antecedentes = input("Antecedentes de lesión (si/no o descripción): ").strip()

        jugador = {
            "nombre": nombre,
            "apellido": apellido,
            "edad": int(edad),
            "telefono": telefono,
            "peso": float(peso),
            "altura": float(altura),
            "antecedentes": antecedentes,
            "asistencias": 0
        }
        db[cedula] = jugador
        print(f"Jugador {nombre} {apellido} registrado con éxito.")

def buscar_jugador(cedula_o_nombre):
    with shelve.open(DB_JUGADORES) as db:
        for cedula in db:
            jugador = db[cedula]
            nombre_completo = f"{jugador['nombre']} {jugador['apellido']}".lower()
            if cedula == cedula_o_nombre or nombre_completo == cedula_o_nombre.lower():
                return cedula, jugador
    return None, None

def modificar_jugador():
    with shelve.open(DB_JUGADORES, writeback=True) as db:
        cedula = input("Ingrese cédula del jugador a modificar: ").strip()
        if cedula not in db:
            print("Jugador no encontrado.")
            return

        jugador = db[cedula]
        print("\nModificando datos. Dejar en blanco para no cambiar.")

        nuevo_telefono = input(f"Teléfono actual ({jugador['telefono']}): ").strip()
        if nuevo_telefono and validar_telefono(nuevo_telefono):
            jugador['telefono'] = nuevo_telefono

        nuevo_peso = input(f"Peso actual ({jugador['peso']} kg): ").strip()
        if nuevo_peso and validar_peso(nuevo_peso):
            jugador['peso'] = float(nuevo_peso)

        nueva_altura = input(f"Altura actual ({jugador['altura']} cm): ").strip()
        if nueva_altura and validar_altura(nueva_altura):
            jugador['altura'] = float(nueva_altura)

        antecedentes = input(f"Antecedentes de lesión actuales ({jugador['antecedentes']}): ").strip()
        if antecedentes:
            jugador['antecedentes'] = antecedentes

        print("Datos actualizados correctamente.")