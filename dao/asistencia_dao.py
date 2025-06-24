import json
import os
from datetime import datetime
from dao.jugador_dao import cargar_jugadores, guardar_jugadores

RUTA_ASISTENCIAS = "dao/asistencias.json"

def cargar_asistencias():
    if not os.path.exists(RUTA_ASISTENCIAS):
        return {}
    with open(RUTA_ASISTENCIAS, "r", encoding="utf-8") as f:
        return json.load(f)

def guardar_asistencias(asistencias):
    with open(RUTA_ASISTENCIAS, "w", encoding="utf-8") as f:
        json.dump(asistencias, f, indent=4)

def registrar_asistencia(entrenador_usuario, cedula):
    jugadores = cargar_jugadores()
    if entrenador_usuario not in jugadores or cedula not in jugadores[entrenador_usuario]:
        print("Jugador no registrado para este entrenador.")
        return

    asistencias = cargar_asistencias()
    key = f"{entrenador_usuario}_{cedula}"
    fecha = datetime.now().strftime("%Y-%m-%d")

    if key in asistencias:
        asistencias[key].append(fecha)
    else:
        asistencias[key] = [fecha]

    jugadores[entrenador_usuario][cedula]['asistencias'] += 1
    guardar_jugadores(jugadores)

    guardar_asistencias(asistencias)
    print(f"Asistencia registrada para {jugadores[entrenador_usuario][cedula]['nombre']} {jugadores[entrenador_usuario][cedula]['apellido']} en {fecha}.")

def listar_asistencias(entrenador_usuario, cedula=None, fecha_inicio=None, fecha_fin=None):
    asistencias = cargar_asistencias()
    resultado = {}
    from datetime import datetime as dt

    fecha_inicio_dt = dt.strptime(fecha_inicio, "%Y-%m-%d") if fecha_inicio else None
    fecha_fin_dt = dt.strptime(fecha_fin, "%Y-%m-%d") if fecha_fin else None

    for key, fechas in asistencias.items():
        if not key.startswith(entrenador_usuario + "_"):
            continue
        jug_cedula = key[len(entrenador_usuario)+1:]
        if cedula and jug_cedula != cedula:
            continue
        filtradas = []
        for f in fechas:
            fecha_dt = dt.strptime(f, "%Y-%m-%d")
            if fecha_inicio_dt and fecha_dt < fecha_inicio_dt:
                continue
            if fecha_fin_dt and fecha_dt > fecha_fin_dt:
                continue
            filtradas.append(f)
        if filtradas:
            resultado[jug_cedula] = filtradas
    print(f"Resultado: {resultado}")
    return resultado

