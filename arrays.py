#ARRAYS ---------------------------------------------------------------------------------------------------------------------->
''' Python no tiene soporte incorporado para Arrays, pero las 'list' se pueden utilizar en su lugar
Para trabajar con arrays en python tendras que importar una biblioteca, como 'numPy'
Las arrays se utilizan para almacenar multiples valores en una sola variable '''
cars = ['ford','bmw','volvo']

### QUE ES UN ARRAY?
''' Una matriz(array) es una variable especial, que puede contener mas de un valoe a la vez
Si tiene una lista de elementos (una lista de nombres de automoviles, por ejemplo),
almacene los coches en variables individuales podrian verse asi:
	car1 = 'Ford'
	car2 = 'Volvo'
	car3 = 'BMW'
Sin embargo,que pasa si desea recorrer los autos y encontrar uno especifico?, y si no 
tuvieras 3 autos, sino 300?
La solucion es una matriz:
Una matriz puede contener muchos valores con un solo nombre, y usted puede acceder a 
los valores haciendo referencia a un numero de un indice. '''
#ACCEDE A LOS ELEMENTOS DE UN ARRAY
#Se refiere a un elemento del array, refiriendce al numero del indice
x = cars[0]
print(x) #ford

#Para modificar un valor de un elemento del array, se realiza la misma operacion que se hace en las listas
cars[0] = 'toyota'
print(cars[0] , x) #toyota ford

### LONGITUD DE UN ARRAY
#Usa el metodo 'len()' para devolver la longitud de un array (nro. de elementos de un array)
x = len(cars)
print(x) #3 La longitud de un array es siempre UNO MAS que el indice de matriz mas alto

#Bucle en los elementos del array
#Puedes usar el bucle 'for in' a traves de todos los elementos de una matriz
for y in cars:
	print(y) #toyota \nbmw \nvolvo

### AGREGAR ELEMENTOS AL ARRAY
#Puedes usar el metodo 'append()' para agregar un elemnto a un array
cars.append('honda')
print(cars) #['toyota','bmw','volvo','honda']

### ELIMINAR ELEMENTOS DE UN ARRAY
#Puedes usar el metodo 'pop()' para eliminar un elemento de un array
cars.pop(1)
print(cars) #['toyota', 'volvo', 'honda']

#Tambien puedes usar el metodo 'remove()' para eliminar un elemento del array
cars.remove('volvo')
print(cars) #['toyota', 'honda']
#El metodo 'remove()', solo elimina la primera aparicion del valor especificado

### METODOS DE ARRAY
#Python tiene un conjunto de métodos integrados que puede usar en listas/matrices.
'''
apeend() : agrega un elemento al final de la lista
clear() : elimina todos los elementos de la lista
copy() : decuelve una copia de la lista
count() : devuelve el numero de elementos con el valor especificado
extend() : agrega los elementos de una lista (o cualquier iterable),al final de la actual lista/array
index() : devuelve el indice de el primer elemento con el valor especificado
insert() : agrega un elemento en la posicion especificada
pop() : elimina el elemento en la pocsicion especificada
remove() : elimina el primer elemento con el valor especificado
reverse() : revierte el orden de la lista/array
sort() : ordena la lista/array
'''
#Python no tiene soporte incorporado para Arrays, pero las listas de Python se pueden usar en su lugar.