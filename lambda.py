#LAMBDA -------------------------------------------------------------------------------------------------------------------------->
'''
Es una pequeña funcion anonima
Una funcion lambda puede tomar cualquier numero de argumentos, pero solo puede tener una exprecion
Sintaxis:
	lambda argumens : expression
'''
x = lambda a : a +10
print(x(5)) #5

#La funcion lambda puedentomar cualquier numero de argumentos
x = lambda a, b : a * b
print(x(5, 6)) #30
x = lambda a, b, c : a + b + c
print(x(5, 6, 2)) #13

#Porque usar las funciones lambda?
'''
El poder de lambda se muestra mejor cuando los usas como una funcion anonima 
dentro de otra funcion
Digamos que tiene una definicion de funcion que toma un argumento y ese
argumento se multiplicara con un numero desconocido:
	def myfunc(n):
  		return lambda a : a * n
Utilice esa definicion de funcion para hacer una funcion que siempre duplica
el numero que se envia:
'''
def myfunc(n):
  return lambda a : a * n
mydoubler = myfunc(2)
print(mydoubler(11)) #22

#O bien, usa la misma definicion de funcion para hacer una funcion que siempre
#triplique el numero que envia
def myfunc(n):
  return lambda a : a * n
mytripler = myfunc(3)
print(mytripler(11)) #33

#O use la misma definicion de funcion para hacer ambas funciones, en la misma funcion
def myfunc(n):
  return lambda a : a * n
mydoubler = myfunc(2)
mytripler = myfunc(3)
print(mydoubler(11)) #22
print(mytripler(11)) #33

#Use funciones lambda cuando se requiera una función anónima por un corto período de tiempo