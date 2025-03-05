#INHERITANCE (HERENCIA) ----------------------------------------------------------------------------------------------------------------------------------->
''' La 'herencia' nos permite definir una clase que hereda todos los metodos y propiedades 
de otra clase.
	## Clase padre: es la clase de la que se hereda, tambien llamada clase base.
	## Clase hijo: es la clase que hereda de otra clase, tambien llamada clase derivada.

### CREAR UNA CLASE PADRE
Cualquier clase puede ser una clase principal, por lo que la sintaxis es la misma que 
crea cualquier otra clase. '''
#Crea una clase llamada 'Person', con propiedades 'firstname' y 'lastname' y un metodo 'printname':
class Person:
	def __init__(self, fname, lname):
		self.firstname = fname
		self.lastname = lname

	def printname(self):
		print(self.firstname, self.lastname)

x = Person("John", "Doe")
x.printname()

### CREAR UNA CLASE HIJO
''' Para crear una clase que herede la funcionalidad de otra clase, envíe la clase padre como 
parámetro al crear el clase hijo: '''
#Crea una clase llamada Student, que heredará las propiedades y métodos de la clase Person
class Student(Person):
	pass # Usa la palabra clave 'pass' cuando no desea agregar otras propiedades o métodos al clase.

#Ahora la clase Student tiene las mismas propiedades y métodos que la clase Person.
#Usa el Student clase para crear un objeto, y luego ejecutar el printname método:
x = Student('Myke','Olsen')
x.printname() 

### AGREGAR LA FUNCION __INIT__()
#Hasta ahora hemos creado una clase hijo que hereda las propiedades y los métodos de su padre.
#Queremos agregar la funcion '__init__()' a la clase hijo (en lugar de la palabra clave 'pass').

