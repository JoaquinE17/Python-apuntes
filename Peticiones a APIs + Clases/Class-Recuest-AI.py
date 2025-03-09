# INTRODUCCION A LAS CLASES EL PYTHON ------------------------------------------------------------------------------------------------------------------------------------------>

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
DEEPSEEK_KEY = "sk-XXXXXXXXXXXXXXXX"

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
		print(res_json['error']['message'])

print('\nOpenAI:')
openAI = API_AI(OPENAI_KEY,"https://api.openai.com/v1/chat/completions","gpt-4o-mini")
openAI.call("Escribe una adivinanza breve")

print('\nDeepseek:')
deepseek = API_AI(DEEPSEEK_KEY,"https://api.deepseek.com/chat/completions","deepseek-chat")
deepseek.call("Escribe una adivinanza breve")