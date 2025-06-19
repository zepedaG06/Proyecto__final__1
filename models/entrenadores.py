import shelve

DB_ENTRENADORES = "data/entrenadores_db"

def registrar_entrenador():
    with shelve.open(DB_ENTRENADORES) as db:
        usuario = input("Usuario: ").strip()
        if usuario in db:
            print("Usuario ya existe.")
            return
        contrasena = input("Contraseña: ").strip()
        db[usuario] = contrasena
        print(f"Entrenador {usuario} registrado.")

def iniciar_sesion():
    with shelve.open(DB_ENTRENADORES) as db:
        usuario = input("Usuario: ").strip()
        contrasena = input("Contraseña: ").strip()
        if usuario in db and db[usuario] == contrasena:
            print(f"Bienvenido, {usuario}!")
            return usuario  
        print("Usuario o contraseña incorrectos.")
        return None
