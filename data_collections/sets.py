#SETS --------------------------------------------------------------------------------------------------------------------------------------->
''' Los sets se utilizan para almacenar multiples elementos en una sola variable. 
Es uno de los 4 tipos de datos integrados en python utilizados para almacenar colecciones
de datos, los otros tres son listas, tuplas y diccionarios, todos con diferentes cualidades y uso
# Un set es una coleccion de datos que es desordenado, *inmutable y sin indexar
	*Los elementos de set son inmutables, pero puede eliminar elementos y agregar nuevos
# Los set estan escritos entre llaves.'''
miset = {'manzana','banana','pera'}
print(miset) #{'pera', 'manzana', 'banana'}

#Los set no estan ordenados, por lo que no puede estar seguro de en que orden
#se encuentra cada elemento

''' Los elementos de un set son desordenados, inmutables y no permiten valores duplicados
# Desordenados: significa que los elementos de un conjunto no tienen un orden definido.
				Los elementos pueden parecer en un orden diferente cada vez que los use o consulte,
				por esto no puede ser referido por un indice o una clave.
# Inmodificable: los elementos de un set son inmutables, lo que significa que no podemos cambiar los 
				 despues que se haya creado el set (conjunto)
				 Lo unico que se pued hacer es eliminar elementos y añadir nuevos elementos
# Duplicados no permitidos: Los cnjuntos no pueden tener dos elementos con el mismo valor. Estos se ignoran'''
miset = {'manzana','banana','pera','banana'}
print(miset) #{'pera', 'manzana', 'banana'}

#Los valores ([True y 1] y [False y 0]) se consideran el mismo valor en conjubtos, y se tratan como duplicados
miset = {'manzana','banana',4,1,True,0,False}
print(miset) #{'manzana', 'banana', 1, 0, 4}

#OBTENER LA LONGITUD DE UN SET:
#Para determinar cuantos elementos tiene un conjunto, use la funcion 'len()'
miset = {'manzana','banana',4,1,True,0,False}
print(len(miset)) #5
miset = {'manzana','banana','pera'}
print(len(miset)) #3

#SET - ELEMENTOS - TIPOS DE DATOS:
#Un set puede contener cualquier tipo de datos (str,int,bool)
set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}
#Un minmo set puede contener distintos tipos de datos.
set1 = {"abc", 34, True, 40, "male"}
print(set1) #{True, 34, 40, 'male', 'abc'}

#TYPE():
#Desde la perspectiva de python, los conjuntos se definen como objetos con el tipo de dato 'set'
myset = {"apple", "banana", "cherry"}
print(type(myset)) #<class 'set'>

#EL CONSTRUCTOR SET():
#TYPEambien es posible utilizar el constructor set() para hacer un conjunto.
thisset = set(("apple", "banana", "cherry")) #Tenga en cuenta los dobles parentesis
print(thisset) #{'apple', 'banana', 'cherry'}

#ACCESO A LOS ELEMENTOS DEL SET ------------------------------------------------------------------------------------------------------------->
'''No se puede acceder a los elementos de un conjunto haciendo referencia a un indice o una clave.
Pero puede recorrer los elementos de un set utilizando el bucle 'FOR' o preguntar si un valor 
especificado esta presente en un set, utilizando la palabra clave 'IN' '''
myset = {'gato','perro','loro'}
for x in myset:
	print(x) #perro \ngato \nloro

myset = {'gato','perro','loro'}
print('perro' in myset) #True

#NO SE PERMITE EL CAMBIO DE ELEMENTOS UNA VEZ CREADO EL SET, PERO PUEDE AGREGAR NUEVOS ELEMENTOS

#AGREGAR ELEMENTOS -------------------------------------------------------------------------------------------------------------------------->
#Para agregar un elemento a un set utilice el metodo add()
myset = {'gato','perro','loro'}
myset.add('tiburon')
print(myset) #{'gato', 'tiburon', 'perro', 'loro'}

#AGREGAR OTRO SET AL SET ACTUAL
#Para agregar elementos de otro set al set actual, utilice el metodo 'update()'
miset = {'gato','perro','loro'}
nuevoset = {'pera','manzana','banana'}
miset.update(nuevoset)
print(miset) #{'loro', 'banana', 'perro', 'pera', 'manzana', 'gato'}

#AÑADIR CUALQUIER ITERABLE
''' El objeto que resibe el metodo update() no tiene por que ser solamente un set, puede ser 
cualquier objeto iterable (tuplas,listas,diccionarios,etc)'''
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]
thisset.update(mylist)
print(thisset) #{'cherry', 'orange', 'banana', 'apple', 'kiwi'}

#ELIMINAR ELEMENTOS DE UN SET ----- --------------------------------------------------------------------------------------------------------->
#Para eliminar un elemento de un set, utilice los metodos remove() o discard()
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset) #{'apple', 'cherry'}
#Si el elemento a eliminar no existe, remove() generará un error
thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset) #{'cherry', 'apple'}
#Si el elemento a eliminar no existe, discard() este NO generar un error.

''' Tambien puedes usar el metodo pop() para eliminar un elemento, pero este metodo
eliminara un elemento aleatorio, por lo que NO puede estar seguro de que elemento 
se elimina. El valor que retorna pop() es el valor del elemento eliminado'''
thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x) #apple
print(thisset) #{'banana','cherry'}
#Los set son desordenados, entonces cuando se usa el metodo pop(), no se sabe 
#que elemento se elimina

#El metodo clear() vacia el set.
thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset) #set()

#La palabra clave 'del' eliminara el set completamente
thisset = {"apple", "banana", "cherry"}
del thisset
#print(thisset) #Devuelve Error porque 'thisset' no existe

#SET - BUCLES ------------------------------------------------------------------------------------------------------------------------------->
#Puede recorrer los elementos de un set utilizando un bucle for 
thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x) #cherry \napple \nbanana

#UNIR SETS ---------------------------------------------------------------------------------------------------------------------------------->
''' Hay varias formas de unir dos o mas conjuntos en python
 Los metodos union() y update() unen todos los elementos de ambos set
 El metodo intersection() mantiene SOLO los duplicados.
 El metodo difference() mantiene los articulos de el primer coonjunto que no
 estan en el otro set
 El metodo symmetric_difference() mantiene todos los elementos EXCEPTO los duplicados'''

#METODO UNION()
#Devuelve un nuevo conjunto con todos los elementos de ambos conjuntos
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3) #{1, 2, 'a', 3, 'b', 'c'}
#Puedes usar el | operador en lugar de la union() método, y obtendrá el mismo resultado.
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1 | set2
print(set3) #{1, 'c', 'b', 2, 3, 'a'}
#Unir multiples set
''' Todos los metodos y operadores de union su pueden usar para unir multiples set.
Cuando utilize un metodo, simplemente agregue mas conjuntos separados por comas.'''
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}
myset = set1.union(set2, set3, set4)
print(myset) #{1, 2, 3, 'apple', 'b', 'bananas', 'Elena', 'c', 'cherry', 'a', 'John'}
#Cuando se usa el | operador, separe los conjuntos con más | operadores:
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}
myset = set1 | set2 | set3 |set4
print(myset) #{1, 2, 3, 'apple', 'Elena', 'John', 'bananas', 'cherry', 'a', 'b', 'c'}
#Unir un set y una tupla
#El metodo union() le permite unir un set con otras colecciones de datos (listas o tuplas)
#EL resultado sera un conjunto
x = {"a", "b", "c"} #set
y = (1, 2, 3) #tupla
z = x.union(y)
print(z) #{1, 2, 3, 'b', 'a', 'c'}
#El operador '|' solo le permite unir set con set, y no con otros tipos
#como si lo puede el metodo union()

#METODO UPDATE()
''' El metodo inserta todos los elementos de un conjunto a otro
y cambia el conjunto original, no devuelve un nuevo conjunto '''
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set1.update(set2)
print(set1) #{1, 2, 3, 'a', 'c', 'b'}
#Ambos union() y update() excluirá cualquier artículo duplicado.

#METODO INTERSECTION()
#Mantiene SOLO los elementos duplicados
#Este metodo devuelve un nuevo conjunto, que solo contiene los elementos que estan presentes
#en ambos sets
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.intersection(set2)
print(set3) #{'apple'}
#Puedes usar el operador '&' en lugar de el metodo intersection(), y obtendra el mismo resultado
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1 & set2
print(set3) #{'apple'}
#El operador '&' solo permite unir set con set, y no con otros tipos como se puede hacer con el 
#metodo intersection
'''El metodo intersection_update() mantendra solo los duplicados, pero cambiara el set original
en lugar de devolver un nuevo sets'''
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.intersection_update(set2)
print(set1) #{'apple'}
#Los valores True y 1 se consideran el mismo valor. Lo mismo ocurre con False y 0.
set1 = {"apple", 1,  "banana", 0, "cherry"}
set2 = {False, "google", 1, "apple", 2, True}
set3 = set1.intersection(set2)
print(set3) #{False, 1, 'apple'}

#	DIFFERENCE()
''' El metodo difference() devolvera un conjunto que contendrá solo los 
elementos del primer conjunto que no estan presentes en el otro conjunto'''
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.difference(set2)
print(set3) #{'banana', 'cherry'}
#Puedes usar el '-' operador en lugar de la difference() método, y obtendrá el mismo resultado.
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1 - set2
print(set3) #{'banana', 'cherry'}
#El operador '-' permite unir set con set, y no con otros tipos, como si se puede con el metodo difference()
''' El metodo diffrence_update() tambien mantendra los elementos del primer set que no estan en el otro set, 
pero cambiará el set original en lugar de devolver un nuevo set'''
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.difference_update(set2)
print(set1) #{'cherry', 'banana'}

#SYMMETRIC DIFFERENCE()
#El metodo solo mantendra los elementos que NO estan presentes en ambos set
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.symmetric_difference(set2)
print(set3) #{'google', 'microsoft', 'cherry', 'banana'}
#Puedes usar el operador '^' en lugar de el metodo symmetric_difference(), y obtendrá el mismo resultado.
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1 ^ set2
print(set3)  #{'google', 'microsoft', 'cherry', 'banana'}
'''El operador '^' solo le permite unir set con set, y no con otros tipos como se 
puede con el metodo symmetric_difference()
El metodo symmetric_difference_update() tambien mantendra todo pero no los duplicados, solo que cambiara el set orifinal
en lugar de devolver uno nuevo'''
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.symmetric_difference_update(set2)
print(set1) #{'cherry', 'microsoft', 'google', 'banana'}

#METODOS ------------------------------------------------------------------------------------------------------------------------------------>
'''
add() : Agrega un elemento al set
clear() : Elimina todos los elementos del set
copy() : Devuelve una copia del set
difference()/[-] : Devuelve un set que contiene la diferencia entre dos o mas set
difference_update()/[-=] : Elimina los elementos de este set que tambien estan incluidos en otro set especificado
discard() : Elimina el elemento especificado
intersection()/[&] : Devuelve un set, que es la interseccion de otros dos set
intersection_update()/[&=] : Elimina los elementos de este set que no estan presentes en otros sets especificados
isdisjoint() : Devuelve si dos conjuntos tienen una interseccion o no
issuubset()/[<=] : Devuelve si otro set contiene este set o no. [<] : Devuelve si todos los elementos de este set estan presentes en otro set especificado
issuperset()/[>=] : Devuelve si este set contiene otro set o no. [>] : Devuelve si todos los elementos de otrosset espesificados estan presentesen este set
pop() : Elimina un elemento especificado del set
remove() : Elimina el elemento especificado
symmetric_difference()/[^] : Devuelve un conjunto con las diferencias simetricas de dos conjuntos
symmetric_difference_update()/[^=] : Inserta las diferencias simetricas de este conjunto y otro
union()/[|] : Devuelve un set que contiene la union de cambos set
update()/[|=] : Actualiza el conjunto con la union de este set y otro
'''