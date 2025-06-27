import re

def validar_cedula(cedula: str) -> bool:
    """
    Valida cédula de identidad nicaragüense.
    Formato: 001-DDMMYY-NNNNG donde:
    - 001: Código de país (Nicaragua)
    - DDMMYY: Fecha de nacimiento (día, mes, año)
    - NNNN: Número secuencial
    - G: Dígito verificador (A-Z)
    """
    cedula_limpia = cedula.replace("-", "").replace(" ", "")
    # Patrón adaptado para sistema nicaragüense
    patron = r'^001\d{6}\d{4}[A-Z]$'
    return bool(re.match(patron, cedula_limpia.upper()))

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
    """
    Valida número telefónico nicaragüense.
    Formato: 8 dígitos (sistema nacional)
    Ejemplo: 85471234, 22501234
    """
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

def validar_posicion(posicion: str) -> bool:
    """
    Valida la posición del jugador en la cancha de baloncesto.
    Posiciones válidas: Base, Escolta, Alero, Ala-Pívot, Pívot
    """
    posiciones_validas = {
        "base", "escolta", "alero", "ala-pivot", "ala-pívot", "pivot", "pívot"
    }
    return posicion.lower().strip() in posiciones_validas

