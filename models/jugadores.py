from .validaciones import validar_cedula, validar_nombre

jugadores_registrados = {}

def registrar_jugador():
    cedula = input("Cédula (6-8 dígitos o 13 para INSS): ")
    if not validar_cedula(cedula):
        print("¡Cédula no válida para Nicaragua!")
        return
    
    nombre = input("Nombre completo: ")
    if not validar_nombre(nombre):
        print("El nombre solo debe contener letras.")
        return
    
    jugadores_registrados[cedula] = {"nombre": nombre, "asistencias": 0}
    print(f"Jugador {nombre} registrado (Cédula: {cedula}).")

def buscar_jugador(cedula):
    return jugadores_registrados.get(cedula, None)