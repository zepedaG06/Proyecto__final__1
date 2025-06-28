class Jugador:
    def __init__(self, cedula, nombre, apellido, edad, telefono, peso, altura, antecedentes, posicion):
        self.cedula = cedula
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.telefono = telefono
        self.peso = peso
        self.altura = altura
        self.antecedentes = antecedentes
        self.posicion = posicion
        self.asistencias = 0
        self._calcular_imc()

    def _calcular_imc(self):
        altura_m = self.altura / 100
        self.imc = round(self.peso / (altura_m ** 2), 2)

    def __str__(self):
        return (f"\n=== DATOS DEL JUGADOR ===\n"
                f"Cédula: {self.cedula}\n"
                f"Nombre: {self.nombre} {self.apellido}\n"
                f"Edad: {self.edad} años | Teléfono: {self.telefono}\n"
                f"Peso: {self.peso}kg | Altura: {self.altura}cm\n"
                f"Posición: {self.posicion}\n"
                f"IMC: {self.imc} | Asistencias: {self.asistencias}\n"
                f"Antecedentes: {self.antecedentes}\n" + "=" * 30)
