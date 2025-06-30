# Definir la clase Jugador que representa a un jugador de básquet
class Jugador:
    # Constructor que inicializa un objeto Jugador con todos sus atributos
    def __init__(self, cedula, nombre, apellido, edad, telefono, peso, altura, antecedentes, posicion):
        # Asignar la cédula de identidad del jugador
        self.cedula = cedula
        # Asignar el nombre del jugador
        self.nombre = nombre
        # Asignar el apellido del jugador
        self.apellido = apellido
        # Asignar la edad del jugador
        self.edad = edad
        # Asignar el número de teléfono del jugador
        self.telefono = telefono
        # Asignar el peso del jugador en kilogramos
        self.peso = peso          
        # Asignar la altura del jugador en centímetros
        self.altura = altura      
        # Asignar los antecedentes médicos del jugador
        self.antecedentes = antecedentes
        # Asignar la posición que juega en el equipo
        self.posicion = posicion
        # Calcular y asignar el IMC automáticamente al crear el objeto
        self.imc = self.calcular_imc()  

    # Método para calcular el Índice de Masa Corporal del jugador
    def calcular_imc(self):
        # Convertir altura de centímetros a metros
        altura_m = self.altura / 100  
        # Verificar que la altura sea mayor a 0 para evitar división por cero
        if altura_m > 0:
            # Fórmula del IMC: peso / (altura en metros)²
            return self.peso / (altura_m ** 2)
        else:
            # Retornar 0 si la altura es inválida
            return 0.0

    # Método especial para convertir el objeto a string (representación textual)
    def __str__(self):
        # Retornar una cadena formateada con todos los datos del jugador
        return (f"\n=== DATOS DEL JUGADOR ===\n"
                f"Cédula: {self.cedula}\n"
                f"Nombre: {self.nombre} {self.apellido}\n"
                f"Edad: {self.edad} años | Teléfono: {self.telefono}\n"
                f"Peso: {self.peso}kg | Altura: {self.altura}cm\n"
                f"Posición: {self.posicion}\n"
                f"IMC: {self.imc:.2f}\n"
                f"Antecedentes: {self.antecedentes}\n"
                + "=" * 30)

