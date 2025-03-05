'''
Python divide a los operadores en los siguientes grupos:
	Operadores aritméticos
	Operadores de asignación
	Operadores de comparación
	Operadores lógicos
	Operadores de identidad
	Operadores de membresía
	Operadores bitwise
'''

#OPERADORES ARITMETCOS ----------------------------------------------------------------------------------------------------------------------->
#Se utilizan con valores numéricos para realizar operaciones matemáticas comunes:
print("Suma 3 + 5 =",3+5) #8 (adicion)
print("Resta 3 - 1 =",3-1) #2 (substraccion)
print("Multiplicacion 3 * 5 =",3*5) #15
print("Divicion 25 / 4 =",25/4) #6.25
print("Modulo 25 % 4 =",25%4) #1
print("Div. (entera) 25 // 4 =",25//4) #6
print("Exponenciacion 5 ** 3 =",5**3) #125 

#OPERADORES ASIGNACION ----------------------------------------------------------------------------------------------------------------------->
#Se utilizan para asignar valores a las variables:
x = 5 #Asignacion simple
x+=3 #[x=x+3]
x-=3 #[x=x-3]
x*=3 #[x=x*3]
x/=3 #[x=x/3]
x%=3 #[x=x%3]
x//=3 #[x=x//3]
x**=3 #[x=x**3]

#A nivel de bits:
y=12
y&=3 #[x=x&3] -> AND |0101 AND 0011 == 1
y|=3 #[x=x|3] -> OR  |0101 OR 0011 == 111(7)

#Desplazamiento:
y^=3 #[x=x^3] -> XOR (compara los bits de ambos operandos y devuelve 1 solo cuando los bits son diferentes) |0101 XOR 0011 == 0110(6)
y>>=3 #[x=x>>3] -> Desplazamiento de bits a la derecha |0101 >> 3 == 0010->0001->0000->[0]
y<<=3 #[x=x<<3] -> Desplazamiento de bits a la izquierda |0101 << 3 == 01010->010100->[0101000](40)
#Este desplazamiento es equivalente a dividir (divicion entera) o multiplicar la variable, por 2 elevado al número de posiciones desplazadas
#	Calculo aritmetico (desplazaamiento derecha): x // 2^y = z
#	Calculo aritmetico (desplazamiento izquierda): x * 2^y = z	

#Operador Warlus:
print(y:=3) #[x=3][print(x)] -> Permite asignar un valor a una variable como parte de una expresión.

#OPERADORES COMPARACION ---------------------------------------------------------------------------------------------------------------------->
#Se utilizan para comparar dos valores:
print("Igualdad 4==4:",4==4) #True
print("Distinto 12!=12:",12!=12) #False 
print("Mayor que 34>4:",34>4) #True 
print("Menor que 12<24:",12<24) #True 
print("Mayor igual que 14>=34:",14>=34) #False 
print("Menor igual que 41<=54:",41<=54) #True 

#OERADORES LOGICOS --------------------------------------------------------------------------------------------------------------------------->
#Se utilizan para combinar declaraciones condicionales:
z=34
print(z<23 and z>8) #False 
print(z<43 or z <56) # True
print(not(z<23 and z>8)) #True

#OPERADORES DE IDENTIDAD --------------------------------------------------------------------------------------------------------------------->
#Se utilizan para comparar los objetos, no si son iguales, sino si en realidad son el mismo objeto, 
#es decir, si tienen la misma ubicación de memoria:
# Diferencia entre 'is' y '=='; 'is not' y '!=' : 
#	'==' : Verifica si los valores dentro de los objetos son iguales.
#	'is' : Verifica si dos referencias apuntan al mismo objeto en memoria (misma instancia).
#	'!=' : Verifica si los valores dentro de los objetos no son iguales.
#	'is not' : Verifica si dos referencias no estan apuntando al mismo objeto en memoria (misma instancia).

x = ["apple", "banana"]
y = ["apple", "banana"]
z = x
print(x is z) #True ('z' es el mismo objeto que 'x')
print(x is y) #False ('x' no es el mismo objeto que 'y', aunque tengan el mismo contenido)
print(x == y) #True 

x = ["apple", "banana"]
y = ["apple", "banana"]
z = x
print(x is not z) #False
print(x is not y) #True
print(x != y) #False

#OPERADORES MEMBRESIA ------------------------------------------------------------------------------------------------------------------------>
#Se utilizan para probar si una secuencia se presenta en un objeto:
x = ["apple", "banana"]
print("banana" in x) #True (la secuencia 'banana' esta en la lista)
print("banana" not in x) #False
y = "zaPato"
print("P" in y) #True
print('A' not in y) #True

#OPERADORES BITWISE -------------------------------------------------------------------------------------------------------------------------->
#Los operadores de bitwise se utilizan para comparar números (binarios):
print(6&3) #0010(2) <- [0110(6) & 0011(3)] - AND
print(6|3) #0111(2) <- [0110(6) | 0011(3)] - OR
print(6^3) #0101(2) <- [0110(6) ^ 0011(3)] - XOR
print(~3) #1100(-4) <- [~0011(3)] - NOT
print(6<<3) #0110000(48) <- [0110(6)] - DESPLAZAMIENTO IZQUIERDA
print(6>>3) #0000(0) <- [0110(6)] - DESPLAZAMIENTO DERECHA

#PRESEDENCIA DE OPERADORES ------------------------------------------------------------------------------------------------------------------->
'''
	()													Parentesis	
	**													Exponenciacion	
	+x  -x  ~x											Unario más, unario menos, y bitwise NOT	
	*  /  //  %											multiplicacion, divicion, divicion entera, y modulos	
	+  -												Adicion and substraccion	
	<<  >>												Bitwise desplazamiento izquierda y derecha	
	&													Bitwise AND	
	^													Bitwise XOR	
	|													Bitwise OR	
	==  !=  >  >=  <  <=  is  is not  in  not in 		Operadores comparacion, identidad, y membresia	
	not													Logico NOT	
	and													Logico AND	
	or													Logico OR	
'''
#Si dos operadores tienen la misma precedencia, la expresión se evalúa desde la izquierda a la derecha.