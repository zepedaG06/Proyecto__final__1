def validar_cedula(cedula: str) -> bool:
    cedula_limpia = cedula.replace("-", "").replace(" ", "")
    return (cedula_limpia.isdigit() and 
            (6 <= len(cedula_limpia) <= 8 or len(cedula_limpia) == 13))

def validar_nombre(nombre: str) -> bool:
    return nombre.replace(" ", "").isalpha()
