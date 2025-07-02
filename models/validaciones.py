# Importar módulo para expresiones regulares (patrones de texto)
import re
# Importar módulo para manejo de caracteres Unicode (tildes, acentos)
import unicodedata

# Función para eliminar tildes y acentos de un texto
def quitar_tildes(texto):
    # Normalizar el texto a forma NFD (descomposición canónica)
    # Filtrar solo caracteres que no sean marcas diacríticas (tildes/acentos)
    # Unir todos los caracteres filtrados en una sola cadena
    return ''.join(
        c for c in unicodedata.normalize('NFD', texto)
        if unicodedata.category(c) != 'Mn'
    )

# Función para validar formato de cédula dominicana
def validar_cedula(cedula):
    # Verificar que la cédula no esté vacía
    if len(cedula) < 1:
        return False
    # Formatear la cédula: todo en minúscula excepto la última letra en mayúscula
    cedula = cedula[:-1] + cedula[-1].upper()
    # Verificar que coincida con el patrón: 001-XXXXXX-XXXXA (donde X=dígito, A=letra)
    return bool(re.fullmatch(r"001-\d{6}-\d{4}[A-Z]", cedula))

# Función para formatear una cédula poniendo la última letra en mayúscula
def formatear_cedula(cedula): 
    # Verificar que la cédula no esté vacía
    if len(cedula) < 1:
        return cedula
    # Retornar la cédula con la última letra en mayúscula
    return cedula[:-1] + cedula[-1].upper()

# Función para validar que un nombre sea válido
def validar_nombre(nombre):
    # Verificar que coincida con el patrón: solo letras, espacios y acentos, entre 2-50 caracteres
    return bool(re.fullmatch(r"[A-Za-zÁÉÍÓÚáéíóúñÑ ]{2,50}", nombre.strip()))

# Función para validar que un apellido sea válido
def validar_apellido(apellido):
    # Verificar que coincida con el patrón: solo letras, espacios y acentos, entre 2-50 caracteres
    return bool(re.fullmatch(r"[A-Za-zÁÉÍÓÚáéíóúñÑ ]{2,50}", apellido.strip()))

# Función para validar que una edad sea válida
def validar_edad(edad):
    try:
        # Intentar convertir la edad a entero
        edad = int(edad)
        # Verificar que esté en el rango de 15 a 50 años
        return 15 <= edad <= 50
    except:
        # Si hay error en la conversión, retornar False
        return False

# Función para validar que un teléfono sea válido
def validar_telefono(telefono):
    # Verificar que coincida con el patrón: exactamente 8 dígitos
    return bool(re.fullmatch(r"\d{8}", telefono))

# Función para validar que un peso sea válido
def validar_peso(peso):
    try:
        # Reemplazar comas por puntos para el formato decimal
        peso = peso.replace(',', '.')
        # Convertir a número decimal
        peso = float(peso)
        # Verificar que esté en el rango de 30 a 200 kg
        return 30 <= peso <= 200
    except:
        # Si hay error en la conversión, retornar False
        return False

def validar_altura(altura):
    try:
        # Reemplazar comas por puntos para el formato decimal
        altura = altura.replace(',', '.')
        # Convertir a número decimal
        altura_f = float(altura)
        # Si la altura es menor a 10, asumir que está en metros y convertir a cm
        if altura_f < 10:
            altura_f *= 100
        # Verificar que esté en el rango de 100 a 250 cm
        return 100 <= altura_f <= 250
    except:
        # Si hay error en la conversión, retornar False
        return False

# Función para validar que una posición de básquet sea válida
def validar_posicion(posicion):
    # Lista de posiciones válidas en básquetbol
    posiciones_validas = ["Base", "Escolta", "Alero", "Ala-Pívot", "Pívot"]
    # Normalizar la posición: quitar tildes y convertir a minúscula
    posicion_norm = quitar_tildes(posicion.lower())
    # Intenta convertir la posición ingresada a su formato correcto
    # (sin tildes, en minúsculas y comparando con el mapeo)
    return formatear_posicion(posicion) is not None

# Función para formatear una posición a su forma correcta
def formatear_posicion(posicion):
    # Diccionario de mapeo de posiciones normalizadas a formato correcto
    map_pos = {
        'base': 'Base',
        'escolta': 'Escolta',
        'alero': 'Alero',
        'ala-pivot': 'Ala-pívot',
        'pivot': 'Pívot'
    }
    # Normalizar la posición: quitar tildes y convertir a minúscula
    posicion_norm = quitar_tildes(posicion.lower())
    # Buscar en el diccionario y retornar la forma correcta, o None si no existe
    return map_pos.get(posicion_norm, None)

# Función para validar que los antecedentes médicos sean válidos
def validar_antecedentes(antecedentes):
    # Limpiar espacios y convertir a minúscula
    antecedentes = antecedentes.strip().lower()
    # Validar: debe ser "si", "no" o tener al menos 2 caracteres de descripción
    return antecedentes in ["si", "no"] or len(antecedentes) >= 2

