'''
Crear un programa que llames desde treminal y Scrapee una pagina web, desde linea de comandos
'''

import requests
import argparse # Parsea argumentos

from bs4 import BeautifulSoup
from urllib.parse import urljoin

parser = argparse.ArgumentParser(description="Web scraping to check SEO for a given URL")
parser.add_argument('url',type=str, help="The URL of the site you want to scrape and check")
args = parser.parse_args()
url = args.url # La URL con la que se trabaja es pasada por el usuario desde la linea de comandos (como argumento)

headers = {
	"UserAgent":'Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; Googlebot/2.1; +http://www.google.com/bot.html) Chrome/135.0.0.0 Safari/537.36'
}
response = requests.get(url,headers=headers)
if response.status_code == 200:
	print('Peticion exitosa :)')

	soup = BeautifulSoup(response.text, 'html.parser') # Crear la sopa con el html manejable
	print(f'Revisando la pagina: {url}')
	print('\n\33[33mSEO basico:\33[0m')
	titulo = soup.title.string
	print('\33[41mTitulo de la pagina:\33[0m',titulo)
	if len(titulo)<70:
		print('Titulo de la pagina aceptable.')
	else:
		print('Titulo demasiado largo.')

'''
COLOR (lineas de comando)
Existe formas de presentar el resultado en terminal en colores, explicaremos una:
	-> [ANSI escape code]
 * [informacion] : https://en.wikipedia.org/wiki/ANSI_escape_code
 *Permite añadir colores de manera sensilla a la salida por consola
 *FG(color de letra) y BG(color de resaltado)
 *Con '\033[<codigo_color>m' iniciamos el escape (cambio de color) y lo finalizamos con '\33[0m'
'''

# Extraer los titulos h1
titulos = [titulo.text for titulo in soup.find_all('h1')]
if not titulos:
	print('\33[41mNo se encontraron titulos H1 en la pagina[0m')
elif len(titulos) > 1:
	print('\33[31mHay mas de un titulo H1 en la pagina\33[0m')
	for titulo in titulos:
		print(titulo)
else:
	print('\33[32mHay un titulo H1 en la pagina\33[0m')