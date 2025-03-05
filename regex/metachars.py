# METACARACTERES ------------------------------------------------------------------------------------------------------------------------------------------------------------------->
# Los metacaracteres son simbolos especiales con significados especificos regulares

import re

#1. El punto (.) : puede remplazar cualquier caracter pero solo uno, excepto una nueva linea
text = "Hola mundo, H0la de nuevo, H$la otra vez"
pattern = r"H.la"
print(re.findall(pattern,text)) # ['Hola', 'H0la', 'H$la']

text = 'casa caasa cosa cisa cesa causa'
pattern = 'c.sa'
print(re.findall(pattern,text)) # ['casa', 'cosa', 'cisa', 'cesa']

text = "Hola mundo. Chau.."
pattern = "." # En este caso hace alucion a todos lo caracteres de la cadena
print(re.findall(pattern,text)) # ['H', 'o', 'l', 'a', ' ', 'm', 'u', 'n', 'd', 'o', '.', ' ', 'C', 'h', 'a', 'u', '.', '.']
# - - -
text = "Hola mundo. H0la de nuevo. H$la otra vez."
pattern = r"\." # La (\) ignora el significado espesial del simbolo siguiente
print(re.findall(pattern,text)) # ['.', '.', '.']

# /d : Coincide com cualquier digito (0-9), pero solo uno
text = "El numero de telefono es 123456789"
print(re.findall(r'\d', text)) # ['1', '2', '3', '4', '5', '6', '7', '8', '9']
print(re.findall(r'\d\d\d', text)) # ['123', '456', '789']
print(re.findall(r'\d{9}', text)) # ['123456789'] | ({9}) es un cuantificador

######## EJERCICIO 01 ########
# Detecta si hay unnumero telefonico de España en el texto gracias al prefijo +34
text = "Mi numero de telefono es +34 336546545"
pattern = r'\+34 \d{9}'
found = re.search(pattern, text)
if found: print(f"Encontre el numero de telefono {found.group()}")
else: print("No la encontre")

# \w : Coincide con cualquier caracter alfanumerico (a-z, A-Z, 0-9, _)
text = "el_ rubius_69 $%"
pattern = r"\w"
print(re.findall(pattern, text)) # ['e', 'l', '_', 'r', 'u', 'b', 'i', 'u', 's', '_', '6', '9']

# \s : coincide cun cualquier espacio en blanco (espacio, tabulacion, salto de linea)
text = "Hola mundo\nComo estas?\t?"
pattern = r"\s"
print(re.findall(pattern, text)) # [' ', '\n', ' ', '\t']

# ^ : Coincide con el principio de una cadena
username = "$234_name$"
pattern = r"^\w"
valid = re.search(pattern,username)
if valid: print("El nombre es valido")
else: print("El nombre no es valido") # El nombre no es valido
# - - - 
username = "234_name$"
pattern = r"^\w"
valid = re.search(pattern,username)
if valid: print("El nombre es valido") # El nombre es valido
else: print("El nombre no es valido")

phone = "+54 453453434"
pattern = r"^\+\d{1,2} " # Cuando se utiliza rangos se debe poner un espacio al final si no queremos un numero mas largo
valid = re.search(pattern,phone)
if valid: print("El numero es valido") # El nombre es valido
else: print("El numero no es valido")

# $ : Coincide con el final de una cadena
text = "Hola mundo"
pattern = r"mundo$"
valid = re.search(pattern,text)
if valid: print("Cadena valida") # Cadena  valida
else: print("Cadena invalida")

######## EJERCICIO 02 ########
#Valida que un crreo sea gmail
text = 'miduga@gmail.com'
pattern = r"gmail.com$"
valid = re.search(pattern,text)
if valid: print("Correo valida") # Correo  valida
else: print("Cadena invalida")

######## EJERCICIO 03 ########
# Tenemos unaa lista de archivos, necesitamos saber los nombres de los ficheros con extencion '.txt'
files = "file1.txt file2.pdf midu-of.webp secret.txt"
pattern = r'\w{1,10}\.txt' # Otra forma seria [ r'\w+\.txt' ]
matches = re.finditer(pattern,files)
for item in matches:
	print(item.group()) # file1.txt \nsecret.txt

# \b : coinside con el principio o final de una palabra, permite que busquemos SOLO la sentencia que se encuentre dentro de ella 
text = "casa casada cosa cosasa casado casa"
pattern = r"\bc.sa\b"
print(re.findall(pattern, text)) # ['casa', 'cosa', 'casa']
'''
# Sin ella el resultado tendria errores y devolveria cualquier cosa

text = "casa casada cosa cosasa casado casa"
pattern = r"c.sa"
print(re.findall(pattern, text)) # ['casa', 'casa', 'cosa', 'cosa', 'casa', 'casa']
'''

# | : Funciona como un 'or' permite combinar expreciones
fruits = "banana, manzana, aguacate, palta, pera. aguacate, aguacate"
pattern = r"palta|aguacate|p..a"
print(re.findall(pattern,fruits)) # ['aguacate', 'palta', 'pera', 'aguacate', 'aguacate']
