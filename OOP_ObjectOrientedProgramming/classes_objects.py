#CLASSES AND OBJECTS -------------------------------------------------------------------------------------------------------------------------->
''' Class/objects:
Python es un lenguaje de programacion orientado a objetos. Casi todo en python es un objeto,
con sus propiedades y metodos. Una clase es como un constructor de objetos, o un "blueprint" 
para crear objetos'''

### CREAR UNA CLASS
#Para crear una clase, use la palabra clave 'class'
class MyClass:
	x = 5

### CREAR UN OBJECT
#Ahora podemos usar la clase llamada 'MyClass' para crear objetos
p1 = MyClass()
print(p1.x) #5

### LA FUNCION __INIT__():
''' Los ejemplos anteriores son clases y objetos en su forma simple, y no son realmente 
utiles en aplicaciones de la vida real.
Para entender el significado de las clases tenemos que entender la funcion incorporada
'__init__()'. Todas las clases tienen una funcion llamada de esta forma, que siempre se 
ejecuta cuando la clase esta siendo iniciada. Esta funcion se utiliza para asignar 
valores a propiedades de objetos u otras operaciones que son nesesarias para hacer 
cuando el objeto esta siendo creado. '''
class Persona:
	def __init__(self, nombre, edad):
		self.nombre = nombre
		self.edad = edad
p1 = Persona('Lucas',32)
print(p1.nombre)
print(p1.edad)

#EXPLICACION |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
'''
Estructura basica:
^^^^^^^^^^^^^^^^^
	class NombreClase:
		def __init__(self, Atributo1, Atributo2...):
			self.atributo1 = atributo1

	object = NombreClase(Atributo1, Atributo2)

Explicacion de class 'Persona':
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
1.Definición de la clase Persona:
	| class Persona:
Aquí estamos creando una clase llamada Persona. En programación orientada a objetos (OOP),
las clases se usan para definir un tipo de objeto que tiene ciertas características y 
comportamientos.

2.Metodo especial '__init__()':
	| def __init__(self, nombre, edad):
	|	self.nombre = nombre
	|	self.edad = edad
El método __init__ es un método especial de Python que se ejecuta automáticamente cuando se 
crea una nueva instancia (objeto) de la clase Persona. El propósito de __init__ es 
inicializar los valores de los atributos del objeto.
- self : Hace referencia a la instancia actual de la clase (el objeto que se está creando).
- nombre y edad : Son los parámetros que se pasan cuando creas un objeto de la clase.
- self.nombre = nombre : Asigna el valor de nombre al atributo nombre del objeto.
- self.edad = edad : Asigna el valor de edad al atributo edad del objeto.

3.Creacion de un objeto 'p1' de la clase 'Persona':
	| p1 = Persona('Lucas',32)
Aqui estamos creando un objeto de la clase Persona llamado p1. Al hacerlo, estamos llamando 
al metodo __init__, pasando 'Lucas' como valor para nombre y 32 como vaor para edad.
Despues de esta linea, el objeto p1 tiene los atributos nombre con el valor 'lucas' y edad 
con el valor 32.

4.Impresion de los atributos del objeto:
	| print(p1.nombre) #Lucas
	| print(p1.edad) #32
print(p1.nombre): Esto imprime el valor del atributo nombre del objeto p1, que es 'Lucas'.
print(p1.edad): Esto imprime el valor del atributo edad del objeto p1, que es 32.

Utiizacion del SELF:
^^^^^^^^^^^^^^^^^^^
¿Qué es self?
self es una referencia a la instancia actual de la clase. En otras palabras, cuando usas 
self dentro de un método de una clase, estás refiriéndote al objeto que ha sido creado a 
partir de esa clase.

¿Por qué es necesario?
Cuando defines una clase y creas instancias (objetos) de esa clase, cada instancia tiene 
sus propios atributos y comportamientos. Python usa self para que dentro de los métodos 
de la clase puedas referenciar y modificar esos atributos de una instancia específica de 
la clase.

¿Dónde se usa self?
self se usa principalmente en dos lugares dentro de una clase:

1. Dentro del constructor __init__: 
En el constructor, self se usa para almacenar los valores pasados cuando creas un objeto, 
asignándolos a los atributos de esa instancia.
	| def __init__(self, nombre, edad):
	|	self.nombre = nombre
	|	self.edad = edad
Aqui self.nombre y self.edad se refieren a los atributos del objeto que estamos creando.

2. Accediendo a los atributos y métodos de la instancia: Dentro de cualquier otro método 
de la clase, también puedes acceder a los atributos de la instancia utilizando self. De 
esta forma, puedes trabajar con los datos que pertenecen a esa instancia (objeto) particular.
	| def saludar(self):
	|	print(f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años.")
Aquí, self.nombre y self.edad se refieren a los atributos del objeto específico.

Para aclarar dudas:
Supon que tienes las siguiente clase (apartir de los dos anteriores)
	| class Persona:
	|     def __init__(self, nombre, edad):
	|         self.nombre = nombre
	|         self.edad = edad
	|     
	|     def saludar(self):
	|         print(f"Hola, soy {self.nombre} y tengo {self.edad} años.")

Ahora, si creas dos objetos de esa clase, cada uno tendra sus propios valores
para nombre y edad
	| p1 = Persona("Lucas", 32)
	| p2 = Persona("Ana", 25)
	| 
	| p1.saludar() #Hola, soy Lucas y tengo 32 años.
	| p2.saludar() #Hola, soy Ana y tengo 25 años.
En este caso:
[p1] tiene los atributos nombre como "Lucas" y edad como 32.
[p2] tiene los atributos nombre como "Ana" y edad como 25.
Cada vez que usas self, estás diciendo "la instancia que está siendo usada en este momento". 
Es una forma de asegurarte de que cada objeto tenga su propia información, sin mezclar los 
datos de diferentes instancias de la clase.

Ideas claras de SELF:
*** 'self' hace referencia al objeto actual (instancia de la clase).
*** Se usa para acceder o modificar los atributos y métodos de la instancia específica.
*** Es necesario en los métodos de una clase para poder trabajar con los atributos de 
	esa instancia, ya que cada objeto puede tener diferentes valores.
'''

### LA FUNCION __STR__():
''' La funcion '__str__()' controla lo que debe devolverse cuando el objeto de la clase 
se representa como una cadena.
Si la funcion no esta establecida, la reprecentacion de cadena del objeto se devuelve '''
# EJEMPLO: La representación de cadena de un objeto SIN el __str__() función:
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
p1 = Person("John", 36)
print(p1) #<__main__.Person object at 0x000001D2BCA22540> 

#EJEMPLO: La representación de cadena de un objeto CON el __str__() función:
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  def __str__(self):
    return f"{self.name}({self.age})"
p1 = Person("John", 36)
print(p1) #John(36)

### METODOS DE OBJETOS:
'''Los objetos también pueden contener métodos. Los métodos en los objetos son funciones 
que pertenece al objeto.'''
#Creemos un método en la clase Persona:
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  def myfunc(self):
    print("Hello my name is " + self.name)
p1 = Person("John", 36)
p1.myfunc() #Hello my name is John
''' El self parámetro es una referencia a la instancia actual de la clase, y se utiliza para 
acceder a las variables que pertenecen a la clase.'''

### AUTOPARAMETRO:
''' El parametro 'self' es una referencia a la instancia a la instancia actual de la clase,
y se utiliza para acceder a las variables que pertenecen a la clase.
No tiene que ser nombrado 'self', puedes llamarlo como quieras, pero tiene que ser el primer 
parametro de cualquier funcion en la clase '''
class Person:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age

  def myfunc(abc):
    print("Hello my name is " + abc.name)

  def __str__(self):
    return f"{self.name}({self.age})" 

p1 = Person("John", 36)
p1.myfunc() #Hello my name is John
print(p1) #John(36)

### MODIFICAR PROPIEDADES DEL OBJETO:
#Puede modificar propiedades en objetos como este:
p1.age = 40
print(p1) #John(40)

### ELIMINAR PROPIEDADES DEL OBJETO:
#Puede eliminar propiedades en objetos utilizando la palabra clave 'del'
del p1.age #Elimina la prodiedad age del obgeto p1

### ELIMINA OBJETOS:
#Puede eliminar objetos utilizando el del palabra clave
del p1

### DECLARACION PASS:
'''Las definiciones 'class' no pueden estar vacias, pero si por alguna razon
tienes un 'class' sin contenido, colocando una declaracion 'pass' evita los 
errores que ocaciona'''
class Persona:
	pass


Persona1 = Person('joaquin',25)
print(Persona1)