import shelve
from datetime import datetime
from .jugadores import DB_JUGADORES

DB_ASISTENCIAS = "data/asistencias_db"

def registrar_asistencia(cedula):
    with shelve.open(DB_JUGADORES, writeback=True) as db_jug, shelve.open(DB_ASISTENCIAS, writeback=True) as db_asist:
        if cedula not in db_jug:
            print("Jugador no registrado.")
            return
        
        fecha = datetime.now().strftime("%Y-%m-%d")

        if cedula in db_asist:
            db_asist[cedula].append(fecha)
        else:
            db_asist[cedula] = [fecha]
        
        db_jug[cedula]['asistencias'] += 1

        print(f"✅ Asistencia registrada para {db_jug[cedula]['nombre']} {db_jug[cedula]['apellido']} en {fecha}.")

def listar_asistencias(cedula=None, fecha_inicio=None, fecha_fin=None):
    with shelve.open(DB_ASISTENCIAS) as db_asist:
        resultado = {}
        from datetime import datetime as dt

        fecha_inicio_dt = dt.strptime(fecha_inicio, "%Y-%m-%d") if fecha_inicio else None
        fecha_fin_dt = dt.strptime(fecha_fin, "%Y-%m-%d") if fecha_fin else None

        for jugador_cedula in db_asist:
            if cedula and jugador_cedula != cedula:
                continue
            fechas = db_asist[jugador_cedula]
            filtradas = []
            for f in fechas:
                fecha_dt = dt.strptime(f, "%Y-%m-%d")
                if fecha_inicio_dt and fecha_dt < fecha_inicio_dt:
                    continue
                if fecha_fin_dt and fecha_dt > fecha_fin_dt:
                    continue
                filtradas.append(f)
            if filtradas:
                resultado[jugador_cedula] = filtradas
        return resultado