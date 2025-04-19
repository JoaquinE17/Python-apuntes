#SCRAPING
'''
Esta es una de las dependencias mas utilizadas para hacer scraping en python.
Pero requiere que importemos 'requests', por que no realiza peticiones, solo recibe y trabaja con el 'html' que recupera esta dependencia

'''
# pip3 install bs4 -> Para instalar la dependencia i poder utilizar beautiful

from bs4 import BeautifulSoup
import requests

url = "https://articulo.mercadolibre.com.ar/MLA-1699359868-calzado-para-hombre-nike-downshifter-12-negro-_JM#polycard_client=homes-korribanSearchPromotions&searchVariation=182038058423&position=35&search_layout=grid&type=item&tracking_id=66430078-69cd-47e7-b4c6-4e6f9c5b5985&c_id=/home/promotions-recommendations/element&c_uid=a423b39b-34c9-4c08-bf4f-9277010d825a"
response = requests.get(url)
if response.status_code == 200:
	print("Peticion exitosa :)")
	soup = BeautifulSoup(response.text, 'html.parser') # [html.parser] anliza el archivo html y lo convierte en un formato manejable 

#print(soup.prettify())
titule = soup.title # El title busca el titulo o la etiqueta <title> dentro del html. Forma parte de su estructura(beautiful soup)
if titule:
	print(f'\nEl titulo de la wb es: {titule.string}') # El [.string] ó [.text] son atributos para recuperar el texto dentro de la sintaxis

metas = soup.title.parent.find_all('meta', content="product") # El parent se utiliza para acceder al elemento padre y desde alli buscar
print('\nLos metas de la wb son:',metas,'...')

# Buscar price usando BSoup

price_span = soup.find('span', class_="andes-money-amount__fraction") #El primer elemento ('span') se puede obviar, pero este ayuda a acelerar el proceso de busqueda
print('\nPrecio del producto:',price_span.text,'\n')

# Busca todos los precios

allprice = soup.find_all('span',"andes-money-amount__fraction")
for price in allprice:
	print(f"El precio del producto es: {price.text}")

# Buscar todos los productos y obtener el nombre y el precio
products = soup.find_all(class_="ui-vpp-highlighted-specs__key-value__labels")
print('\nCaracteristicas del producto:')
for product in products:	
	name = product.find(class_="ui-pdp-color--BLACK ui-pdp-size--XSMALL ui-pdp-family--REGULAR")
	price = product.find(class_="ui-pdp-color--BLACK ui-pdp-size--XSMALL ui-pdp-family--SEMIBOLD")
	print(f'{name.string} {price.string}')
   