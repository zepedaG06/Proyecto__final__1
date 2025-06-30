# Importar módulo pickle para serializar/deserializar objetos Python
import pickle
# Importar datetime para manejar fechas y horas
from datetime import datetime

# Clase para manejar operaciones de datos (DAO) de asistencias
class AsistenciaDAO:
    # Variable de clase que define el nombre del archivo donde se guardan las asistencias
    _archivo = "asistencias.bin"

    # Método de clase para cargar datos de asistencias desde archivo
    @classmethod
    def _cargar(cls):
        try:
            # Abrir archivo en modo lectura binaria
            with open(cls._archivo, "rb") as f:
                # Deserializar y retornar el contenido del archivo
                return pickle.load(f)
        except (FileNotFoundError, EOFError):
            # Si el archivo no existe o está vacío, retornar diccionario vacío
            return {}

    # Método de clase para guardar datos de asistencias en archivo
    @classmethod
    def _guardar(cls, datos):
        # Abrir archivo en modo escritura binaria
        with open(cls._archivo, "wb") as f:
            # Serializar y guardar los datos en el archivo
            pickle.dump(datos, f)

    # Método de clase para registrar asistencias de jugadores
    @classmethod
    def registrar(cls, entrenador, cedula=None):
        # Importar JugadorDAO para acceder a los jugadores (evita importación circular)
        from dao.jugador_dao import JugadorDAO 

        # Obtener la lista de jugadores del entrenador especificado
        jugadores = JugadorDAO.cargar_jugadores().get(entrenador, {})
        # Verificar si el entrenador tiene jugadores registrados
        if not jugadores:
            print("No hay jugadores para registrar asistencia")
            return

        # Cargar las asistencias existentes desde archivo
        asistencias = cls._cargar()

        # Iterar sobre cada jugador del entrenador
        for ced, jugador in jugadores.items():
            # Bucle para solicitar respuesta válida del usuario
            while True:
                # Preguntar si se registra asistencia para este jugador
                respuesta = input(f"Registrar asistencia para {jugador.nombre} {jugador.apellido} (s/n): ").strip().lower()
                # Verificar que la respuesta sea válida
                if respuesta in ['s', 'n']:
                    break
                print("Respuesta inválida, ingresa 's' o 'n'.")
            # Si la respuesta es 'sí', registrar la asistencia
            if respuesta == 's':
                # Crear clave única combinando entrenador y cédula
                key = f"{entrenador}_{ced}"
                # Obtener fecha y hora actual en formato específico
                fecha = datetime.now().strftime("%Y-%m-%d %H:%M")
                # Si ya existen asistencias para este jugador, agregar la nueva fecha
                if key in asistencias:
                    asistencias[key].append(fecha)
                else:
                    # Si es la primera asistencia, crear nueva lista
                    asistencias[key] = [fecha]
                print(f"Asistencia registrada para {jugador.nombre} {jugador.apellido}")
            else:
                # Informar que no se registró asistencia
                print(f"Asistencia NO registrada para {jugador.nombre} {jugador.apellido}")

        # Guardar todas las asistencias actualizadas en archivo
        cls._guardar(asistencias)

    # Método de clase para obtener total de asistencias y última fecha de un jugador
    @classmethod
    def obtener_asistencias_y_ultima(cls, entrenador, cedula):
        # Cargar las asistencias desde archivo
        asistencias = cls._cargar()
        # Crear clave única combinando entrenador y cédula
        key = f"{entrenador}_{cedula}"
        # Verificar si existen asistencias para este jugador
        if key in asistencias and asistencias[key]:
            # Contar el total de asistencias
            total = len(asistencias[key])
            # Obtener la fecha de la última asistencia (ultimo elemento de la lista)
            ultima_fecha = asistencias[key][-1]
            # Retornar el total y la última fecha
            return total, ultima_fecha
        # Si no hay asistencias, retornar 0 y None
        return 0, None

