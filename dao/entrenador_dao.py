<<<<<<< HEAD
# Importar módulo pickle para serializar/deserializar objetos Python
import pickle

# Clase para manejar operaciones de datos (DAO) de entrenadores
class EntrenadorDAO:
    # Variable de clase que define el nombre del archivo donde se guardan los entrenadores
    _archivo = "entrenadores.bin"

    # Método de clase para cargar datos de entrenadores desde archivo
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

    # Método de clase para guardar datos de entrenadores en archivo
    @classmethod
    def _guardar(cls, datos):
        # Abrir archivo en modo escritura binaria
        with open(cls._archivo, "wb") as f:
            # Serializar y guardar los datos en el archivo
            pickle.dump(datos, f)

    # Método de clase para registrar un nuevo entrenador
    @classmethod
    def registrar(cls):
        # Cargar la lista actual de entrenadores
        entrenadores = cls._cargar()

        # Solicitar nombre de usuario y quitar espacios en blanco
        usuario = input("Usuario: ").strip()
        # Verificar si el usuario ya existe en el sistema
=======
import pickle

class EntrenadorDAO:
    _archivo = "entrenadores.bin"

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
    def registrar(cls):
        entrenadores = cls._cargar()

        usuario = input("Usuario: ").strip()
>>>>>>> b6f705b77ef221602d9b51533faaa2621a2172cd
        if usuario in entrenadores:
            print("Usuario ya existe")
            return

<<<<<<< HEAD
        # Solicitar contraseña y quitar espacios en blanco
        contrasena = input("Contraseña: ").strip()

        # Agregar el nuevo entrenador al diccionario
        entrenadores[usuario] = {"contrasena": contrasena}
        # Guardar los datos actualizados en el archivo
        cls._guardar(entrenadores)
        print("Entrenador registrado")

    # Método de clase para iniciar sesión de un entrenador
    @classmethod
    def iniciar_sesion(cls):
        # Cargar la lista actual de entrenadores
        entrenadores = cls._cargar()
        # Solicitar credenciales del usuario
        usuario = input("Usuario: ").strip()
        contrasena = input("Contraseña: ").strip()

        # Verificar si el usuario existe en el sistema
        if usuario in entrenadores:
            # Obtener los datos del usuario
            datos = entrenadores[usuario]
            # Verificar que los datos sean un diccionario y que la contraseña coincida
            if isinstance(datos, dict) and "contrasena" in datos and datos["contrasena"] == contrasena:
                print(f"Bienvenido {usuario}")
                # Retornar el nombre de usuario si el login es exitoso
                return usuario

        # Mostrar mensaje de error si las credenciales son incorrectas
        print("Usuario o contraseña incorrectos")
        # Retornar None si el login falla
=======
        contrasena = input("Contraseña: ").strip()

        entrenadores[usuario] = {"contrasena": contrasena}
        cls._guardar(entrenadores)
        print("Entrenador registrado")

    @classmethod
    def iniciar_sesion(cls):
        entrenadores = cls._cargar()
        usuario = input("Usuario: ").strip()
        contrasena = input("Contraseña: ").strip()

        if usuario in entrenadores:
            datos = entrenadores[usuario]
            if isinstance(datos, dict) and "contrasena" in datos and datos["contrasena"] == contrasena:
                print(f"Bienvenido {usuario}")
                return usuario

        print("Usuario o contraseña incorrectos")
>>>>>>> b6f705b77ef221602d9b51533faaa2621a2172cd
        return None
