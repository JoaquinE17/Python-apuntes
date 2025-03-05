#WHILE ---------------------------------------------------------------------------------------------------------------------------------->
'''Puede recorrer los elementos de la lista utilizando el bucle 'while'.
Usa la funcion 'len()' para determinar la longitud de la lista, luego 
inicialise una variable en '0' y recorra los elementos de la lista refiriéndose a sus índices.
Recuerde aumentar la varuable en 1 después de cada iteración.'''
frutas = ['careza', 'banana', 'peras', 'mango']
i = 0
while i < len(frutas):
  print(frutas[i])
  i = i + 1

#Con el mientras loop podemos ejecutar un conjunto de declaraciones siempre que una condición sea verdadera.
i = 1
while i < 6:
  print(i)
  i += 1
#Recuerde incrementar 'i', o de lo contrario el bucle continuará para siempre.
'''El mientras loop requiere que las variables relevantes estén inisializadas, en este 
ejemplo necesitamos definir una variable de indexación 'i', que establecemos en 1'''

#Declaracion 'break'
#Con la declaración 'break' podemos detener el bucle incluso si la condición de 'while' es verdadera:
i = 1
while i < 6:
  print(i) #1 \n2 \n3
  if i == 3:
    break
  i += 1

#Declaracion 'continue'
#Con la declaración 'continue' podemos detener el iteración actual, y continuar con la siguiente:
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i) #1 \n2 \n4 \n5 \n6

#Declaracion 'else'
#Con la declaracion 'else' podemos ejecutar un bloque de código una vez cuando la condición ya no es cierta:
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("La variable 'i' llego a 6")

#FOR ------------------------------------------------------------------------------------------------------------------------------------>
alumnos = ['pablo', 'lautaro', 'romina', 'hector', 'laura']
for i in alumnos:
	print(i) #pablo \nlautaro \nromina \nhector \nlaura
#También puede recorrer los elementos de la lista haciendo referencia a su número de índice.
#Usa el range() y len() funciones para crear un iterable adecuado.
alumnos = ['pablo', 'lautaro', 'romina', 'hector', 'laura']
for i in range(len(alumnos)):
	print(alumnos[i]) #pablo \nlautaro \nromina \nhector \nlaura

'''El bucle 'for' se usa para iterar sobre una secuencia (que puede ser una lista, una tupla, o un diccionario, un set o un string).
Esto se parece menos a la palabra clave for en otros lenguajes de programación y funciona más como un método iterador como el 
que se encuentra en otros lenguajes de programación orientados a objetos.
Con el bucle 'for' podemos ejecutar un conjunto de sentencias, una vez por cada elemento de una lista, tupla, set etc.
El bucle 'for' no requiere una variable de indexación para establecer de antemano.'''

#Con el 'break' podemos detener el bucle antes de que haya recorrido todos los elementos:
alumnos = ['pablo', 'lautaro', 'romina', 'hector', 'laura']
for x in alumnos:
	print(x) #pablo \nlautaro \nromina
	if x == 'romina':
		break #Corta el bucle

#Con el 'continue' podemos detener el iteración actual del bucle, y continuar con el siguiente:
alumnos = ['pablo', 'lautaro', 'romina', 'hector', 'laura']
for x in alumnos:
  if x == "romina":
    continue
  print(x) #pablo \nlautaro \nhector \nlaura

'''La función range()
Para recorrer un conjunto, un número específico de veces, podemos usar la funcion 'range()'.
El range() devuelve una secuencia de números, comenzando desde 0 por defecto, e incrementa en 1 (por defecto), 
y termina en un número especificado.'''
for x in range(6):
	print(x) #0 \n1 \n2 \n3 \n4 \n5
#Tenga en cuenta que rango(6) no son los valores de 0 a 6, sino los valores de 0 a 5.
#La funcion 'range()' por defecto es 0 su valor inicial, sin embargo, es posible especificar el valor inicial 
#agregando un parámetro: rango(2, 6),es decir, valores medios entre 2 y 6 (pero sin incluir 6):
for x in range(2,6):
	print(x) #2 \n3 \n4 \n5
#La función range() por defecto aumenta la secuencia en 1, sin embargo, es posible especificar el valor 
#de incremento agregando un tercer parámetro: rango(2, 30, 3):
for x in range(2,6,2):
	print(x) #2 \n4 

#Uso de 'else' en bucle 'for'
#La palabra clave 'else' en el bucle 'for' especifica un bloque de código a ser ejecutado cuando el bucle está terminado:
for x in range(6):
  print(x) #0 \n1 \n2 \n3 \n4 \n5
else:
  print("Finalizado") #Finalizado
#El bloque 'else' NO se ejecutará si el bucle es detenido por la declaración 'break'.
for x in range(6):
	if x == 3:break
	print(x) #0 \n1 \n2
else:
  print("Finalizado") #No imprime esta linea

#Bucles anidados:
#Un bucle anidado es un bucle dentro de un bucle.
#El "bucle interno" se ejecutará una vez para cada iteración del "bucle exterior":
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]
for x in adj:
  for y in fruits:
    print(x, y) #red apple \nred banana \nred cherry \nbig appel... \ntasty apple...

#Declaracion 'pass':
#Los bucles 'for' no pueden estar vacíos, pero si es por alguna razón tiene un bucle 'for' sin contenido,
#poner en la declaración 'pass' para evitar obtener un error.
for x in [0, 1, 2]:
  pass

