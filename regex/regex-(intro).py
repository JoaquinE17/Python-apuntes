# EXPRECIONES REGULARES -------------------------------------------------------------------------------------------------------------------------------------------------------------------->
'''Las expresiones regulares, también conocidas como regex o regexp, son una serie de símbolos que permiten definir 
PATRONES de búsqueda en cadenas de texto. Estos PATRONES se utilizan para encontrar una determinada combinación 
de caracteres dentro de una cadena de texto, y pueden ser muy útiles para manipular y realizar búsquedas sobre 
archivos de texto o incluso textos sin necesidad de que estén contenidos en un archivo.

## Porque aprender regex:
	- Busqueda avanzada: Encontrar patrones especificos en textos grandes de forma rapida y precisa
	- Validacion de datos: Asegurate que los datos que ingresa un usuario como el email, telefomo, etc. son correctos
	- Extraccion de informacion: Permitir obtener y aprovechar datos especificos de un texto como nombres, fechas o direcciones
	- Manipulacion de texto: Extraerr, remplazar y modificar partes de la cadena de texto
	- Optimizacion de tareas: Automatizar procesos repetitivos que implican tratar con el texto'''

# Para trabajar cn espreciones regulares en python se importa la libreria "re"
import re

# Crear un patron (una cadena de texto que describe lo que queremos encontrar)
pattern = 'Hola'

# Texto donde buscar
text = 'Hola mundo'

#Usar la funcion de busqueda de 're' 
result = re.search(pattern,text) # Esta funcion devuelve un objeto (Match[str]) o un 'None'
if result:
	print('Patron encontrado') # Patron encontrado
else:
	print('Patron no encontrado') 

# .group() : devuelve la cadena que coincide con el patron
print(result.group()) # Hola

# .tart() : devuelce la pocicion inicial de la coincidencia
print(result.start()) # 0

# .end() : devuelve la pocicion final de la coincidencia
print(result.end()) # 4

######## EJERCICIO 01 ########
''' Encuentra la primera ocurrencia de la palabra 'IA' en el siguiente texto
e indica en que pocicion empieza y termina la coincidencia '''
text = 	'Todo el mundo dice que la IA nos va a quitar el trabajo. Pero solo hace falta ver como la puede cagar con las REGEX para ir con cuidado'
pattern = 'IA'
result = re.search(pattern,text)
if result:
	print(f"Patron {result.group()} encontrado") # Patron IA encontrado
	print("Posicion inicial:",result.start()) # Posicion inicial: 26
	print("Posicion final:",result.end()) # Posicion final: 28
else:
	print("No se ha encontrado el patron")

# Encontrar todas la coincidencias de un patron en una cadena
# .findall() devuelve una lista con todas la coincidencias
text = "Me gusta python. Python es lo maximo. Aunque python no es tan dificil, ojo con python."
pattern = "python"
matches = re.findall(pattern,text)
print(matches) # ['python', 'python', 'python']
'''
	text = "Me gusta python. Python es lo maximo. Aunque python no es tan dificil, ojo con python."
	pattern = ".ython"
	matches = re.findall(pattern,text)
	print(matches) # ['python', 'Python', 'python', 'python']
	print(len(matches)) # 4
'''

# iter() : Devuelve un iterador que contiene todos los resultados de la busqueda detalladamente
text = "Me gusta python. Python es lo maximo. Aunque python no es tan dificil, ojo con python."
pattern = "python"
matches = re.finditer(pattern,text)
for item in matches:
	print(item.group(), item.start(), item.end()) #python 9 15 \npython 45 51 \npython 79 85
''' 
 Otra forma, colocando solamente 'print(item)' devuelve los detalles de cada iteracion
	<re.Match object; span=(9, 15), match='python'>
	<re.Match object; span=(45, 51), match='python'>
	<re.Match object; span=(79, 85), match='python'>
'''

######## EJERCICIO 02 ########
''' Encuentra todas las ocurrencias de la palabar 'midudev' en el siguiente texto
e indica en que pocicion empieza y termina cada coinsidencia y cuantas veces e encontro '''
text = "Este es el curso de python de midudev. Suscribete a midudev su te gusta el cntenido. midudev."
pattern = 'midudev'
matches = re.finditer(pattern,text)
for item in matches:
	print(' ',item) # Imprime informacion detallada de cada iteracion
print('Las coinsidencias encontradas son', len(re.findall(pattern,text))) # Las coinsidencias encontradas son 3

# MODIFICADORES
# Los modificdores son opciones que se pueden agregar a un patron para cambiar su comportamiento
# re.IGNORECASE : Ignora su escritura, es decir que no es sencible a las mayusculas y minusculas
text = "Todo el mundo dice que la IA nos va a quitar el trabajo. Pero solo hace falta ver como la Ia usa mas ia"
pattern = "IA"
found = re.findall(pattern, text, re.IGNORECASE)
print(found) # ['IA', 'Ia', 'ia']

######## EJERCICIO 03 ########
''' Encuentra todas las ocurrencias de la palabra "pithon" en el siguiente texto, 
sin distinguir mayusculas y minusculas '''
text = "Este es el curso de python de midudev. Suscribete a python si te gusta mi contenido, PYTHON"
pattern = "PYTHON"
foun = re.findall(pattern,text, re.IGNORECASE)
print(foun) # ['python', 'python', 'PYTHON']

# REMPLAZAR TEXTO
# .sub() remplaza todas las coincidencias de un patron en un texto
text = "Hola mundo. Hola de nuevo. hola"
pattern = "Hola"
replace = "adios"
new_text = re.sub(pattern, replace,text)
print(new_text) # adios mundo. adios de nuevo. hola
new_text = re.sub(pattern, replace,text, 1) # Se agrego el numero de veces que se remplazara, por defecto es 0
print(new_text) # adios mundo. Hola de nuevo. hola
new_text = re.sub(pattern, replace, text, 0 , re.IGNORECASE) # Se agrego un modificador
#NOTA: siempre que se agregue un modificador hay que espesificar numero de veces a remplazar o solo poner "flags=<modificador> sin el numero de veces"
print(new_text) # adios mundo. adios de nuevo. adios

