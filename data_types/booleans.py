#BOOLEAN TYPES -------------------------------------------------------------------------------------------------------------------------------->

#Valores booleanos (true o false)
print(19>10) #True
print(19==10) #False
print(19<10) #False

#Boleanos en los 'if'
a=43
b=23
if a<b:
	print("Lunes")
else:
	print("Martes")

#Evaluar variables
c=23.123
print(bool(c)) #True
print(bool("hola")) #True
print(bool(12)) #True
print(bool(["apple", "cherry", "banana"])) #True
#La mayoria de las variables son 'true' exepto los valores vacios
print(bool(False)) #False
print(bool(None)) #False
print(bool(0)) #False
print(bool("")) #False
print(bool(())) #False
print(bool([])) #False
print(bool({})) #False

#Uso de class u objeto con funcion __len__ retorna 0 o false
class my_class():
	def __len__(self):
		return 0
my_objet=my_class()
print("class ==",bool(my_objet)) #class == False

#Funciones retornan booleanos
def my_funtion():
	return True
print("funtion ==",my_funtion()) #funtion == True

def myFunction() :
  return True

if myFunction():
  print("YES!") #YES!
else:
  print("NO!")

#Otras funciones que retornan booleanos
#[isinstance()] -> Determina si un objeto es de un determinado tipo de datos
x = 200
print(isinstance(x, int)) #True
