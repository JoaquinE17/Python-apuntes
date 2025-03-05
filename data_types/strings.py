#STRINGS TYPES ------------------------------------------------------------------------------------------------------------------------------->
print("Pinta vinito")	# Pinta vinito
print("Pinta 'vinito'")	# Pinta 'vinito'
print('"Pinta" vinito')	# "Pinta" vinito

x= "hola"
y= 'Octavio'
print(x,y)

a="""Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua"""

b='''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua'''
print(a,'\n',b)

#SON ARRAYS ---------------------------------------------------------------------------------------------------------------------------------->
a='hola, mundo'
print(a[1]) #o

#Recorrer array
for x in "banana":
	print(x)

#Saber su longitud 
a= "Hola, dumbo!"
print(len(a)) #12		##### METODO #####
	
#Revisar coincidencias
txt= "La mejor vida del mundo"
print('mundo' in txt)	#True

#Utilizarlo en un condicional
if "mundo" in txt:
	print("Efectivamente es tu mundo")

txt='Lo mejor es el rock'
print('pop' not in txt)	#True

if 'pop' not in txt:
	print('Aguante el rock!!')

#SLICING (sintaxis de corte) ----------------------------------------------------------------------------------------------------------------->
a= 'hola, donald'
print(a[2:5])	#la, -> (la pocicion 5 no se incluye)

b= "Hola, mickey"
print(b[:5])	#Hola, -> (comienza desde el inicio hasta la pocicion 5(que no se incluye))

c= 'Hola, gufi'
print(c[2:])	#la, gufi -> (comienza desde la pocicion 2 hasta el final)

#Indice negativo
a= 'hola, donald'
print(a[-5:-2])	#ona -> (no incluye las pociciones -5(d) y -2(l))

#CONCATENACION ------------------------------------------------------------------------------------------------------------------------------->
a= "hola"
b= "mundo"
c= a+b
print(c) #holamundo

a= "hola"
b= "mundo"
c= a+" "+b
print(c) #hola mundo

#F-STRING (formatar cadenas) ----------------------------------------------------------------------------------------------------------------->
age=36
txt=f"Mi nombre es Jhon, tengo {age} años"
print(txt) #Mi nombre es Jhon, tengo 36 años

precio= 34
txt=f"El dolar a la venta esta {precio:.2f} pesos"	# modificador (:) rendodeo a dos desimales
print(txt) #El dolar a la venta esta 34.00 pesos

txt=f"Mi nombre es Jhon, tengo {6*2} años"	# operaciones
print(txt) #Mi nombre es Jhon, tengo 12 años

#Indice con nombre
txt='Soy {nombre}, tengo {edad} años..'
print(txt.format(nombre='Juan',edad=19)) #Soy Juan, tengo 19 años..

#Indice enumerado
txt='Me gusta {0} y {1}..'
print(txt.format('jugar','estudiar')) #Me gusta jugar y estudiar

#Marcadores de pocicion vacios
txt='Mi deporte favorito es el {} y el {}..'
print(txt.format('futbol','basquet')) #Mi deporte favorito es el futbol y el basquet

#CARACTERES DE ESCAPE ------------------------------------------------------------------------------------------------------------------------>
print("\'gufi\' es un perro") # comillas simples
print("micky \\maus\\ es el raton") # barra invertida
print("micky y gufi \n- son de disney") # nueva linea
print("miny es \r una ratoncita") # retorno
print("donald es \t presidente") # tabulador
print("pluto es una \bmascota") # retrocede un espacio
#formato octal (\ooo) -> "\110\145\154\154\157" --> hello
#formato hexadesimal (\xhh) -> "\x48\x65\x6c\x6c\x6f" --> hello

#MODIFICAR STRING ---------------------------------------------------------------------------------------------------------------------------->
a= 'hola, donald'
print(a.upper())	#HOLA, DONALD -> (devuelve la cadena en mayusculas)		##### METODO #####

b= "Hola, mickey"
print(b.lower())	#hola, mickey -> (devuelve la cadena en minusculas)		##### METODO #####

c= " Hola, gufi "
print(c) #| Hola, gufi |
print(c.strip())	#|Hola, gufi| -> (elimina espacio en blanco inicio y fin)		##### METODO #####
print(c.lstrip())	#|Hola, gufi | -> (elimina espacio en blanco del inicio)		##### METODO #####
print(c.rstrip())   #| Hola, gufi| -> (elimina espacio en blanco del final)			##### METODO #####

d= 'hola, donald'
print(d.replace("h","J"))	#Jola, donald -> (remplazar una cadena por otra)		##### METODO #####

e="diario del lunes"
print(e.title()) #Diario Del Lunes -> (Convierte el primer caracter en mayusculas)		##### METODO #####

f="martes de chaya"
print(f.center(20,'$')) #$$martes de chaya$$$ -> (centra la cadena dada)		##### METODO #####

g="miercoles negro"
print(g.ljust(20,'*')) #miercoles negro***** -> (acomoda la cadena a la izquierda)		##### METODO #####
print(g.rjust(20,'*')) #*****miercoles negro -> (acomoda la cadena a la derecha)		##### METODO #####

#SPLIT -> Divide una cadena en sub-elementos de una lista, usando el argumento de la funcion
y= 'Hola, gufi'	
print(y.split(","))	#['Hola', 'gufi'] -> (Separador utilizado ',')		##### METODO #####

#JOIN - Convierte los sub-elementos de una lista en una cadena, usando el argumento anterior a la funcion como separador
z= ['hola','pluto','depierta']
print('***'.join(z)) #hola***pluto***depierta -> (Separador utilizado '***')		##### METODO #####
#		[ "<separador_a_usar>".JOIN(<cadena>) ]

# METODOS ------------------------------------------------------------------------------------------------------------------------------------>
s="ExtrUaño MUndao "
letra1=s.find('U') #4 -> (Busca la primera ocurrencia, devuelve su pocicion, si no se encuentra devuelve -1)
letra2=s.rfind('a') #12 -> (Busca la ultima ocurrencia, devuelve su pocicion, si no se encuentra devuelve -1) 
letra3=s.count(' ') #2 -> (Cuenta parametro pasado al metodo)
letra4=s.capitalize() #Extraño mundo -> (Standeriza - normaliza la cadena) 
letra5=s.swapcase() #eXTRAÑO muNDO -> (Invierte cada caracter, mayuscula a minuscula y viceversa)
letra6=s.zfill(20) #0000000Extraño MUndo -> (Completa con '0' los caracteres faltantes, para llegar al valor del argumento)

cad='355544'
a=cad.isdigit() #[True] -> (true si cad es todo numeros)
b=cad.isalnum() #[True] -> (true si cad es todo numeros o todo caracteres alfabeticos)
c=cad.isalpha() #[False] -> (true si cad es todo caracteres alfabeticos solo minusculas)
d=cad.islower() #[False] -> (true si cad tiene minusculas -numeros,espacios y signos de puntuacion-)
e=cad.istitle() #[False] -> (true si la primera letra de cada es mayusculas)
f=cad.isspace() #[False] -> (true si cad es todo espacios)
g=cad.startswith('3') #[True] -> (true si cad comienza con el prefijo espesificado)

#CONVERSIONES -------------------------------------------------------------------------------------------------------------------------------->
#Los caracteres mapean a numeros usando el estandar ASCII y Unicode.
#  ord(<texto>) -> convierte un string a un numero segun el codigo ASCCI
print("a =",ord("a"))# -> 97 
print("b =",ord("b"))# -> 98
#  chr(<numero>) -> Convierte numero a un string
print("120 =",chr(120))# -> 'x'
print()

#EXPRECIONES REGULARES ----------------------------------------------------------------------------------------------------------------------->
# Una limitación de las operaciones básicas de las cadenas es
# que no ofrecen ningún tipo de transformación usando
# patrones más sofisticados. Para eso vas a tener que usar el
# módulo re y aprender a usar expresiones regulares. El
# manejo de estas expresiones es un tema en sí mismo.
# Encontrar las fechas en el texto

import re
texto = 'Hoy es 22/05/2023. Mañana será 23/05/2023.'
lista = re.findall(r'\d+/\d+/\d+', texto)
print(lista) #['22/05/2023', '23/05/2023']
# Cambiar el formato
texto2 = re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\2-\1', texto)
print(texto2) #'Hoy es 2023-05-22. Mañana será 2023-05-23.'
print()