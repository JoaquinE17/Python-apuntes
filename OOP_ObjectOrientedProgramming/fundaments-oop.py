#OPP-FUNDAMENTOS ------------------------------------------------------------------------------------------------------------------------------>
''' Los fundmentos de la Programacion Orientada a Objetos (OOP) son los pilares de la sobre los
cuales se construye este paradigma de programacion. Los principales fundamentos son: 

1. CLASES Y OBJETOS:
^^^^^^^^^^^^^^^^^^^^
	*clase : Es una plantilla o molde que define los atributos y comportamientos (metodos)
	 comunes de un tipo de objeto. Se pueden pensar como un 'Tipo de dato' personalizado.
	*objeto : Es una instancia de un clase. Cada objeto tiene su propio conjunto de atributos
	 y puede ejecutar los metodos definidos en la clase.'''
class Persona:                              #} Clase
    def __init__(self, nombre, edad):       #} Metodo principal
        self.nombre = nombre                #} Propiedad
        self.edad = edad                    #} Propiedad

    def saludar(self):                      #} Metodo (adicional)
        print(f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años.")        #}Propiedad

# Crear un objeto de la clase Persona 
p1 = Persona("Juan", 30)                    #} Objeto
p1.saludar()  #Hola, mi nombre es Juan y tengo 30 años.

'''
2. ENCAPSULAMIENTO:
^^^^^^^^^^^^^^^^^^^
	El encapsulamiento es el principio de ocutar los detalles internos de una clase y solo
	exponer lo necesario a traves de metodos publicos. Esto ayuda a proteger los datos y 
	controlar como se accede o modifica la informacion dentro de la clase.
		*Atributos privados: Aunque python no tiene un mecanismo de privacidad estricta, se 
		 utiliza la convencion de colocar un guion bajo '_' para indicar que un atributo o 
		 metodo es privado, y no debe ser accesible directamente desde fuera de la clase.'''
class CuentaBancaria:
    def __init__(self, saldo_inicial):
        self._saldo = saldo_inicial  # Atributo privado

    def depositar(self, cantidad):
        if cantidad > 0:
            self._saldo += cantidad

    def consultar_saldo(self):
        return self._saldo

p1 = CuentaBancaria(500)
p1.depositar(23)
print(p1.consultar_saldo()) #523

'''
3. HERENCIA:
^^^^^^^^^^^^
	La herencia es un mecanismo que permite a un clase (subclase) heredar atributos y metodos
	de otra clase (superclase). Esto permite reutilizar codigo y crear jerarquias de clases.
		*Subclase: Es la clase que hereda otra
		*Superclase: Es la clase de la cual se heredan los atributos y metodos. '''
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        pass

class Perro(Animal):
    def hablar(self):
        return "Guau"

class Gato(Animal):
    def hablar(self):
        return "Miau"

perro = Perro("Rex")
gato = Gato("Miau")

print(perro.hablar())  #Guau
print(gato.hablar())   #Miau

'''
4.POLIMORFISMO:
^^^^^^^^^^^^^^^
	El polimorfismo permite que diferentes clases sean tratadas de manera uniforme, ya que 
	pueden compartir el mismo metodo, pero cada una puede implementar su propia vercion del 
	metodo. En otras palabras, es la capacidad de usar un mismo metodo (interfaces) para objetos de 
	diferentes tipos. '''
class Ave:
    def volar(self):
        print("El ave está volando")

class Murcielago(Ave):
    def volar(self):
        print("El murciélago está volando en la oscuridad")

ave = Ave()
murcielago = Murcielago()

ave.volar()  #El ave está volando
murcielago.volar()  #El murciélago está volando en la oscuridad

'''
5. ABSTRACCION: [ver a profundidad]
^^^^^^^^^^^^^^^
	La abstraccion es el proceso de ocultar la complejidad y mostrar solo la informacion 
	esencial. Esti se logra mediante el uso de clases abstractas o interfaces (metodos), 
	donde se definen metodos que deben ser implementados en la subclases, pero no se 
	especifica su implementacion en la clase base.
		*En python, se puede usar el modulo 'abc' (Abstract Base Classes) para definir
		 clases abstractas '''
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def hacer_sonido(self):
        pass

class Perro(Animal):
    def hacer_sonido(self):
        print("Guau")

perro = Perro()
perro.hacer_sonido()  #Guau

'''
Resumen de los fundamentos:
# Clases y Objetos : Los bloques básicos de OOP. Las clases definen cómo serán los objetos
  y los objetos son instancias de esas clases.
# Encapsulamiento : Oculta los detalles internos y solo expone lo necesario a través de métodos.
# Herencia : Permite que una clase herede características de otra, facilitando la reutilización 
  de código.
# Polimorfismo : Permite que diferentes clases usen métodos con el mismo nombre, pero con 
  implementaciones distintas.
# Abstracción : Oculta la complejidad y expone solo lo necesario, utilizando clases abstractas.

Dominar estos conceptos es clave para entender y aplicar correctamente la programación orientada a objetos en Python (y en otros lenguajes).

###########################################################################################################################
#   Cuando el metodo de la clase tiene la propiedad 'print(...)' se llama solo al metodo -> ['<variable>.<metodo>()']     #
#   En cambio si el propiedad del metodo en un 'return...' es necesario usar el print -> [print(<variable>.<metodo>())]   #
###########################################################################################################################
