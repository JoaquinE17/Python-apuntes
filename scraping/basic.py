# SCRAPING
'''
Web scraping:
````````````
REQUESTS: + Muy rapido
		  + Muy sencillo de implementar
		  - No puede saltarse los paywall ni los captcha
		  - No puedes navegar
		  - Muy manual para encontrar lo que te interesa (expreciones regulares)

???

???


'''
'''
Scraping: extraer datos
Scraping web: Existen varios sistemas para scrapear una web nos sentraremos en solo tres.
				. Recuests -> 	+ Muy rapido
								+ Sensillo de implementar
								- No puede saltarse los captcha y ni los paywall
								- Tampoco puedes navegar
								- La busqueda es manual requiere el uso de expreciones regulares
				. Beautiful Soup ->	+ Extremadamente rapido
									+ Sencillo de implementar
									+ Facilidad para filtrar y encontrar elementos, atributos, etc
									- No puede saltarse los paywall ni los captchas
									- No se puede navegar, pero si seguir el flujo de las URLs que se encuentres en el html
				. ??? 

Siempre cuando se realiza una peticion (requests) se envia el Agente de Usuario (UserAgent)
Por ejemplo, usando la consola del navegador se puede saberlo escribiendo [navigator.usserAgent]:
	-> 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36'
Pero existe un metodo para disfrazar nuestro 'userAgent' agregando:
	-> headers = {
		"UserAgent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36'
	}
	# Agregando en la peticion este parametro [requests.get(url,headers=headers)]
 *Esto lo que hace es decir al ente propietario (mercadolibre) mediante que dispositivo me estoy conectando
El truco para evitar esto es modificando el valor del 'UserAgent', lo que hay que hacer es remplazarlo por el UserAgent de google:
Para esto accede a googlebot(rastreadores habituales) copia un agente bot de google:
	-> headers = {
		"UserAgent":'Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; Googlebot/2.1; +http://www.google.com/bot.html) Chrome/135.0.0.0 Safari/537.36'
	}
 *Modificar los valores 'W.X.Y.Z' que vienen por defecto

TENER CUIDADO!!!
Si al momento de hacer esto (entrar a una pagina web con el agente de googlebot) y usar nuestra IP puede que nos restringan el acceso a esa web
Ahora bien, si haces SCRAPING y/o usas este truco siempre usar un VPN (por ejemplo warp u otras)
El proxi es la unica alternativa para la navegacion segura.

'''
# pip3 install requests -> Instalar la dependencia para hacer peticiones 

import requests
import re
url = "https://articulo.mercadolibre.com.ar/MLA-1699359868-calzado-para-hombre-nike-downshifter-12-negro-_JM#polycard_client=homes-korribanSearchPromotions&searchVariation=182038058423&position=35&search_layout=grid&type=item&tracking_id=66430078-69cd-47e7-b4c6-4e6f9c5b5985&c_id=/home/promotions-recommendations/element&c_uid=a423b39b-34c9-4c08-bf4f-9277010d825a"

response = requests.get(url)

print(response.status_code)
if response.status_code == 200:
	print('Peticion exitosa :)')
	html = response.text

price = r'<span class="andes-money-amount__fraction" aria-hidden="true">(.*?)</span>'
match = re.search(price, html)
if match:
	print(f"El precio del producto es: {match.group(1)}")

titule= r'<title>(.*?)</title>'
match = re.search(titule,html)
if match:
	print(f"El titulo es: {match.group(1)}")