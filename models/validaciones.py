import re
import unicodedata

def quitar_tildes(texto):
    return ''.join(
        c for c in unicodedata.normalize('NFD', texto)
        if unicodedata.category(c) != 'Mn'
    )

def validar_cedula(cedula):
    if len(cedula) < 1:
        return False
    cedula = cedula[:-1] + cedula[-1].upper()
    return bool(re.fullmatch(r"001-\d{6}-\d{4}[A-Z]", cedula))

def formatear_cedula(cedula):
    if len(cedula) < 1:
        return cedula
    return cedula[:-1] + cedula[-1].upper()

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
        peso = peso.replace(',', '.')
        peso = float(peso)
        return 30 <= peso <= 200
    except:
        return False

def parsear_peso(peso):
    peso = peso.replace(',', '.')
    return float(peso)

def validar_altura(altura):
    try:
        altura = altura.replace(',', '.')
        altura_f = float(altura)
        if altura_f < 10:
            altura_f *= 100
        return 100 <= altura_f <= 250
    except:
        return False

def parsear_altura(altura):
    altura = altura.replace(',', '.')
    altura_f = float(altura)
    if altura_f < 10:
        altura_f *= 100
    return altura_f

def validar_posicion(posicion):
    posiciones_validas = ['base', 'escolta', 'alero', 'ala-pivot', 'pivot']
    posicion_norm = quitar_tildes(posicion.lower())
    return posicion_norm in posiciones_validas

def formatear_posicion(posicion):
    map_pos = {
        'base': 'Base',
        'escolta': 'Escolta',
        'alero': 'Alero',
        'ala-pivot': 'Ala-pívot',
        'pivot': 'Pívot'
    }
    posicion_norm = quitar_tildes(posicion.lower())
    return map_pos.get(posicion_norm, None)

