import pickle
from models.jugador import Jugador
from models.validaciones import (
    validar_cedula, formatear_cedula,
    validar_nombre, validar_apellido,
    validar_edad, validar_telefono,
    validar_peso, parsear_peso,
    validar_altura, parsear_altura,
    validar_posicion, formatear_posicion
)

class JugadorDAO:
    _archivo = "jugadores.bin"

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
    def registrar(cls, entrenador: str):
        jugadores = cls._cargar()
        if entrenador not in jugadores:
            jugadores[entrenador] = {}

        while True:
            cedula = input("Cédula (formato 001-XXXXXX-XXXXA): ").strip()
            cedula = formatear_cedula(cedula)
            if not validar_cedula(cedula):
                print("Cédula inválida.")
                continue
            if cedula in jugadores[entrenador]:
                print("Cédula ya registrada")
                continue
            break

        while True:
            nombre = input("Nombre: ").strip()
            if not validar_nombre(nombre):
                print("Nombre inválido.")
                continue
            break

        while True:
            apellido = input("Apellido: ").strip()
            if not validar_apellido(apellido):
                print("Apellido inválido.")
                continue
            break

        while True:
            edad_input = input("Edad: ").strip()
            if not validar_edad(edad_input):
                print("Edad inválida. Debe estar entre 15 y 50.")
                continue
            edad = int(edad_input)
            break

        while True:
            telefono = input("Teléfono (8 dígitos): ").strip()
            if not validar_telefono(telefono):
                print("Teléfono inválido.")
                continue
            break

        while True:
            peso_input = input("Peso (30-200 kg, acepta coma decimal): ").strip()
            if not validar_peso(peso_input):
                print("Peso inválido.")
                continue
            peso = parsear_peso(peso_input)
            break

        while True:
            altura_input = input("Altura (100-250 cm o en metros, ej. 1.75): ").strip()
            if not validar_altura(altura_input):
                print("Altura inválida.")
                continue
            altura = parsear_altura(altura_input)
            break

        antecedentes = input("Antecedentes médicos: ").strip()

        while True:
            posicion_input = input("Posición (Base, Escolta, Alero, Ala-pívot, Pívot): ").strip()
            if not validar_posicion(posicion_input):
                print("Posición inválida.")
                continue
            posicion = formatear_posicion(posicion_input)
            break

        jugador = Jugador(cedula, nombre, apellido, edad, telefono, peso, altura, antecedentes, posicion)
        jugadores[entrenador][cedula] = jugador
        cls._guardar(jugadores)
        print("Jugador registrado")

    @classmethod
    def buscar(cls, entrenador: str, criterio: str) -> Jugador:
        jugadores = cls._cargar().get(entrenador, {})
        criterio = criterio.strip()
        for cedula, jugador in jugadores.items():
            if cedula.lower() == criterio.lower():
                return jugador
        criterio_lower = criterio.lower()
        for jugador in jugadores.values():
            nombre_completo = f"{jugador.nombre} {jugador.apellido}".lower()
            if nombre_completo == criterio_lower:
               return jugador
        return None

    @classmethod
    def listar(cls, entrenador: str):
        jugadores = cls._cargar().get(entrenador, {})
        if not jugadores:
            print("No hay jugadores registrados")
            return
        try:
            with open("asistencias.bin", "rb") as f:
                asistencias = pickle.load(f)
        except (FileNotFoundError, EOFError):
            asistencias = {}

        print(f"\n=== JUGADORES DE {entrenador.upper()} ===")
        for cedula, jugador in jugadores.items():
            key = f"{entrenador}_{cedula}"
            if key in asistencias:
                jugador.asistencias = len(asistencias[key])
            else:
                jugador.asistencias = 0
            print(jugador)
            print("-" * 40)

    @classmethod
    def modificar(cls, entrenador: str):
        jugadores = cls._cargar()
        if entrenador not in jugadores or not jugadores[entrenador]:
            print("No hay jugadores para modificar")
            return

        cedula = input("Cédula del jugador a modificar: ").strip()
        cedula = formatear_cedula(cedula)
        if cedula not in jugadores[entrenador]:
            print("Jugador no encontrado")
            return

        jugador = jugadores[entrenador][cedula]
        print("Deje en blanco si no desea modificar ese dato.\n")

        nuevo_nombre = input(f"Nuevo nombre [{jugador.nombre}]: ").strip()
        nuevo_apellido = input(f"Nuevo apellido [{jugador.apellido}]: ").strip()
        nueva_edad = input(f"Nueva edad [{jugador.edad}]: ").strip()
        nuevo_telefono = input(f"Nuevo teléfono [{jugador.telefono}]: ").strip()
        nuevo_peso = input(f"Nuevo peso [{jugador.peso}]: ").strip()
        nueva_altura = input(f"Nueva altura [{jugador.altura}]: ").strip()
        nueva_posicion = input(f"Nueva posición [{jugador.posicion}]: ").strip()
        nuevos_antecedentes = input(f"Nuevos antecedentes [{jugador.antecedentes}]: ").strip()

        if nuevo_nombre and validar_nombre(nuevo_nombre): 
            jugador.nombre = nuevo_nombre
        elif nuevo_nombre:
            print("Nombre inválido, no se cambió.")

        if nuevo_apellido and validar_apellido(nuevo_apellido):
            jugador.apellido = nuevo_apellido
        elif nuevo_apellido:
            print("Apellido inválido, no se cambió.")

        if nueva_edad:
            if validar_edad(nueva_edad):
                jugador.edad = int(nueva_edad)
            else:
                print("Edad inválida, no se cambió.")

        if nuevo_telefono and validar_telefono(nuevo_telefono):
            jugador.telefono = nuevo_telefono
        elif nuevo_telefono:
            print("Teléfono inválido, no se cambió.")

        if nuevo_peso:
            if validar_peso(nuevo_peso):
                jugador.peso = parsear_peso(nuevo_peso)
            else:
                print("Peso inválido, no se cambió.")

        if nueva_altura:
            if validar_altura(nueva_altura):
                jugador.altura = parsear_altura(nueva_altura)
            else:
                print("Altura inválida, no se cambió.")

        if nueva_posicion:
            if validar_posicion(nueva_posicion):
                jugador.posicion = formatear_posicion(nueva_posicion)
            else:
                print("Posición inválida, no se cambió.")

        if nuevos_antecedentes:
            jugador.antecedentes = nuevos_antecedentes

        jugador._calcular_imc()

        cls._guardar(jugadores)
        print("Datos del jugador actualizados")

    @classmethod
    def eliminar(cls, entrenador: str):
        jugadores = cls._cargar()
        if entrenador not in jugadores or not jugadores[entrenador]:
            print("No hay jugadores para eliminar")
            return

        cedula = input("Cédula del jugador a eliminar: ").strip()
        cedula = formatear_cedula(cedula)
        if cedula not in jugadores[entrenador]:
            print("Jugador no encontrado")
            return

        confirmacion = input(f"¿Estás seguro de eliminar a {jugadores[entrenador][cedula].nombre}? (s/n): ").strip().lower()
        if confirmacion == "s":
            del jugadores[entrenador][cedula]
            cls._guardar(jugadores)
            print("Jugador eliminado")
        else:
            print("Operación cancelada")
