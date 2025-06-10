from datetime import datetime
from .jugadores import jugadores_registrados  # ← MOVERLO AQUÍ

asistencias_registradas = {}

def registrar_asistencia(cedula):
    fecha = datetime.now().strftime("%Y-%m-%d")
    
    if cedula in asistencias_registradas:
        asistencias_registradas[cedula].append(fecha)
    else:
        asistencias_registradas[cedula] = [fecha]
    
    if cedula in jugadores_registrados:
        jugadores_registrados[cedula]["asistencias"] += 1
    
    print(f"✅ Asistencia registrada para cédula {cedula}.")
