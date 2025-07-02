# Importa el módulo pickle, que permite guardar y cargar objetos de Python en formato binario
import pickle
# Importa el módulo os para interactuar con el sistema operativo (verificar archivos, rutas, etc.)
import os
# Importa la clase Jugador, que contiene los atributos y métodos de cada jugador
from models.jugador import Jugador
# Importa todas las funciones de validación necesarias para asegurar que los datos ingresados sean válidos
from models.validaciones import (
    validar_cedula, validar_nombre, validar_apellido,
    validar_edad, validar_telefono, validar_peso,
    validar_altura, validar_antecedentes, validar_posicion, formatear_posicion, formatear_cedula
)

# Nombre del archivo donde se guardarán los datos de los jugadores en formato binario
JUGADORES_FILE = "jugadores.bin"

# Clase JugadorDAO (Data Access Object), encargada de manejar todas las operaciones de almacenamiento y consulta de jugadores
class JugadorDAO:

    # Método que intenta cargar los datos de jugadores desde el archivo binario
    @staticmethod
    def cargar_jugadores():
        # Verifica si el archivo existe en el sistema
        if os.path.exists(JUGADORES_FILE):
            # Abre el archivo en modo lectura binaria
            with open(JUGADORES_FILE, "rb") as f:
                # Carga (deserializa) el contenido del archivo usando pickle
                jugadores = pickle.load(f)
                # Recorre cada entrenador registrado en el archivo
                for entrenador in jugadores:
                    jugadores_entrenador = jugadores[entrenador]
                    ceds_correctas = {}  # Diccionario para corregir el formato de cédulas
                    # Recorre cada jugador asociado al entrenador
                    for cedula, jugador in jugadores_entrenador.items():
                        # Formatea la cédula correctamente (por ejemplo, elimina espacios, mayúsculas, etc.)
                        cedula_formateada = formatear_cedula(cedula)
                        # Guarda al jugador usando la cédula formateada como clave
                        ceds_correctas[cedula_formateada] = jugador
                    # Reemplaza los jugadores del entrenador con las cédulas corregidas
                    jugadores[entrenador] = ceds_correctas
                return jugadores  # Devuelve todos los jugadores cargados
        # Si el archivo no existe, devuelve un diccionario vacío (sin jugadores registrados)
        return {}

    # Método para guardar el diccionario de jugadores en el archivo binario
    @staticmethod
    def guardar_jugadores(jugadores):
        # Abre el archivo en modo escritura binaria (sobrescribe si ya existe)
        with open(JUGADORES_FILE, "wb") as f:
            # Guarda (serializa) el diccionario completo usando pickle
            pickle.dump(jugadores, f)

    # Método que permite registrar un nuevo jugador asociado a un entrenador específico
    @staticmethod
    def registrar_jugador(entrenador_usuario):
        jugadores = JugadorDAO.cargar_jugadores()  # Carga los jugadores desde archivo
        if entrenador_usuario not in jugadores:
            jugadores[entrenador_usuario] = {}  # Crea un nuevo espacio para ese entrenador

        # Entrada y validación de cédula única
        while True:
            cedula = input("Cédula: ").strip()
            cedula = formatear_cedula(cedula)
            if validar_cedula(cedula) and cedula not in jugadores[entrenador_usuario]:
                break
            print("Cédula no válida o ya existente.")

        # Entrada y validación de nombre
        while True:
            nombre = input("Nombre: ").strip()
            if validar_nombre(nombre):
                break
            print("Nombre no válido.")

        # Entrada y validación de apellido
        while True:
            apellido = input("Apellido: ").strip()
            if validar_apellido(apellido):
                break
            print("Apellido no válido.")

        # Entrada y validación de edad
        while True:
            edad = input("Edad: ").strip()
            if validar_edad(edad):
                edad = int(edad)
                break
            print("Edad no válida.")

        # Entrada y validación de teléfono
        while True:
            telefono = input("Teléfono (8 dígitos): ").strip()
            if validar_telefono(telefono):
                break
            print("Teléfono no válido.")

        # Entrada y validación de peso (convierte coma a punto si es necesario)
        while True:
            peso = input("Peso (kg): ").strip()
            if validar_peso(peso):
                peso = float(peso.replace(',', '.'))
                break
            print("Peso no válido.")

        # Entrada y validación de altura (en metros o cm, se convierte todo a cm)
        while True:
            altura = input("Altura (m o cm): ").strip()
            if validar_altura(altura):
                altura = float(altura.replace(',', '.'))
                if altura < 10:  # Si la altura es menor de 10, se asume que está en metros
                    altura *= 100
                break
            print("Altura no válida.")

        # Entrada de antecedentes (si no es válida se guarda como "No especificado")
        antecedentes = input("Antecedentes de lesión (si/no o descripción): ").strip()
        if not validar_antecedentes(antecedentes):
            print("Antecedentes inválidos. Se guardará como 'No especificado'.")
            antecedentes = "No especificado"

        # Entrada y validación de la posición del jugador
        while True:
            posicion_ingresada = input("Posición (Base, Escolta, Alero, Ala-Pívot, Pívot): ").strip()
            posicion_formateada = formatear_posicion(posicion_ingresada)
            if posicion_formateada:
                posicion = posicion_formateada
                break
            print("Posición no válida. Intente de nuevo.")

        # Se crea el objeto jugador con todos los datos recolectados
        jugador = Jugador(cedula, nombre, apellido, edad, telefono, peso, altura, antecedentes, posicion)
        # Se agrega el jugador al diccionario correspondiente al entrenador
        jugadores[entrenador_usuario][cedula] = jugador
        # Se guardan todos los datos nuevamente en archivo
        JugadorDAO.guardar_jugadores(jugadores)
        print("Jugador registrado correctamente.")

    # Método para buscar un jugador por cédula o nombre completo
    @staticmethod
    def buscar_jugador(entrenador_usuario):
        from dao.asistencia_dao import AsistenciaDAO  # Importación local para evitar referencias circulares
        jugadores = JugadorDAO.cargar_jugadores()
        if entrenador_usuario not in jugadores:
            print("No hay jugadores registrados.")
            input("Presione Enter para continuar...")
            return None

        # Solicita un término de búsqueda (puede ser cédula o nombre completo)
        consulta = input("Ingrese cédula o nombre completo: ").strip().lower()
        for cedula, jugador in jugadores[entrenador_usuario].items():
            nombre_completo = f"{jugador.nombre} {jugador.apellido}".lower()
            # Compara tanto la cédula como el nombre completo
            if cedula.lower() == consulta or nombre_completo == consulta:
                # Muestra todos los datos del jugador encontrado
                print("\n=== DATOS DEL JUGADOR ===")
                print(f"Cédula: {jugador.cedula}")
                print(f"Nombre: {jugador.nombre} {jugador.apellido}")
                print(f"Edad: {jugador.edad} años | Teléfono: {jugador.telefono}")
                print(f"Peso: {jugador.peso}kg | Altura: {jugador.altura}cm")
                print(f"Posición: {jugador.posicion}")
                print(f"IMC: {jugador.imc:.2f}")  # Muestra el índice de masa corporal

                # Muestra información sobre asistencia del jugador
                total_asistencias, ultima_fecha = AsistenciaDAO.obtener_asistencias_y_ultima(entrenador_usuario, cedula)
                if ultima_fecha:
                    print(f"Asistencias: {total_asistencias} (última: {ultima_fecha})")
                else:
                    print(f"Asistencias: {total_asistencias}")

                print(f"Antecedentes: {jugador.antecedentes}")
                print("==============================\n")
                input("Presione Enter para continuar...")
                return jugador

        # Si no encuentra coincidencia
        print("Jugador no encontrado.")
        input("Presione Enter para continuar...")
        return None

    # Método que permite modificar los datos de un jugador existente
    @staticmethod
    def modificar_jugador(entrenador_usuario):
        jugadores = JugadorDAO.cargar_jugadores()
        if entrenador_usuario not in jugadores:
            print("No hay jugadores registrados.")
            input("Presione Enter para continuar...")
            return

        # Solicita la cédula del jugador a modificar
        cedula = input("Ingrese cédula del jugador a modificar: ").strip()
        cedula = formatear_cedula(cedula)
        if cedula not in jugadores[entrenador_usuario]:
            print("Jugador no encontrado.")
            input("Presione Enter para continuar...")
            return

        jugador = jugadores[entrenador_usuario][cedula]

        # Solicita nuevos valores para actualizar (dejar vacío si no se desea modificar)
        nuevo_telefono = input(f"Teléfono actual ({jugador.telefono}): ").strip()
        if nuevo_telefono and validar_telefono(nuevo_telefono):
            jugador.telefono = nuevo_telefono

        nuevo_peso = input(f"Peso actual ({jugador.peso} kg): ").strip()
        if nuevo_peso and validar_peso(nuevo_peso):
            jugador.peso = float(nuevo_peso.replace(',', '.'))

        nueva_altura = input(f"Altura actual ({jugador.altura} cm): ").strip()
        if nueva_altura and validar_altura(nueva_altura):
            altura_f = float(nueva_altura.replace(',', '.'))
            if altura_f < 10:
                altura_f *= 100
            jugador.altura = altura_f

        antecedentes = input(f"Antecedentes actuales ({jugador.antecedentes}): ").strip()
        if antecedentes and validar_antecedentes(antecedentes):
            jugador.antecedentes = antecedentes

        nueva_posicion = input(f"Posición actual ({jugador.posicion}): ").strip()
        if nueva_posicion and validar_posicion(nueva_posicion):
            jugador.posicion = nueva_posicion

        # Recalcula el IMC con los nuevos datos
        jugador.imc = jugador.calcular_imc()

        # Guarda los cambios actualizados en archivo
        JugadorDAO.guardar_jugadores(jugadores)
        print("Datos actualizados correctamente.")
        input("Presione Enter para continuar...")

    # Método que elimina a un jugador del sistema
    @staticmethod
    def eliminar_jugador(entrenador_usuario):
        jugadores = JugadorDAO.cargar_jugadores()
        if entrenador_usuario not in jugadores:
            print("No hay jugadores registrados.")
            input("Presione Enter para continuar...")
            return

        # Solicita cédula del jugador a eliminar
        cedula = input("Ingrese la cédula del jugador a eliminar: ").strip()
        cedula = formatear_cedula(cedula)
        if cedula in jugadores[entrenador_usuario]:
            # Solicita confirmación antes de borrar
            confirmacion = input(f"¿Está seguro de eliminar al jugador {jugadores[entrenador_usuario][cedula].nombre}? (s/n): ").strip().lower()
            if confirmacion == "s":
                del jugadores[entrenador_usuario][cedula]
                JugadorDAO.guardar_jugadores(jugadores)
                print("Jugador eliminado correctamente.")
        else:
            print("Jugador no encontrado.")
        input("Presione Enter para continuar...")

    # Método que muestra en pantalla todos los jugadores de un entrenador
    @staticmethod
    def listar(entrenador_usuario):
        jugadores = JugadorDAO.cargar_jugadores()
        if entrenador_usuario not in jugadores or not jugadores[entrenador_usuario]:
            print("No hay jugadores registrados.")
            input("Presione Enter para continuar...")
            return

        print(f"\n=== Lista de jugadores del entrenador {entrenador_usuario} ===")
        # Recorre y muestra la información de cada jugador
        for jugador in jugadores[entrenador_usuario].values():
            print(jugador)
            print("-" * 30)
        input("Presione Enter para continuar...")
