class Persona:
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apeliido = apellido
        self.edad = edad

    def mostrar_detalle (self):
        print (f'Persona : {self.nombre} {self.apeliido} {self.edad}')

persona1 = Persona('carlos', 'Perez', 29)
persona1.mostrar_detalle()