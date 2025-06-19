import shelve
from datetime import datetime
from .jugadores import DB_JUGADORES

DB_ASISTENCIAS = "data/asistencias_db"

def registrar_asistencia(entrenador_usuario, cedula):
    with shelve.open(DB_JUGADORES, writeback=True) as db_jug, shelve.open(DB_ASISTENCIAS, writeback=True) as db_asist:
        if entrenador_usuario not in db_jug or cedula not in db_jug[entrenador_usuario]:
            print("Jugador no registrado para este entrenador.")
            return
        
        fecha = datetime.now().strftime("%Y-%m-%d")

        key = f"{entrenador_usuario}_{cedula}"  

        if key in db_asist:
            db_asist[key].append(fecha)
        else:
            db_asist[key] = [fecha]
        
        db_jug[entrenador_usuario][cedula]['asistencias'] += 1

        print(f"Asistencia registrada para {db_jug[entrenador_usuario][cedula]['nombre']} {db_jug[entrenador_usuario][cedula]['apellido']} en {fecha}.")


def listar_asistencias(entrenador_usuario, cedula=None, fecha_inicio=None, fecha_fin=None):
    with shelve.open(DB_ASISTENCIAS) as db_asist:
        resultado = {}
        from datetime import datetime as dt

        fecha_inicio_dt = dt.strptime(fecha_inicio, "%Y-%m-%d") if fecha_inicio else None
        fecha_fin_dt = dt.strptime(fecha_fin, "%Y-%m-%d") if fecha_fin else None

        for key in db_asist:
            if not key.startswith(entrenador_usuario + "_"):
                continue
            jug_cedula = key[len(entrenador_usuario)+1:]
            if cedula and jug_cedula != cedula:
                continue
            fechas = db_asist[key]
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