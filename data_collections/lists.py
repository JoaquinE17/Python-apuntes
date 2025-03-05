#LISTAS -------------------------------------------------------------------------------------------------------------------------------------->
'''
Se utilizan para almacenar múltiples elementos en una sola variable.
Son uno de los 4 tipos de datos integrados en Python utilizados para almacenar colecciones de datos, 
los otros 3 son Tuplas, Sets, y Diccionarios, todos con diferentes cualidades y uso.
Las listas se crean utilizando corchetes('[]'):
'''
frutas=['bananas','arandanos','ciruelas',12]
print(frutas) #['bananas','arandanos','ciruelas',12]
print(type(frutas)) #<class 'list'>

'''
Los elementos de la lista se ordenan, se pueden modificar y permiten valores duplicados
Estos elementos se encuentran indexados, es decir que el primer elemento se encuentra en la pocicion '0', 
el siguiente en el '1' y asi sucesivamente.
	Ordenados: Significa que lo elementos tienen un orden definido y ese orden no cambiara.
			   Si se agrega nuevos elementos a una lista, estos se agregaran al final de la lista.
	Modificables: Significa que podemos cambiar, agregar y eliminar elementos en una lista después de 
				  que se haya creado.
	Valores duplicados: Dado que las listas están indexadas, las listas pueden tener elementos con el mismo valor.
'''

#LONGITUD DE LISTA
#Para determinar cuantos elementos tiene una lista, se utiliza la funcion len()
frutas={'peras','bananas','naranjas','manzanas'}
print(len(frutas)) #4

#ELEMENTOS
#Los elementos de la lista pueden ser de cualquier tipo de datos:
#Cadenas, int, float
lista1 = ['manzana','banana','arandanos']
lista2 = [1,2,4,5,7,3]
lista3 = [True,False,True]

#Una lista puede contener diferentes tipos de datos
lista1 = ['abc',34,True,23.3,'23']

#type() -> las listas se definen como objetos con el tipo de datos 'lista'
print(type(lista1))

#list() -> Es posible usar el cinstructor list() para crear una nueva lista
lista1 = list(('manzana','mandarinas',12,True))
print(lista1)

#ACCESO A LOS ELEMENTOS DE UNA LISTA --------------------------------------------------------------------------------------------------------> 
'''Los elementos de la lista están indexados y se puede acceder a ellos haciendo referencia al 
número de índice. Por ejemplo para imprimir el segundo elemento se escribe <name_list>[1]
Ejemplo:	lista_elemen 		[P, L, A, T, O]   
			Pociciones(+)		[0][1][2][3][4]		'''
frutas = ['cereza','moras','mango','kiwi']
print(frutas[1]) #moras

#INDEXACION NEGATIVA
'''Los medios de indexación negativos comienzan desde el final [-1], que se refiere al último elemento,
[-2] que se refiere al segundo último elemento, etc.
Ejemplo:	lista_elemen		[ P,  L,  A,  T,  O]   
			Pociciones(-)		[-4][-4][-3][-2][-1]	'''
verduras = ['zapallos','tomates','limones','papas']
print(verduras[-1]) #papas

#RANGO DE INDICES
'''Puede especificar un rango de índices especificando dónde comenzar y dónde finaliza el rango.
Al especificar un rango, el valor de retorno será una nueva lista con el artículos especificados.
La busqueda comenzara en el indice especificado, y terminara en el vanor anterior al indice dado 
<<< [Ii:(If-1)] >>> '''
frutas = ['cereza','moras','mango','kiwi']
print(frutas[1:3]) #['moras','mango']

#Al dejar de lado el valor de inicio, el rango comenzará en el primer elemento:
frutas = ['cereza','moras','mango','kiwi'] 
print(frutas[:3]) #['cerezas','moras','mango']

#Al dejar de lado el valor final, el rango pasará al final de la lista:
frutas = ['cereza','moras','mango','kiwi'] 
print(frutas[2:]) #['mango','kiwi']

#RANGO DE INDICES NEGATIVOS	
#Especifique los índices negativos si desea iniciar la búsqueda desde el final del lista:
verduras = ['zapallos','tomates','limones','papas','cebollas','lechugas']
print(verduras[-5:-1]) #['tomates', 'limones', 'papas', 'cebollas']

#COMPROBAR EXISTENCIA DE UN ELEMENTO
#Para determinar si un elemento especificado está presente en una lista, use la palabra clave 'in':
verduras = ['zapallos','tomates','limones','papas','cebollas','lechugas']
if 'papas' in verduras:
	print("Si, hay que comprar papas") #Si, hay que comprar papas

#CAMBIAR LOS ELEMENTOS DE UNA LISTA ---------------------------------------------------------------------------------------------------------> 
#Para cambiar el valor de un elemento espesifico, se debe espesificar su indice
verduras = ['zapallos','tomates','limones','papas','cebollas','lechugas']
verduras[4] = 'espinacas'
print(verduras) #['zapallos', 'tomates', 'limones', 'papas', 'espinacas', 'lechugas']

#CAMBIAR ELEMENTOS DENTRO DE UN RANGO
#Para cambiar el valor de los elementos dentro de un rango específico, defina una lista con los 
#nuevos valores y consulte el rango de números de índice donde desea insertar los nuevos valores:
verduras = ['zapallos','tomates','limones','papas','cebollas','lechugas']
verduras[3:] = ['repollo','zanahorias','pepinos']
print(verduras) #['zapallos', 'tomates', 'limones', 'repollo', 'zanahorias', 'pepinos']

#Si inserta MAS elementos de lo esperado para reemplasar, y exede el rango dado, estos se insertarán donde se
#especificó y los elementos restantes se moverán en consecuencia:
frutas = ['careza','moras','mango']
frutas[1:2] = ['banana','peras']
print(frutas) #['careza', 'banana', 'peras', 'mango']

#Si inserta MENOS elementos para reemplasar, se insertarán los nuevos elementos donde se especificó,
#y los elementos restantes se moverán en consecuencia:
frutas = ['careza', 'banana', 'peras', 'mango']
frutas[1:4] = ['damazco']
print(frutas) #['careza', 'damazco']

#INSERTAR ELEMENTOS 
#Para insertar un nuevo elemento de lista, sin reemplazar ninguno de los valores existentes, podemos usar el metodo <insert()>.
#El insert() inserta UN elemento en el índice especificado:		<list_name>.insert(<int>,<str>)
frutas = ['careza', 'damazco']
frutas.insert(1,'arandanos')
print(frutas) #['careza', 'arandanos', 'damazco']

#AGREGAR ELEMENTOS A UNA LISTA ---------------------------------------------------------------------------------------------------------------->
#Para agregar un elemento al final de una lista utiliza el metodo <<< append() >>>
verduras = ['pepinos','cebollas','papas','limones']
verduras.append('tomates')
print(verduras) #['pepinos', 'cebollas', 'papas', 'limones', 'tomates']

#Para insertar un ellemento a un indice especifico, usar el metodo <<< insert() >>>
verduras = ['pepinos','cebollas','papas','limones']
verduras.insert(1,'huevos')
print(verduras) #['pepinos', 'huevos', 'cebollas', 'papas', 'limones']

#Para agragar elementos de otra lista a la lista actual se usa el metodido <<< extend() >>>
lista_compras = ['arroz','harina','fideos','lentejas']
prod_limpieza = ['detergente','levandina','jabon']
lista_compras.extend(prod_limpieza)
print(lista_compras) #['arroz', 'harina', 'fideos', 'lentejas', 'detergente', 'levandina', 'jabon']
'''
El metodo 'extend()' no solo puede anexsarse listas, tambien permite agregar cualquier otro objeto iterable
(tuplas, conjuntos, diccionarios, etc)'''
alumnos = ['pablo','hector','fabricio','lautaro']
carrera = ('romina','laura') #tupla
alumnos.extend(carrera)
print(alumnos) #['pablo', 'hector', 'fabricio', 'lautaro', 'romina', 'laura']

#ELIMINAR ELEMENTOS DE UNA LISTA --------------------------------------------------------------------------------------------------------------->
#Eliminar un elemento espesifico usando remove()
alumnos = ['pablo', 'hector', 'fabricio', 'lautaro', 'romina', 'laura']
alumnos.remove('fabricio')
print(alumnos) #['pablo', 'hector', 'lautaro', 'romina', 'laura']
'''
Si se quiere eliminar un elemento que se repite 2 o mas veces en la lista 
el metodo remove elimina el primero, es decir, la primera concurrencia'''
alumnos = ['pablo', 'hector', 'lautaro', 'romina', 'hector', 'laura']
alumnos.remove('hector')
print(alumnos) #['pablo', 'lautaro', 'romina', 'hector', 'laura']

#Eliminar atraves de un indice especifico usando el metodo <<< pop() >>>
alumnos = ['pablo', 'lautaro', 'romina', 'hector', 'laura']
alumnos.pop(3)
print(alumnos) #['pablo', 'lautaro', 'romina', 'laura']
''' 
Si no se espesifica el indice, el metodo pop() elimina el ultimo elemento'''
alumnos = ['pablo', 'lautaro', 'romina', 'hector', 'laura']
alumnos.pop()
print(alumnos) #['pablo', 'lautaro', 'romina','hector']

#La palabra clave 'del' tambien elimina un indice especifico dando como argumento el indice del elemento
alumnos = ['pablo', 'lautaro', 'romina','hector']
del alumnos[2]
print(alumnos) #['pablo', 'lautaro', 'hector']
'''
Si no se le pasa ningun argumento, la palabra clave elimina la lista completa por defecto'''
alumnos = ['pablo', 'lautaro', 'hector']
del alumnos
#print(alumnos) #Devuelve error, por que la lista ya no existe

#LISTAS - BUCLES ------------------------------------------------------------------------------------------------------------------------------->
'''
Python tiene dos comandos de bucle primitivos:
	_bucle 'while'
	_bucle 'for'
'''
# ***** 'FOR' *****
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

# ***** 'WHILE' *****
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
#El mientras loop requiere que las variables relevantes estén inisializadas, en este 
#ejemplo necesitamos definir una variable de indexación 'i', que establecemos en 1

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

# ***** LIST-COMPRESION *****
#List Comprension ofrece una sintaxis más corta cuando se desea crear una nueva lista basada en los valores de un lista existente.
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]
'''
Ejemplo:
Según una lista de frutas, crea una nueva lista que contenga solo las frutas que contenga la letra "a" en el nombre.
Sin list-compresion tendrás que escribir un declaración 'for' con una prueba condicional en el interior:'''
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []
for x in fruits:
  if "a" in x:
    newlist.append(x)
print(newlist) #['apple', 'banana', 'mango']

#Con list-compresion puedes hacer todo eso con una sola línea de código:
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist) #['apple', 'banana', 'mango']

#_SINTAXIS:
# NUEVA_LISTA = [EXPRECION for ITEM in ITERABLE if CONDICION == True]
#El valor de retorno es una nueva lista, dejando la lista anterior sin cambios.

# CONDICION:
#La 'condición' es como un filtro que solo acepta los elementos que valoran True.
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if x != 'apple']
print(newlist) #['banana', 'cherry', 'kiwi', 'mango']
#La 'condicion' [if x != 'apple'] volvera 'True' para todos los elementos que no sean
# 'apple', haciendo que la nueva lista contenga todas las frutas exepto 'manzana'.
#La condicion es opcional y se puede omitir:
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits]
print(newlist) #['apple', 'banana', 'cherry', 'kiwi', 'mango']

# ITERABLE:
#El iterable puede ser cualquier objeto iterable, como una lista, tupla, conjunto, etc.
newlist = [x for x in range(10)]	
print(newlist) #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#Mismo ejemplo pero con una condicion:
newlist = [x for x in range(10) if x < 5]
print(newlist) ##[0, 1, 2, 3, 4]

# EXPRECION:
#El expresión es el elemento actual en la iteración, pero también es el resultado,
#que puede manipular antes de que termine como un elemento de lista en el nuevo lista:
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x.upper() for x in fruits]
print(newlist) #['APPLE', 'BANANA', 'CHERRY', 'KIWI', 'MANGO']
#Puede estableser el resultado a lo que quieras:
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = ['hello' for x in fruits]
print(newlist) #['hello', 'hello', 'hello', 'hello', 'hello']
#El expresión también puede contener condiciones, no como un filtro, sino como un forma de manipular el resultado:
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x if x != "banana" else "orange" for x in fruits]
print(newlist) #['apple', 'orange', 'cherry', 'kiwi', 'mango']
#La exprecion del ejemplo anterior dice:
'''Devuelva el articulo si no es un platano, si es platano, regrese naranja'''

#ORDENAR LISTA --------------------------------------------------------------------------------------------------------------------------------->
#Ordenar la lista alfanumericamente: los objetos de lista tienen un metodo 'sort()'
#Por defecto ordena una lista alfanumericamente de forma ascendente.
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
fruits.sort()
print(fruits) #['apple', 'banana', 'cherry', 'kiwi', 'mango']
thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist) #[23, 50, 65, 82, 100]

#Para ordenar una lista de forma descendente usa como argumento la palabra clave 'reverse = True'
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist) #['pineapple', 'orange', 'mango', 'kiwi', 'banana']
thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist) #[100, 82, 65, 50, 23]

#Personalizar funcion para 'sort':
#Se puede personalizar una funcion utilizando el argumento 'key = <funcion>'
#La funcion devolvera un numero que se utilizara para ordenar la lista (el numero mas bajo primero)
def mi_funcion(n):
	return abs(n - 50) #-> retorna un valor absoluto 
mi_lista = [100,50,65,82,23]
mi_lista.sort(key = mi_funcion)
print(mi_lista) #[50, 65, 23, 82, 100] --> [0, 15, 27, 32, 50]
'''El método sort() ordena los elementos de la lista thislist in-place, es decir, modifica la lista original. 
El parámetro key se utiliza para definir una función que se usa para extraer una clave de comparación de cada elemento de la lista.
En este caso, el parámetro key está configurado para usar la función myfunc. Esto significa que antes de ordenar los elementos, 
Python evaluará myfunc en cada elemento de la lista y usará el valor devuelto por myfunc para decidir el orden.
Es decir, Python ordenará la lista de acuerdo con los valores absolutos de las diferencias entre cada número en la lista y 50.'''

#Caso no-sensible de 'sort':
#Por defecto el metodo 'sort' es sensible a casos, y dando como resultado que todas las letras mayusculas se ordenen antes que las 
#letras minusculas
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist) #['Kiwi', 'Orange', 'banana', 'cherry']
'''Afortunadamente, podemos usar funciones integradas como funciones clave al ordenar una lista.
Entonces, si desea una función de clasificación insensible a casos, use str.lower como función clave:'''
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist) #['banana', 'cherry', 'Kiwi', 'Orange']

#Orden inversamente
#¿Qué pasa si desea revertir el orden de una lista, independientemente del alfabeto?
#El método 'reverse()' invierte el orden de clasificación actual de los elementos.
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist) #['cherry', 'Kiwi', 'Orange', 'banana']

#COPIAR LISTAS --------------------------------------------------------------------------------------------------------------------------------->
#No puede copiar una lista simplemente escribiendo 'list2 = list1', porque: 'list2' sólo será un referencia a 'list1' y cambios realizados en 
#'list1' también se hará automáticamente en 'list2'.
# Usando el metodo 'copy()':
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist) #["apple", "banana", "cherry"]

#Usando el metodo 'list()':
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist) #["apple", "banana", "cherry"]

#Usando el slice-operator: [rebanadas -> ':']
thislist = ["apple", "banana", "cherry"]
mylist = thislist[:]
print(mylist) #["apple", "banana", "cherry"]

#JOINs(unir) listas ----------------------------------------------------------------------------------------------------------------------------> 
#Hay varias formas de unir o concatenar dos d mas listas en python
#Una de las formas mas faciles es madiante el uso del operador (+)
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3) #['a', 'b', 'c', 1, 2, 3]

#Otras formas de unir dos listas es agregando todos los elementos de 
#lista2 a lista1, uno por uno:
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
for x in list2:
  list1.append(x)
print(list1) #['a', 'b', 'c', 1, 2, 3]

#O puedes usar el metodo 'extend()', donde el propocito es agregar 
#elementos de una lista a otra:
ist1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
list1.extend(list2)
print(list1) #['a', 'b', 'c', 1, 2, 3]

#METODOS de listas ----------------------------------------------------------------------------------------------------------------------------->
'''
append()	Agrega un elemento al final de la lista.
clear()	Elimina todos los elementos de la lista.
copy()	Devuelve una copia de la lista.
count()	Devuelve la cantidad de elementos con el valor especificado
extend()	Agrega los elementos de una lista (o cualquier iterable) al final de la lista actual
index()	Devuelve el indice del primer valorespecificado
insert() Agrega un elemento en la pocicion espesificada
pop()	Elimina el elemento en la pocicion espesificada
remove()	Elimina el elemento con el valor especificado
reverse()	Invierte el orden de la lista
sort()	Ordena la lista
'''