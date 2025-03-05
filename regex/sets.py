# CONJUNTOS ------------------------------------------------------------------------------------------------------------------------------------>
import re

# [] : Coincide con cualquier sentencia o caracter dentro de los corchetes
'''
username = "rub.ius_6$9"
pattern = r"[\w._%+-]+"
match = re.search(pattern,username)
if match:
	print("El nombre es valido:", match.group()) # El nombre es valido: rub.ius_6  <------
else:
	print("El nombre no es valido")
'''
# El uso de los metacaracteres (^ , $) es para que al momento de revisar la cadena me lea de principio a fin sin cortarce y de un falso-positivo
username = "rub.ius_69"
pattern = r"^[\w._%+-]+$"
match = re.search(pattern,username)
if match:
	print("El nombre es valido:", match.group()) # El nombre es valido: rub.ius_69 <------
else:
	print("El nombre no es valido")

# Buscar las vocales en una cadena
text = "Hola mundo"
pattern = r"[aeiou]"
print(re.findall(pattern,text)) # ['o', 'a', 'u', 'o']

# Una regex para encontrar las palabras 'man,fan,ban' pero ignora el resto
text = "man ran fan ñan ban fon fan"
pattern = r"[mfb]an"
print(re.findall(pattern,text)) # ['man', 'fan', 'ban', 'fan']

######## EJERCICIO 01 ########
# Busca las palabras 'man,fan,ban' en las siguiente cadena
text = "omniman fanatico man bandana"
pattern = r"\b[mfb]an\b"
print(re.findall(pattern,text)) # ['man']

# Para espesificar un rango utiliza '[m-n]' estos (m,n) pueden ser de cualquier tipo (letras,numeros,letras con acento,simbolos) 
text = "52452"
pattern = r"[1-4]"
print(re.findall(pattern,text)) # ['2', '4']

text = "sadaSD12"
pattern = r"[a-z]"
print(re.findall(pattern,text)) # ['s', 'a', 'd', 'a']

text = "sadaSD12"
pattern = r"[A-Z]"
print(re.findall(pattern,text)) # ['S', 'D']

# Incluso puedes combinarlas
text = "sadaSD12"
pattern = r"[a-zA-Z0-9]"
print(re.findall(pattern,text)) # ['s', 'a', 'd', 'a', 'S', 'D', '1', '2'] 

# [^] : Le decimos que busque cualquier caracter que NO esté dentro de los cochetes
text = "Hola mundo"
pattern = r"[^aeiou]" # Buscame todas las letras que no sean vocales
print(re.findall(pattern,text)) # ['H', 'l', ' ', 'm', 'n', 'd']

######## EJERCICIO FINAL ########
''' Con todo lo aprendido mejorar esto: https://www.computerhope.com/jargon/r/regular-exprecion.png
## Buscar carner-cases que no pasen y arreglarlo:
	* 'lo.que+sea@shopping.online'
	* 'nichael@gov.co.uk'
'''
