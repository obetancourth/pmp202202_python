class Cliente:
    nombre = ""
    edad = ""
    telefono = ""
    correo = ""
    id = 0

    def __init__(self, nombre, edad, telefono, correo):
        self.nombre = nombre
        self.edad = edad
        self.telefono = telefono
        self.correo = correo

    def to_string(self):
        return self.nombre + " (" + str(self.edad) + ")"
