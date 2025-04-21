'''
Realizar un scraping de la pagina de wikipedia
'''
from bs4 import BeautifulSoup
import requests
from urllib.parse import urljoin # Este 'urljoin' lo que hace es presentar de una forma mas legible las distintas direcciones (URLs) que contiene la pagina (html)

url = "https://midu.dev"#"https://es.wikipedia.org/wiki/Web_scraping"
response = requests.get(url)
if response.status_code == 200:
	print("Peticion exitosa :)")
	soup = BeautifulSoup(response.text, 'html.parser') # [html.parser] anliza el archivo html y lo convierte en un formato manejable 

	# Extraer todos los titulos <h1>
	titulos = [titulo.string for titulo in soup.find_all('h2')]
	print('El titulo de la pagina es:',titulos)
	
	# Extraer todos los enlaces <a>
	enlaces = [urljoin(url,enlace.get('href')) for enlace in soup.find_all('a')] # [enlace.get('href')] -> Para cada enlace que encontres en el html solo extraeme los atributos 'href'
	#print(enlaces) # Sin el uso de 'urljoin' el resltado obtenido es confuso y dificil de leer, mejor importar la libreria 'urllib.parse'
	
	# Extraer todo el contenido de la pagina de texto
	#all_text = soup.get_text()
	#print(all_text)

	# Extraer el texto del elemento main
	#main_text = soup.find('main').get_text()
	#print(main_text)

	# Extraer de la id mw-content-text
	#content_text = soup.find('div',{'id':'mw-content-text'}).get_text()
	#print(content_text)
	# Otra forma de hacer esto:
	#content_text = soup.find('div',id='mw-content-text').get_text()
	#print(content_text)	

	# Extraer el open graph (si existe) -> wikipedia no tiene este elemento, intentarlo con [https://midu.dev]
	og_image = soup.find('meta',{'property':'og:image'})
	if og_image:
		print(og_image['content'])
	else:
		print('No se encontro la imagen')
	# Otra forma de aser esto:
	og_image = soup.find('meta',property='og:image')
	if og_image:
		print(og_image['content'])
	else:
		print('No se encontro la imagen')
	# En caso de tener mas de un elemento en uno de sus parametros se recomienda usar un diccionario