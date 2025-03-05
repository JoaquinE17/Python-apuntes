#NUMERIC TYPES -------------------------------------------------------------------------------------------------------------------------------->
x = 1		#int
y = 2.8		#float
z = 1j		#complex (j->parte imaginaria)
print(x,'|',y,'|',z)

a = float(x)	#convercion int a float
b = int(y)		#convercion float a int
c = complex(x)	#convercion int a complex
print(a,'|',b,'|',c)

import random	#numeros aleatorios
print(random.randrange(1,100))

#Casting (fundicion) -> convertir un tipo a otro
x=int(1)	# x=1
y=int(2.8)	# y=2	
z=int('5')	# z=5

x=float(1)		# x=1.0
y=float(2.8)	# y=2.8
z=float('5')	# z=5.0
w=float("4.2")	# w=4.2

x=str('s3')	# x='s3'
y=str(2)	# y='2'
z=str(3.0)	# z='3.0'
