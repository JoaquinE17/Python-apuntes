# INTRODUCCION A LAS CLASES EL PYTHON ------------------------------------------------------------------------------------------------------------------------------------------>

# Envocar api
# dotenv -> Si no tienes el paquete 'dotenv' instalado, instálalo. Si trabajas en Python, puedes usar el paquete 
#'python-dotenv' para cargar las variables de entorno. El comando es 'pip install python-dotenv'.
from dotenv import load_dotenv
import os
load_dotenv() # cargar el .env
api_key = os.getenv('API_KEY') # acceder a 'API_KEY'

# Las clases son plantillas para crear objetos. Un objeto es una instancia de una clase.
# Nos permite agrupar datos (atributos o propiedades) y funciones (metodos) en un solo lugar

# Ejemplo basico de una clase:
class coche:
	# Atributo de clase (comparte todas las instancias)
	tipo = 'veiculo de cuatro ruedas'

	# Metodo especial que el que construye un objeto
	# Se llama automaticamente este método cuando se crea la instancia
	def __init__(self, marca, modelo, color):
		# Atribtos de la instancia
		self.marca = marca
		self.modelo = modelo
		self.color = color

	def arrancar(self):
		print(f"El coche {self.marca} {self.modelo} arranco")

print('Ejemplo basico:')
micoche = coche('toyota', 'corola', 'rojo')  
micoche.arrancar() #El coche toyota corola arranco

# ENCAPSULACION: es ocultar los detalles internos de una clase y exponer solo la interfaz publica

# CREAR UNA CLASE PARA LLAMAR A LA IA DE OPENAI, DEEPSEEK O LO QUE SEA:
import requests

OPENAI_KEY = "sk-XXXXXXXXXXXXXXXX"
DEEPSEEK_KEY = api_key

class API_AI:
	def __init__(self,api_key, url, model):
		self.api_key = api_key
		self.url = url
		self.model = model

	def call(self, prompt):
		headers = {
			"Content-Type": "application/json",
			"Authorization": f"Bearer {self.api_key}"
		}
		data = {
			"model": self.model,
			"messages": [{'role':'user', 'content':prompt}]
		}
		reponse = requests.post(self.url, json=data, headers=headers)
		res_json = reponse.json()
		print(res_json['choices'][0]['message']['content'])

print('\nOpenAI:')
#openAI = API_AI(OPENAI_KEY,"https://api.openai.com/v1/chat/completions","gpt-4o-mini")
#openAI.call("Escribe una adivinanza breve")

print('\nDeepseek:')
deepseek = API_AI(DEEPSEEK_KEY,"https://api.deepseek.com/chat/completions","deepseek-chat")
deepseek.call("Escribe una adivinanza breve")

'''
Deepseek:
{'id': '9dc99a8f-4b67-4819-b01e-a1bd049d7691', 
'object': 'chat.completion', 
'created': 1741727699, 
'model': 'deepseek-chat',

'choices':  [{'index': 0,
 			  'message': {'role': 'assistant', 
 			  'content': 'Claro, aquí tienes una adivinanza breve:\n\n**"Blanco por dentro, verde por fuera. Si quieres que te lo diga, espera."**\n\n¿Sabes qué es? 😊'},  <--- [message_output]
  			  'logprobs': None, 'finish_reason': 'stop'
  			}], 

'usage': {  'prompt_tokens': 10,
  		    'completion_tokens': 45,
  		    'total_tokens': 55, 
  		    'prompt_tokens_details': {'cached_tokens': 0}, 
  		    'prompt_cache_hit_tokens': 0,
  		    'prompt_cache_miss_tokens': 10
  		 }, 
'system_fingerprint': 'fp_3a5770e1b4_prod0225'}
'''