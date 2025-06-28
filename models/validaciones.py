import re

def validar_cedula(cedula):
    return bool(re.fullmatch(r"001-\d{6}-\d{4}[A-Z]", cedula))

def validar_nombre(nombre):
    return bool(re.fullmatch(r"[A-Za-zÁÉÍÓÚáéíóúñÑ ]{2,50}", nombre.strip()))

def validar_apellido(apellido):
    return bool(re.fullmatch(r"[A-Za-zÁÉÍÓÚáéíóúñÑ ]{2,50}", apellido.strip()))

def validar_edad(edad):
    try:
        edad = int(edad)
        return 15 <= edad <= 50
    except:
        return False

def validar_telefono(telefono):
    return bool(re.fullmatch(r"\d{8}", telefono))

def validar_peso(peso):
    try:
        peso = float(peso)
        return 30 <= peso <= 200
    except:
        return False

def validar_altura(altura):
    try:
        altura = float(altura)
        return 100 <= altura <= 250
    except:
        return False

def validar_posicion(posicion):
    posiciones = ['Base', 'Escolta', 'Alero', 'Ala-pivot', 'Pivot']
    return posicion in posiciones

