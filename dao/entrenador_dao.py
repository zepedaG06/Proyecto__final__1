import json
import os

RUTA_ENTRENADORES = "dao/entrenadores.json"

def cargar_entrenadores():
    if not os.path.exists(RUTA_ENTRENADORES):
        return {}
    with open(RUTA_ENTRENADORES, "r", encoding="utf-8") as f:
        return json.load(f)

def guardar_entrenadores(entrenadores):
    with open(RUTA_ENTRENADORES, "w", encoding="utf-8") as f:
        json.dump(entrenadores, f, indent=4)

def registrar_entrenador():
    entrenadores = cargar_entrenadores()
    usuario = input("Usuario: ").strip()
    if usuario in entrenadores:
        print("Usuario ya existe.")
        return False
    contrasena = input("Contraseña: ").strip()
    entrenadores[usuario] = contrasena
    guardar_entrenadores(entrenadores)
    print(f"Entrenador {usuario} registrado.")
    return True

def iniciar_sesion():
    entrenadores = cargar_entrenadores()
    usuario = input("Usuario: ").strip()
    contrasena = input("Contraseña: ").strip()
    if usuario in entrenadores and entrenadores[usuario] == contrasena:
        print(f"Bienvenido, {usuario}!")
        return usuario
    print("Usuario o contraseña incorrectos.")
    return None
