#IF..ELIF..ELSE --------------------------------------------------------------------------------------------------------------------------------------------------------->
#CONDICIONALES EN PYTHON Y DECLARACION 'IF':
'''
Python admite las condiciones logicas habituales de las matematicas
	Iguales : [a == b]
	No Iguales : [a != b]
	Menos que : [a < b]
	Menos o igual a : [a <= b]
	Mayor que : [a > b]
	Mayor o igual a : [a >= b]
Estas condiciones se pueden usar de varias maneras, mas comunmente 
en declaraciones 'si' y los bucles
Se escribe una declaracion 'si' usando la palabra clave 'if'
'''
a = 33
b = 200
if b > a:
  print("b is greater than a") #b is greater than a

#IDENTACION
''' Python se basa en la sangria(espacio en blanco desde el comienzo de una linea)
para definir el alcance el el codigo. Otros lenguagees de programacion a menudo
usan llaves para este propocito 
a = 33
b = 200
if b > a:
print("b is greater than a") # you will get an error '''

#ELIF
''' La palabra clave 'elif' es la forma en que python dice: 
"si las condiciones anteriores no eran ciertas, entonces prueba esta condicion" '''
a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal") #a and b are equal

#ELSE
''' La palabra clave 'else' atrapa cualquier cossa que no sea atrapada
por las condiciones anteriores'''
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b") #a is greater than b
#Tambien puedes tener un 'else' sin 'elif'
a = 200
b = 33
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a") #b is not greater than a

#FORMA CORTA 'IF'
''' Si solo tiene una instruccion que ejecutar, puede ponerla en la misma
linea que la instruccin 'if' '''
if a > b: print("a is greater than b") #a is greater than b

#FORMA CORTA 'IF..ELSE' (OPERADOR TERNARIO)
''' Si solo tiene una instruccion para ejecutar, una para si y otra para otra, 
puede ponerla todo en la misma linea'''
a = 2
b = 330
print("A") if a > b else print("B") #B
#Esta tecnica se conoce como OPERADORES TERNARIOS, o expreciones condicionales
#Tambien puede tener varias declaracionesen la misma linea:
a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B") #=

#AND
#La palabra clave 'and' es un operador logico, se utiliza para combinar declaraciones condicionales
a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True") #Both conditions are True

#OR
#La palabra clave 'or' es un operador logico,y es utilizado para combinar declaraciones condicionales
a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True") #At least one of the conditions is True

#NOT
#La palabra clave 'not' es un operador logico, y es usado para revertir el resultado de las declaraciones condicionales
a = 33
b = 200
if not a > b:
  print("a is NOT greater than b") #a is NOT greater than b

#IF ANIDADO
#Puedes tener declaraciones 'if' dentro de otras declaraciones 'if', esto se llama 'declaraciones 'if' anidados
x = 41
if x > 10:
  print("Above ten,") #Above ten,
  if x > 20:
    print("and also above 20!") #and also above 20!
  else:
    print("but not above 20.")

#Declaracion de aprobacion
''' Las declaraciones 'if' no pueden estar vacias, pero si usted por alguna razon tener una 
declaracion sin contenido, poner la declaracion 'pass' para evitar obtener error'''
a = 33
b = 200

if b > a:
  pass