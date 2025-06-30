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
    def registrar(cls, entrenador, cedula=None):
        from dao.jugador_dao import JugadorDAO 

        jugadores = JugadorDAO.cargar_jugadores().get(entrenador, {})
        if not jugadores:
            print("No hay jugadores para registrar asistencia")
            return

        asistencias = cls._cargar()

        for ced, jugador in jugadores.items():
            while True:
                respuesta = input(f"Registrar asistencia para {jugador.nombre} {jugador.apellido} (s/n): ").strip().lower()
                if respuesta in ['s', 'n']:
                    break
                print("Respuesta inválida, ingresa 's' o 'n'.")
            if respuesta == 's':
                key = f"{entrenador}_{ced}"
                fecha = datetime.now().strftime("%Y-%m-%d %H:%M")
                if key in asistencias:
                    asistencias[key].append(fecha)
                else:
                    asistencias[key] = [fecha]
                print(f"Asistencia registrada para {jugador.nombre} {jugador.apellido}")
            else:
                print(f"Asistencia NO registrada para {jugador.nombre} {jugador.apellido}")

        cls._guardar(asistencias)

    @classmethod
    def obtener_asistencias_y_ultima(cls, entrenador, cedula):
        asistencias = cls._cargar()
        key = f"{entrenador}_{cedula}"
        if key in asistencias and asistencias[key]:
            total = len(asistencias[key])
            ultima_fecha = asistencias[key][-1]
            return total, ultima_fecha
        return 0, None

