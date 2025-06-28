import pickle
from datetime import datetime

class AsistenciaDAO:
    _archivo = "asistencias.bin"

    @classmethod
    def _cargar(cls):
        try:
            with open(cls._archivo, "rb") as f:
                return pickle.load(f)
        except (FileNotFoundError, EOFError):
            return {}

    @classmethod
    def _guardar(cls, datos):
        with open(cls._archivo, "wb") as f:
            pickle.dump(datos, f)

    @classmethod
    def registrar(cls, entrenador, cedula):
        asistencias = cls._cargar()
        key = f"{entrenador}_{cedula}"
        fecha = datetime.now().strftime("%Y-%m-%d %H:%M")

        if key in asistencias:
            asistencias[key].append(fecha)
        else:
            asistencias[key] = [fecha]

        cls._guardar(asistencias)
        print(f"Asistencia registrada (Total: {len(asistencias[key])})")

