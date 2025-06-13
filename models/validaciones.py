def validar_cedula(cedula: str) -> bool:
    cedula_limpia = cedula.replace("-", "").replace(" ", "")
    return cedula_limpia.isdigit() and (6 <= len(cedula_limpia) <= 8 or len(cedula_limpia) == 13)

def validar_nombre(nombre: str) -> bool:
    return bool(nombre.strip()) and all(c.isalpha() or c.isspace() for c in nombre)

def validar_apellido(apellido: str) -> bool:
    return validar_nombre(apellido)

def validar_edad(edad: str) -> bool:
    if not edad.isdigit():
        return False
    val = int(edad)
    return 5 <= val <= 100

def validar_telefono(telefono: str) -> bool:
    return telefono.isdigit() and len(telefono) == 8

def validar_peso(peso: str) -> bool:
    try:
        val = float(peso)
        return 30 <= val <= 200
    except ValueError:
        return False

def validar_altura(altura: str) -> bool:
    try:
        val = float(altura)
        return 100 <= val <= 250
    except ValueError:
        return False

def validar_antecedentes(antecedentes: str) -> bool:
    return True

