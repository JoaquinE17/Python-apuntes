# CUANTIFICADORES ------------------------------------------------------------------------------------------------------------------------------------------------>
''' Los cuantificadores se utilizan para especificar cuantas ocurrencias de un caracter 
o grupo de caracteres se deben encontrar en una cadena'''

import re

# * : El caracter o cadena especificada puede aparecer 0 o mas veces
text = "aaaaba"
pattern = "a*"
print(re.findall(pattern,text)) # ['aaaa', '', 'a', '']

######## EJERCICIO 01 ########
# Cuantas palabras tienen de 0 a mas 'a' y despues una 'b'
#. . .

# + : El caracter o cadena espesificado, aparece 1 o mas veces
text = "aaaa bbba ccc a caca"
pattern = "a+"
print(re.findall(pattern,text)) # ['aaaa', 'a', 'a', 'a', 'a']

# ? : El caracter o cadena espesificado aparece 0 o 1 vez, es decir que sea opcional el caracter especificado
text = 'aaabacb'
pattern = "a?b"
print(re. findall(pattern,text)) # ['ab', 'b']

######## EJERCICIO 02 ########
# Haz opcional que aparezca un '+34' en el siguiente texto
phone = '+34 6889999999'

# {n} : Verifica que la sentencia dada se repita exactamente 'n' veces
text = "aaaaaa  aa  aaaa a a a"
pattern = "a{3}"
print(re.findall(pattern,text)) # ['aaa', 'aaa', 'aaa']

#{n,m} : Verifica que la sentencia dada se repita 'n' a 'm' veces. Si quereemos que sea a partir de un numero se coloca '{n,}'
text = "u uu uuuu u uuu"
pattern = r"\bu{2,3}\b"
print(re.findall(pattern,text)) #['uu', 'uuu']

######## EJERCICIO 03 ########
# Encuentra las palabras de 4 a 6 letras en el siguiente texto
words = "ala casa arbol leon cinco murcielago"
pattern = r"\b\w{4,6}\b"
print(re.findall(pattern,words)) # ['casa', 'arbol', 'leon', 'cinco']
'''
# Sin el \b el resultado seria:

words = "ala casa arbol leon cinco murcielago"
pattern = r"\w{4,6}"
print(re.findall(pattern,words)) # ['casa', 'arbol', 'leon', 'cinco', 'murcie', 'lago']
'''

######## EJERCICIO 04 ########
# Encuntra las palabras de mas de 6 letras
words = "ala casa arbol leon cinco murcielago"
pattern = r"\b\w{5,}\b"
print(re.findall(pattern,words)) # ['arbol', 'cinco', 'murcielago']