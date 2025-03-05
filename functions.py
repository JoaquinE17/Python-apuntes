#FUNCTIONS -------------------------------------------------------------------------------------------------------------->
''' Una funcion es un bloque de codigo que solo se ejecuta cuando se llama
Puede pasar datos, conosidos como parametros, a una funcion
Una funcion puede devolver datos como resultado '''

#CREAR UNA FUNCION
#En python, una funcio se define usando la palabra clave 'def'
def my_function():
  print("Hello from a function")

#LLAMANDO A UNA FUNCION
#Para llamar a una funcion, use el nombre de una funcion seguido de parentesis.
def my_function():
  print("Hello from a function")

my_function() #Hello from a function

#ARGUMENTOS (arg)
''' La informacion puede pasar a funciones como argumentos
Los argumentos se especifican despues del nombre de la funcion, dentro de 
los parentesis. Puede agregar tantos argumentos como desee, solamente
separados entre comas.'''
def my_function(fname):
  print(fname + " Refsnes")
my_function("Emil") #Emil Refsnes
my_function("Tobias") #Tobias Refsnes
my_function("Linus") #Linus Refsnes

#NUMERO DE ARGUMENTOS 
''' De forma predeterminada, se debe llamar a una funcion con el numero correcto
de argumentos. Lo que significa que si su funcion espera '2 arg', debe
llamar a la funcion con '2 arg', ni mas ni menos.'''
def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil", "Refsnes") #Emil Refsnes
#Si intenta llamar a la función con 1 o 3 argumentos, obtendrá un error

#ARGUMENTOS ARBITRARIOS (*args)
''' Si no sabe cuantos argumentos se pasaran a su funcion, añadir un '*' antes 
del nombre del parametro en la definicion de la funcion
De esta manera la funcion recibira una tupla de argumentos, y puede acceder a 
los elementos en concecuencia '''
def my_function(*kids):
  print("The youngest child is " + kids[2])
my_function("Emil", "Tobias", "Linus") #The youngest child is Linus

#'PALABRA CLAVE' COMO ARGUMENTO
''' Tambien puede enviar argumentos con la sintaxis 'clave = valor'
De esta manera el orden de los argumentos no importa'''
def my_function(child3, child2, child1):
  print("The youngest child is " + child3) #The youngest child is Linus
my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

#ARGUMENTOS ARBITRARIOS 'PALABRA CLAVE' (**kwargs)
''' Si no sabe cuantos arguentos de 'clave=valor' se pasaran a la funcion, añadir
dos asteriscos '**' antes del nombre del parametro en la definicion de la funcion. 
De esta manera la funcion recibira un diccionario de argumantos, y puede acceder a los
elementos en consecuencia '''
def my_function(**kid):
  print("His last name is " + kid["lname"]) #His last name is Refsnes
my_function(fname = "Tobias", lname = "Refsnes")

#VALOR DE ARGUMENTO PREDETERMINADO
''' El siguiente ejemplo muestra como usar un valor de parametro predeterminado
Si llamamos a la funcion sin argumento, utiliza el valor predeterminado'''
def my_function(country = "Norway"):
  print("I am from " + country)
my_function("Sweden") #I am from Sweden
my_function("India") #I am from India
my_function() #I am from Norway
my_function("Brazil") #I am from Brazil

#PASAR UNA LISTA COMO ARGUMENTO
''' Puede enviar cualquier tipo de argumento de datos a una funcion 
(cadena,numero,lista,diccionario,etc) y lo hara ser tratado como el 
mismo tipo de datos dentro de la funcion
Por ejemplo, si envia una lista como argumento, seguira siendo una 
lista cuando pase a la funcion'''
def my_function(food):
  for x in food:
    print(x) #apple \nbanana \ncherry
fruits = ["apple", "banana", "cherry"]
my_function(fruits)

#VALORES RETURN
#Para permitir que una funcion devuelva un valor, use la declaracion 'return'
def my_function(x):
  return 5 * x
print(my_function(3)) #15
print(my_function(5)) #25
print(my_function(9)) #45

#DECLARACION 'PASS'
''' Las funciones no pueden estar vacias, pero si por alguna razon tienes una 
funcion sin contenido, use la declaracion 'pass' para evitar obtener errores.'''
def myfunction():
  pass

#ARGUMENTOS SOLO-POCICIONALES
''' Puede especificar que ua funcion solo pueda tener argumentos pocsicionales
o solo argumentos de palabras claves
Para espesificar que una funcion solo pueda tener argumentos pocisionales', /'
despues de los argumentos'''
def my_function(x, /):
  print(x) #3
my_function(3)
'''Sin el ', /' en realidad, se le permite usar argumentos de palabras clave incluso 
si la funcion espera argumentos pocicionales '''
def my_function(x):
  print(x) #3
my_function(x = 3)
'''Pero al agregar el ', /' obtendra un error si intenta enviar un argumento de palabra clave
def my_function(x, /):
  print(x)

my_function(x = 3)'''

#ARGUMENTOS SOLO CON PALABRAS CLAVE
''' Para especificar que una funcion solo puede tener argumentos de palabra clave, agregue
'*, ' antes de los argumentos'''
def my_function(*, x):
  print(x) #3
my_function(x = 3)
''' Sin el '*, ' se le permite usar argumentos posicionales incluso si la funcion espera
argumentos de palabras claves'''
def my_function(x):
  print(x)
my_function(3) #3
''' Pero con el '*, ' obtendra un error si intenta enviar un argumento posicional
def my_function(*, x):
  print(x)
my_function(3) '''

#COMBINE SOLO POSICIONAL Y SOLO PALABRAS CLAVES
''' Puede combinar los dos tipos de argumentos en la misma funcion. Cualquier argumento antes
del '/ ,' son solo posicionales, y cualquier argumento despues del '*,' son solo palabras claves'''
def my_function(a, b, /, *, c, d):
  print(a + b + c + d) #26
my_function(5, 6, c = 7, d = 8)

################
# RECURSIVIDAD #
################
''' Python tambien acepta la recurcion de funciones lo que significa que una funcion definida
puede llamarse a si misma.
 La recurcion es un concepto matemetico y de programacion comun. Significaque una funcion se 
llama a si misma. Esto significa que la funcion puede recorrer datos hasta alcnzar
un resultado.
 El desarrollador debe tener mucho cuidado con la recurcion, ya que puede ser bastante facil
deslizarse en la escritura de una funcion que nunca termina, o uno que utiliza cantidades 
excesivas de memoria o potencia del procesador. Sin embargo cuando se escribe correctamente,
la recurcion puede ser un enfoque muy eficiente y matematicamente elegante para la progremacion.
 
 En este ejemplo, 'tri_recursion()' es una funcion que hemos definido para llamarse a si misma
('recurse'). Usamos la variable 'k' como los datos, que disminuye (-1) cada vez que recurrimos.
La recurcion termina cuando la condicion no es mayor que '0' (es decir, cuando es cero)
 Para un nuevo desarrollador puede tomar algun tiempo averiguar como funcciona exactamente essto,
la mejor manera de averiguarlo es probandolo y modificandolo '''
def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("Recursion Example Results:")
tri_recursion(6)

'''
  k -> 6  +  tri_recursion(k - 1) -> 5  ¡>  1 + 0 = 1
  k -> 5  +  tri_recursion(k - 1) -> 4  |   2 + 1 = 3
  k -> 4  +  tri_recursion(k - 1) -> 3  |   3 + 3 = 6
  k -> 3  +  tri_recursion(k - 1) -> 2  |   4 + 6 = 10
  k -> 2  +  tri_recursion(k - 1) -> 1  |   5 + 10 = 15
  k -> 1  +  tri_recursion(k - 1) -> 0 _|   6 + 15 = 21

'''

def producto_recursivo(a,b):
  if (b>0):
    return a + producto_recursivo(a,b-1)
  else:
    return 0


print('el producto recursivo es:',producto_recursivo(4,5))
