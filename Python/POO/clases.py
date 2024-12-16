
#Ejemplo 
# Clases
# fundamentos de programación orientada a objetos

"""
Existen cuatro tipos de notación

Camel Case -> contarElementos

Pascal Case -> ContarElementos

Snake Case -> contar_elementos

Kebab Case -> contar-elementos

"""


edad1 = 27
class Persona :
    # Primero los atributos de la clase

    # Constructor
    def __init__(self, nombre, edad, altura) :
        self.nombre = nombre
        self.edad = edad
        self.altura = altura

    def leer_edad(self) :
        return self.nombre + " tiene " + str(self.edad) + " años"

jesus = Persona("Jesús", 27, 1.75)
print(jesus.leer_edad())
print(jesus.altura)

mari = Persona("Mari", 25, 1.60)
print(mari.leer_edad())
print(mari.altura)

print("--------------------------------------")

#Ejercicio 

#Creacion de la clase 
class carro :
    #atributos 
            # EL CONSTRUCTOR 
    def __init__(self, marca, modelo, año):
        #self es imprante por el scope
        self.marca = marca 
        self.modelo = modelo 
        self.año = año
    #
    def mostrar_informacion(self):
        return "Marca:" + self.marca + ", Modelo : " + self.modelo + ", Año: " + self.año
    
#Asignar algunos datos
mi_carro = carro("Toyota", "Corolla", "2020")
print(mi_carro.mostrar_informacion())

su_carro = carro("Honda" , "Civic", "2018")
print(su_carro.mostrar_informacion())
