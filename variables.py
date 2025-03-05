#ASIGNACION MULTIPLE  ------------------------------------------------------------------------------------------------------------------------->

#Desempaquetar una lista a multiples variables
frutas=["pera", "banana", "naranja"]
x,y,z=frutas
print(x,y,z) #pera banana naranja

#Multiples valores a multiples variables 
x,y,z="rata","caballo",'serpiene'
print(x,y,z) #rata caballo serpiente 

#Un valor a multiples variables
x=y=z='ordenador' 
print(f"x = {x}, y = {y}, z = {z}") #x = ordenador, y = ordenador, z = ordenador

#VARIABLES GLOBALES---------------------------------------------------------------------------------------------------------------------------->
x="ganador"#---> VARIABLE GLOBAL
def mi_funcion():
	x='perdedor'#--- >VARABLE LOCAL
	print('Pablo es', x) #Pablo es perdedor
mi_funcion()
print('Pablo es', x)#Pablo es ganador

#MODIFICACION DE VARIBLE GLOBAL---------------------------------------------------------------------------------------------------------------->
y='idolo'#---> VARIABLE GLOBAL
def mi_funcion2():
	global y 
	y= 'crack'#---> VARIABLE GLOBAL(modificada)
mi_funcion2()
print('Pablo es', y) #Pablo es crack

#SEP - END en print():
print(1,2,3,sep='-') #1-2-3
print(f'Pablo es, {y}', end='!') #Pablo es, crack!1 2 3
print(1,2,3)

#VARIABLE - TIPADO DINAMICO
#En python una variable puede variar en sus tipos (bool,int,str,etc) durante la ejecucion del codigo
mi_variable = 'Hola'
print(type(mi_variable)) #<class 'str'>
mi_variable = 23
print(type(mi_variable)) #<class 'int'>

#VARIABLE - INPUT
#Lo que se ingresa en el input siempre va a ser un 'str' (cadena de texto)
edad = input('ingresa tu edad: ')
print(f'dentro de 20 años tendras {int(edad)+20}') #dentro de 20 años tendras 65

nombre, apellido = input('ingresa tu nombre y apellido: ').split(' ')
print(f'Hola {nombre} {apellido}')
print(type(nombre))
print(type(apellido))

job = input('pulse enter para salir')