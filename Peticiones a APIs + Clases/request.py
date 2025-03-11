# REQUEST API -------------------------------------------------------------------------------------------------------------------------------------->

# Envocar api
# dotenv -> Si no tienes el paquete 'dotenv' instalado, instálalo. Si trabajas en Python, puedes usar el paquete 
#'python-dotenv' para cargar las variables de entorno. El comando es 'pip install python-dotenv'.
from dotenv import load_dotenv
import os
load_dotenv() # cargar el .env
api_key = os.getenv('API_KEY') # acceder a 'API_KEY'

## PETICIONES A APIs CON PYTHON
#  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#########################################################################################################
# SIN DEPENDENCIAS (modulos nativos) # 																	#
###################################### 																	#
																										#
# Para ello importamos dos librerias:																	#
import urllib.request # habre una URL y realiza las consultas que le especifiquemos						#
import json # Transforma la respuesta de 'urllib.request' a una 'json'									#
 																										#
''' 																									#
Utiliza las APIs de esta pagina para practicar y hacer los siguientes ejemplos:   						#
	- https://jsonplaceholder.typicode.com/ 															#
''' 																									#
																										#
print("\n> URLLIB (sin dependencias):")																	#
api_post = "https://jsonplaceholder.typicode.com/posts" 												#
 																										#
try:  																									#
	response = urllib.request.urlopen(api_post) # Abre la 'api_post' y guardala en 'response' 			#
	data = response.read() # Lee el 'response' y guardalo en data 										#
	json_data = json.loads(data.decode('utf-8')) # Convierte (decodifica) 'data' a un formato 'json'    #
	print(json_data[1]) # [{'userId': 1, 'id': 1, 'title': 'sunt aut facere repellat...   				#
	response.close() # NO te olvides de cerrar 'response' sino quedara abierto  						#
except urllib.error.URLError as e:  																	#
	print(f"Error en la solisitud: {e}") 																#
 																										#
''' 																									#
En estos casos es mejor usar 'try/except' por si ocurre algun problema el programa 						#
no se rompa. 																							#
''' 																									#
#########################################################################################################

#################################################################################################################################################
# CON DEPENDENCIAS (requests) #  																											    #
###############################       																											#
''' 																																			#	
Lo primero es instalar las dependencias, por defecto el instalador de paquetes de 	                   											#
python es 'pip' pero existen otros como 'uv' 																									#
Las librerias a utilizar pueden ser otras, existe una gran variedad. 																			#
'''                                  																											#
# Paso 1: instalar el modulo 'requests'. En terminal ejecutar el comando: 																		#
		#	pip install requests 																												#
# Paso 2: Despues necesitas importarlo para que pueda ser utilizado: 																			#
import requests 																																#
# Y con eso ya podras usar la libreria 																											#
print("\n> REQUESTS (con dependencias):")																										#
api_post = "https://jsonplaceholder.typicode.com/posts"																							#
response = requests.get(api_post)																												#
#print(response.json()) -> Devuelve la API completa en formato JSON 																			#
post = response.json()																															#
print("El tercer posteo es:",post[2]) # Devuelve el tercer post: {'userId': 1, 'id': 3, 'title': 'ea molestias quasi exercitationem repellat... #
																																				#
#################################################################################################################################################


# REALIZAR UN POST:
# Esto permite insertar nuevos elementos, si la API lo permite

print('\n> POST:') 
api_post = "https://jsonplaceholder.typicode.com/posts"
inputt = {
		'title': 'example_test',
		'body': 'developer inside',
		'user_ID': 5	}
response = requests.post(api_post, json=inputt)
print(response.json()) # {'title': 'example_test', 'body': 'developer inside', 'user_ID': 5, 'id': 101}
print("El codigo de estado es:",response.status_code) # 201

''' Forma optimizada:
response = requests.post(
	"https://jsonplaceholder.typicode.com/posts",
	json = {
		'title': 'example_test',
		'body': 'developer inside'
		'user_ID': 5  })
print(response.json()) # {'title': 'example_test', 'body': 'developer inside', 'user_ID': 5, 'id': 101} '''

# Probando error con try/except:
print('\n> POST (try/except):')
try:
	response = requests.post(
		"https://jsonplaceholder.typicode.d",
	 	json = {
			'title': 'example_test',
			'body': 'developer inside',
			'user_ID': 5	})
	print(response.json())
	print("El codigo de estado es:",response.status_code)
except requests.exceptions.RequestException as e:
	print(f"Error en la solicitud: {e}") # Error en la solicitud: HTTPSConnectionPool(host='jsonplaceholder...


# REALIZAR UN PUT:
# Esto permite actualizar un elemento, si la API lo permite

print('\n> PUT:')
api_put = "https://jsonplaceholder.typicode.com/posts/2"
inputt = {
		'title': 'example_test',
		'body': 'developer inside',
		'user_ID': 5	}
response = requests.put(api_put, json=inputt)
print(response.json()) # {'title': 'example_test', 'body': 'developer inside', 'user_ID': 5, 'id': 2}
print("El codigo de estado es:",response.status_code) # 200

''' Forma optimizada con try/except:
try:
	response = requests.put(
		"https://jsonplaceholder.typicode.com/posts/2",
	 	json = {
			'title': 'example_test',
			'body': 'developer inside',
			'user_ID': 5	})
	print(response.json()) #{'title': 'example_test', 'body': 'developer inside', 'user_ID': 5, 'id': 2}
	print(response.status_code) # 200
except requests.exceptions.RequestException as e:
	print(f"Error en la solicitud: {e}") 
'''


# RECUEST API DE IA:
import requests
import json

## REQUEST API DE OPENAI:
# Lo primero que necesitas es obtener una clave de acceso, esta se la consigue ingresando al siguiente enlase:
#	- https://platform.openai.com/settings/organization/api-keys

print("\n> Open AI:")

OPENAI_KEY = "sk-XXXXXXXXXXXXXXXX"

def call_openai_gpt(api_key, prompt):
	url = "https://api.openai.com/v1/chat/completions"
	headers = {
		'Content-Type': 'application/json',
		'Authorization': f'Bearer {api_key}'
	}
	data = {
		'model': 'gpt-4o-mini',
		'messages': [{'role':'user', 'content': prompt}]
	}
	response = requests.post(url, json=data, headers=headers)
	return response.json()

api_response = call_openai_gpt(OPENAI_KEY,"Escribe un poema sobre programacion")
print(api_response['error']['message']) 


## REQUEST API DE DEEPSEEK:
# Lo primero que necesitas es obtener una clave de acceso, esta se la consigue ingresando al siguiente enlase:
#	- https://platform.deepseek.com/api_keys

print("\n> DEEPSEEK:")

DEEPSEEK_KEY = api_key

def call_deepseek(api_key, prompt):
	url = "https://api.deepseek.com/chat/completions"
	headers = {
		'Content-Type': 'application/json',
		'Authorization': f'Bearer {api_key}'
	}
	data = {
		'model': 'deepseek-chat',
		'messages': [{'role':'user', 'content': prompt}]
	}
	response = requests.post(url, json=data, headers=headers)
	return response.json()

api_response = call_deepseek(DEEPSEEK_KEY,"Escribe una idea sobre programacion")
print(api_response['choices'][0]['message']['content']) 


 