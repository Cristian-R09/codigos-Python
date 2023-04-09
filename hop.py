class Persona : 
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    def __str__(self) :
        return  print(f'persona: {self.nombre} {self.apellido} tiene {self.edad} años')
                      
    
persona1 = Persona('carlos' , 'Ramirez', 49)

# print(persona1)
