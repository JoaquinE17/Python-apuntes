#DICTIONARIES -------------------------------------------------------------------------------------------------------------------------------->
''' Los diccionarios se utilizan para almacenar valores de datos en pares de 
{CLAVE : VALOR}. Un diccionario es una coleccion que es ordenado*, modificable
y no permite duplicados.
# A partir de la vercion 3.7 de Python, los diccionarios son ordenados
# Los diccionarios estan escritos entre llaves y contienen pares de clave y valor'''
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict) #{'brand': 'Ford', 'model': 'Mustang', 'year': 1964}

#ELEMENTOS DEL DICCIONARIO:
''' Los elemntos del diccionario son ordenados, pueden ser modificados y no
se permiten duplicados.
Los elementos se presentan en pares 'clave : valor' y pueden ser referidos utilizando
el nombre de la clave'''
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["brand"]) # Ford

#ORDENADO
''' Cuando decimos que los diccionarios estan ordenados, significa que los elementos 
tienen un orden definido, y ese orden no cambiara.

#MODIFICABLE
Los diccionarios son cambiables, lo que significa que podemos cambiar, agregar o eliminar 
elementos despues de que el diccionario es creado.

#DUPLICADOS NO PREMITIDOS
Los diccionarios no puedes tener dos elementos con la misma clave'''
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict) #{'brand': 'Ford', 'model': 'Mustang', 'year': 2020}

#LONGITUD DE DICCIONARIOS:
#Para determinar cuantos elementos tienen un diccionario, utilize la funcion 'len()'
print(len(thisdict)) #3

#ELEMENTOS DEL DICCIONARIO - TIPOS DE DATOS:
#Los valores de los elementos en el diccionario pueden ser de cualquier tipo de datos
thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}
print(thisdict) #{'brand': 'Ford', 'electric': False, 'year': 1964, 'colors': ['red', 'white', 'blue']}

#TYPE()
#Desde la perspectiva de python, los diccionarios se definen como obgeto ('dict')
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(type(thisdict)) # <class 'dict'>

#CONSTRUCTOR DICT():
#Tambien es posible usar el constructor dict() para hacer un diccionario
thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict) #{'name': 'John', 'age': 36, 'country': 'Norway'}

''' Al elegir un tipo de colección, es importante comprender las propiedades de dicho tipo. 
Seleccionar el tipo adecuado para un conjunto de datos específico puede conservar el 
significado y también mejorar la eficiencia o la seguridad. '''

#ACCESO A LOS ELEMENTOS -------------------------------------------------------------------------------------------------------------->
''' Puede acceder a los elementos de un diccionario haciendo referencia a su nombre clave,
dentro de llaves'''
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]
print(x) #Mustang
#Tambien hay un metodo llamado 'get()' eso te dara el mismo resultado
x = thisdict.get("model")
print(x) #Mustang

#OBTENER KEYS (claves)
#El metodo 'keys()' devolvera una lista de todas las claves en el diccionario
x = thisdict.keys()
print(x) #dict_keys(['brand', 'model', 'year'])
''' La lista de las claves es una visualizacion del diccinario, lo que significau 
que cualquier cambio realizado en el diccionario se reflejaran en la lista de claves'''
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = car.keys()
print(x) #antes del cambio -> dict_keys(['brand', 'model', 'year'])
car["color"] = "white"
print(x) #despues del cambio -> dict_keys(['brand', 'model', 'year', 'color'])

#OBTENER VALUES (valores)
#El metodo 'values()' devolvera una lista de todos los valores en el diccionario
x = thisdict.values()
print(x) #dict_values(['Ford', 'Mustang', 1964])
''' La lista de los valores es una visualizacion del diccionario, lo que significa
que cualquier cambio realizado en el diccionario se reflejaran en la lista de valores'''
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = car.values()
print(x) #antes del cambio -> dict_values(['Ford', 'Mustang', 1964])
car["year"] = 2020
print(x) #despues dek cambio -> dict_values(['Ford', 'Mustang', 2020])

#OBTENER ELEMENTOS
#El metodo 'items()' devolvera cada elemento de un diccionario, como tuplas en una lista
x = thisdict.items()
''' La lista que devuelve visualiza los elementos del diccionario, lo que significa que 
cualquier cambio realizado en el diccionario se reflejan en la lista de elementos'''
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = car.items()
print(x) #antes del cambio -> dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964)])
car["year"] = 2020
print(x) #despues del cambio ->dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 2020)])
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = car.items()
print(x) #antes del cambio -> dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964)])
car["color"] = "red"
print(x) #despues del cambio -> dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964), ('color', 'red')])

#COMPRUEBE SI LA CLAVE EXISTE
#Para determinar si una clave espesifica esta presente en un diccionario, use la palabra clave 'in'
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary") #Yes, 'model' is one of the keys in the thisdict dictionary

#CAMBIAR ELEMENTOS DEL DICCIONARIO -------------------------------------------------------------------------------------------------------------->
#Puede cambiar el valor de un elemento especifico haciendo referencia a su nombre clave
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict['year']) #1964
thisdict["year"] = 2018
print(thisdict['year']) #2018

#ACTUALIZAR DICCIONARIO
'''El metodo 'update()' actualizará el diccionario con los elementos del argumento dado
El arguento debe ser un diccionario o un objeto iterable con pares de clave:valor'''
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict['year']) #1964
thisdict.update({"year": 2020})
print(thisdict['year']) # 2020

#AGREGAR ELEMENTOS AL DICCIONARIO --------------------------------------------------------------------------------------------------------------->
#Agregar un elemento al diccionario se realiza utilizando un nueva clave de indice y asignandole un valor.
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["color"] = "red"
print(thisdict) #{'brand': 'Ford', 'model': 'Mustang', 'year': 1964, 'color': 'red'}

#ACTUALIZAR DICCIONARIO
''' El metodo 'update()' actualizara el diccionario con los elementos de un argumento dado.
Si el elemento no existe, se agregará al diccionario
El argumento debe ser un diccionario o un obgeto iterablev con pares de clave:valor '''
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict) #{'brand': 'Ford', 'model': 'Mustang', 'year': 1964}
thisdict.update({"color": "red"})
print(thisdict) #{'brand': 'Ford', 'model': 'Mustang', 'year': 1964, 'color': 'red'}

#ELLIMINAR ELEMENTOS DE UN DICCIONARIO ---------------------------------------------------------------------------------------------------------->
#Hay varios metodos para eliminar elementos de un diccionario
 #Ejemplo1: El metodo 'pop()' elimina el elemento con el nombre clave especificado
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict) # {'brand': 'Ford', 'year': 1964}

 #Ejemplo2: El metodo 'popitem()' elimina el ultimo elemento insertado (en verciones
 #anterires a 3.7, se elimina un elemento aletrio en su lugar)
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.popitem()
print(thisdict) #{'brand': 'Ford', 'model': 'Mustang'}

 #Ejemplo3: La palabra clave 'del' elimina el elemento con el nombre clave especificado
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict["model"]
print(thisdict) #{'brand': 'Ford', 'year': 1964}
#La palabra clave 'del' tambien puede eliminar el diccionario completo
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict
#print(thisdict) #Esto causará un error porque "thisdict" ya no existe.

 #Ejemplo4: El metodo 'clear()' vacia el diccionario
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.clear()
print(thisdict) #{}

#BUCLE A TRAVES DE UN DICCIONARIO --------------------------------------------------------------------------------------------------------------->
''' Puede recorrer un diccionario utilizando un bucle 'for'
Al hacer un bucle a traves de un diccionario, el valor de retorno es las 'key()' del 
diccionario, pero hay metodos para devolver el 'values()' tambien'''
 #Ejemplo1: Imprime todas las keys del diccionario
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict:
  print(x) #brand \nmodel \nyear

 #Ejemplo2: Imprime todos los valores del diccionario
for x in thisdict:
  print(thisdict[x]) #Ford \nMustang \n1964

 #Ejemplo3: El metodo 'values()' para retornar valores del dicconario
for x in thisdict.values():
  print(x) #Ford \nMustang \n1964

 #Ejemplo4: El metodo 'keys()' devuelve las claves del diccionario
for x in thisdict.keys():
  print(x) #brand \nmodel \nyear

 #Ejemplo5: Bucle a traves de los pares clave:valor, usando el metodo 'items()'
for x, y in thisdict.items():
  print(x, y) #brand Ford \nmodel Mustang \nyear 1964

#COPIAR DICCIONARIOS ----------------------------------------------------------------------------------------------------------------------------->
''' No puede copiar un diccionario simplemente escribiendo 'dict2 = dict1', porque dict2 
solo sera una referencia a dict1 y los cambios realizados en dict1 tambien se vera reflejado 
automaticamente en dict2
Hay formas de hacer una copia:'''
 #Una forma es utilizar el metodo 'copy()':
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(thisdict) #{'brand': 'Ford', 'model': 'Mustang', 'year': 1964}
print(mydict) #{'brand': 'Ford', 'model': 'Mustang', 'year': 1964}
 #Otra forma es usar la funcion 'dict()':
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = dict(thisdict)
print(thisdict) #{'brand': 'Ford', 'model': 'Mustang', 'year': 1964}
print(mydict) #{'brand': 'Ford', 'model': 'Mustang', 'year': 1964}

#DICCIONARIOS ANIDADOS ---------------------------------------------------------------------------------------------------------------------------->
#Un diccionario puede contener diccionarios, esto se llama anidado diccionarios.
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
print(myfamily) #{'child1': {'name': 'Emil', 'year': 2004}, 'child2': {'name': 'Tobias', 'year': 2007}, 'child3': {'name': 'Linus', 'year': 2011}}

#O si desea agregar tres diccionariosa un nuevo diccionario
child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}
print(myfamily) #{'child1': {'name': 'Emil', 'year': 2004}, 'child2': {'name': 'Tobias', 'year': 2007}, 'child3': {'name': 'Linus', 'year': 2011}}

#Acceso a los elementos de diccionarios anidados:
''' Para acceder a los diccionarios anidados, utiliza el nombre 
de los diccionarios, comenzando con el diccionario externo'''
print(myfamily["child2"]["name"]) #Tobias

#Bucle a travez de diccionarios anidados
#Puede recorrer un diccionario utilizando el metodo 'items()':
for x, obj in myfamily.items():
  print(x)
  for y in obj:
    print(y + ':', obj[y])
'''
child1
name: Emil
year: 2004
child2
name: Tobias
year: 2007
child3
name: Linus
year: 2011
'''

#METODOS ------------------------------------------------------------------------------------------------------------------------------------------>
'''
clear() : Elimina todos los elementos del diccionario
copy() : Devuelve una copia del diccionario
fromkeys() : Devuelve un diccionario con las claves y valor especificado
get() : Devuelve el valor de la clave especificada
items() : Devuelve una lista que contiene una tupla para cada par 'clave:valor'
keys() : Devuelve una lista que contiene las claves del diccionario
pop() : Elimina el elemento con la clave especificada
popitem() : Elimina el ultimo par 'clave:valor' insertado
setdefault() : Devuelve el valor de la clave especificada. Si la clave no existe, inserta la clave con el valor especificado
update() : Actualiza el diccionario con los pares 'clave:valor'
values() : Devuelve una lista de todos los valores del diccionario
'''