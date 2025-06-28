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
        if usuario in entrenadores:
            print("Usuario ya existe")
            return

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
        return None
