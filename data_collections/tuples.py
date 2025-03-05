#TUPLAS -------------------------------------------------------------------------------------------------------------------------------------->
'''
Las tuplas se utilizan para almacenar múltiples elementos en una sola variable.
'Tuple' es uno de los 4 tipos de datos integrados en Python utilizados para almacenar 
colecciones de datos, los otros 3 son Lista, Set, y Diccionario, todos con diferentes cualidades y uso.
Una tupla es una colección que es ordenada e inmutable.
Las tuplas están escritas con corchetes redondos.
Ejemplo
'''
mitupla = ('manzana','arandano','banana','durazno')
print(mitupla) #('manzana', 'arandano', 'banana', 'durazno')
print(type(mitupla)) #<class 'tuple'>

#ELEMENTOS DE TUPLE
#Los elementos de una 'tupla' se ordenan son inmutables y permiten valores duplicados 
#Los elementos de tupla están indexados, el primer elemento tiene índice [0], el segundo elemento tiene índice [1] etc.

#ORDENADO
#Cuando decimos que las tuplas están ordenadas, significa que los elementos tienen un orden definido, y ese orden no cambiará.

#INMODIFICABLE
#Las tuplas son inmutables, lo que significa que no podemos cambiar, agregar o eliminar elementos después de que se haya creado la tupla.

#PERMITIR DUPLICADOS
#Dado que las tuplas están indexadas, pueden tener elementos con el mismo valor:

mitupla = ('manzana','arandano','banana','manzana','durazno')
print(mitupla) #('manzana', 'arandano', 'banana', 'manzana', 'durazno')

#LONGITUD DE TUPLA
#Para determinar cuantos elementos tiene una tupla, use la funcion 'len()'
mitupla = ('manzana','banana','arandanos')
print(len(mitupla)) #3

#CREA TUPLA CON UN ELEMENTO
'''Para crear una tupla con un solo elemento, debe agregar una coma despues del elemento de lo contrario,
Python  no lo reconocera como una tupla'''
mitupla = ('manzana',)
print(type(mitupla)) #<class 'tuple'>

mitupla = ('manzana')
print(type(mitupla)) #<class 'str'>

#TYPE()
#Desde la perspectiva de python, las tuplas se definen como objetos con el tipo de dato 'tupla'

#ELEMENTOS DE TUPLE - TIPOS DE DATOS 
'''
Los elementos de tuple pueden ser de cualquier tipo de datos (str, int, bool)

tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)

Una tupla puede contener diferentes tipos de datos 

tuple1 = ("abc", 34, True, 40, "male")
'''

#EL CONSTRUCTOR TUPLE()
#Tambien es posible utilizar el constructor tuple() para hacer una tupla, tener en cuenta los dobles parentesis
mitupla = tuple(('manzana','mango',"pera"))
print(mitupla) #('manzana', 'mango', 'pera')

#ACCESO A LOS ELEMENTOS DE LA TUPLA----------------------------------------------------------------------------------------------------------->
#Puede acceder a los elementos de tupla haciendo referencia al numero de indice, dentro de los corchetes rectangulares
thistuple = ("apple", "banana", "cherry")
print(thistuple[1]) #banana

#INDEXACION NEGATIVA
''' Los  medios de indexacion negativos comienzan deste el final
'-1' se refiere al ultimo elemento, '-2' al penultimo y asi sucesivamente.'''
thistuple = ("apple", "banana", "cherry")
print(thistuple[-1]) #cherry

#RANGO DE INDICES
''' Puede espesificar un rango de indices especificando donde comienza y donde finaliza el rango
Al especificar un rango, el valor de retorno sera una nueva tupla con los articulos especificados'''
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5]) #('cherry', 'orange', 'kiwi')
#La busqueda comenzara en el indice 2 (incluido) y finalizara en el indice 5 (no incluido)

#Al dejar de lado el valor del inicio, el rango comenzara en el primer elemento
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[:4]) #('apple', 'banana', 'cherry', 'orange')

#Al dejar de lado el valor final, el rango pasara al final de la tupla
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:]) #('cherry', 'orange', 'kiwi', 'melon', 'mango')

#RANGO DE INDICES NEGATIVOS
#Especifica los indices negativos si desea iniciar la busqueda desde el final de la tupla
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1]) #('orange', 'kiwi', 'melon')
#Este ejemplo devuelve los elementos del índice -4 (incluido) al índice -1 (excluido)

#COMPROBAR SI UN ARTICULO EXISTE
#Para determinar si un elemento especifico esta presente en una tupla, utilise la palabra clave 'in'
thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple") #Yes, 'apple' is in the fruits tuple
  
#ACTUALIZAR TUPLAS --------------------------------------------------------------------------------------------------------------------------->
''' Las tuplas son inmutables, lo que significa que no puede cambiar, agregar o eliminar elementos
una vez que se crea la tupla. Pero existe algunas soluciones alternativas.

#CAMBIAR ELEMENTOS:
Se puede convertir la tupla en una lista, cambiar la lista y convertir la lista nuevamente a una tupla'''
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi" #Modifica el segundo valor ('banana')
x = tuple(y)
print(x) #('apple', 'kiwi', 'cherry')

#AGREGAR ELEMENTOS 
''' Como laas tuplas son inmutables, no tienen incorporado el metodo 'append()', pero hay otras 
formas de agregar elementos a una tupla.
Op1: CONVERTIR EN UNA LISTA
 Al igual que la solucion para 'cambiar elementos', puede convertirla en una lista, agregar su items 
 y convertirla nuevamente en una tupla.'''
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)
print(thistuple) #('apple', 'banana', 'cherry', 'orange')
'''Op2: AÑADE TUPLA A UNA TUPLA
 Se permite agregar tupla a otra tupla, a si que si quieres agregar un elemento, o muchos, crea una 
 tupla con items, y añadirlo a la tupla existente.'''
thistuple = ("apple", "banana", "cherry")
y = ("orange",) #recuerde incluir una coma después del elemento
thistuple += y
print(thistuple) #('apple', 'banana', 'cherry', 'orange')

#ELIMINAR ELEMENTOS
'''Las tuplas son inmutables, por lo que no puede eliminar elementos a partir de él, pero puede usar 
la misma solucion alternativa que usamos para cambiar y agregar elementos.
Como convertir la tupla a lista y de nuevo a tupla:'''
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)
print(thistuple) #('banana', 'cherry')
#O puede eliminar la tupla por completo utilizando la palabra clave 'del'
thistuple = ("apple", "banana", "cherry")
del thistuple
#print(thistuple) #esto generará un error porque la tupla ya no existe

#DESEMPAQUETAR TUPLAS ------------------------------------------------------------------------------------------------------------------------>
#Cuando creamos una tupla, normalmente le asignamos valores. Esto se llama empaquetar una tupla:
frutas = ('manzana','banana','cherry')
print(frutas) #('manzana', 'banana', 'cherry')
#Pero, en Python, tambien se nos permite extraer los valores de nuevo en variables, esto se llama desempaquetar:
fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits
print(green) #apple
print(yellow) #banana
print(red) #cherry
''' Si el número de elementos no coincide exactamente con el número de variables, obtendrás un error. 
Sin embargo, puedes usar el asterisco para manejar esos casos y recopilar los valores restantes como
una lista'''

#USO DEL ASTERISKO (*)
'''Si el numero de variables es menor que el numero de valores, puede agregar un '*' al nombre de la 
variable y los valores se asignaran a la variable como una lista'''
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits
print(green) #apple
print(yellow) #banana
print(red) #['cherry', 'strawberry', 'raspberry']
''' Si el asterisco se agrega a otro nombre de variable, que no sea el ultimo, 
Python asignará valores a la variable hasta que el número de valores que quedan 
coincida con el número de variables que quedan.'''
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
(green, *tropic, red) = fruits
print(green) #apple
print(tropic) #['mango', 'papaya', 'pineapple']
print(red) #cherry
#Este tipo de desempaquetado es útil cuando solo te interesan algunos valores 
#de la tupla, pero quieres capturar el resto de los elementos en otra variable

#DESEMPAQUETADO EN FUNCIONES
#También puedes usar el desempaquetado cuando trabajas con funciones que devuelven tuplas.
def obtener_datos():
    return ("Juan", 25, "Madrid")
nombre, edad, ciudad = obtener_datos()
print(nombre) #Juan
print(edad) #25
print(ciudad) #Madrid

#BUCLE EN TUPLAS ----------------------------------------------------------------------------------------------------------------------------->
#Recorrer una tupla utilizando el bucle 'for':
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x) #apple \nbanana \ncherry
#Recorrrer atravez de los numeros de indice
'''Tambien puede recorrer los elemntos de una tupla haciendo referencia a
su numero de indice. Use las funciones 'range()' y 'len()' para crear un iterable adecuado'''
thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
  print(thistuple[i]) #apple \nbanana \ncherry

#Recorrer una tupla con el bucle 'while':
'''Puede recorrer los elementos de tupla utilizando un bucle while. Usa la funcion 'len()' para determinas la longitud de la tupla, 
luego comience en '0' y recorra los elementos de tupla refiriendose a sus indices.
Recuerde aumentar el indice de 1 despues de cada iteracion.'''
thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
  print(thistuple[i]) #apple \nbanana \ncherry
  i = i + 1

#JOINs - TUPLAS ------------------------------------------------------------------------------------------------------------------------------>
#Unir dos tuplas:
#Para unir dos o mas tuplas puedes usar el operador '+'.
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
print(tuple3) #('a', 'b', 'c', 1, 2, 3)

#Si desea multiplicar el contenido de una tupla un numero de veces, puede usar el operador '*'.
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2
print(mytuple) #('apple', 'banana', 'cherry', 'apple', 'banana', 'cherry')

#METODOS TUPLE ------------------------------------------------------------------------------------------------------------------------------->
#Python tiene dos metodos integrados que puedes usar en tuplas
'''
count():
  Descripción: Este método cuenta cuántas veces aparece un elemento específico en la tupla.
  Sintaxis: tupla.count(elemento)
  Parámetros: Un único valor, que es el elemento que deseas contar en la tupla.
Ejemplo:
tupla = (1, 2, 3, 1, 1)
print(tupla.count(1))  # Resultado: 3

index():
  Descripción: Este método devuelve el índice de la primera aparición de un elemento en la tupla.
  Sintaxis: tupla.index(elemento)
  Parámetros: Un único valor que es el elemento del que deseas encontrar el índice.
Ejemplo:
tupla = (10, 20, 30, 40)
print(tupla.index(30))  # Resultado: 2
'''