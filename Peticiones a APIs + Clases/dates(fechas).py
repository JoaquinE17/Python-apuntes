# REQUEST (peticiones) ------------------------------------------------------------------------------------------------------------------------->
# TRABAJANDO CON FECHAS Y HORAS EN PYTHON

# Primero debemos importar el modulo al que queremos hacer una peticion:
from datetime import datetime, timedelta
# En este caso importamos el modulo 'datetime', y de esta espesificamos que solo usaremos las librerias "datetime, timedelta"

# Obtener la fecha y hora actual con '.now()':
now = datetime.now()
print(f"Esta es la fecha y hora actual: {now}") # Esta es la fecha y hora actual: 2025-03-08 10:40:55.421927

# Crear una fecha y hora especifica:
specific_date = datetime(2025,2,21,14,3,0) # [YYYY,MM,DD,hh,mm,ss]
print(f"Fecha y hora especifica: {specific_date}") # Fecha y hora especifica: 2025-02-21 14:03:00

# Formatear fechas
# Utiliza el metodo 'strftime()', pasando como parametro el objeto DATETIME y el formato especificado
# Para saver los formatos visitar: https://docs.python.org/3/library/datetime.html#datetime.datetime.strftime
format_date = now.strftime("%d/%m/%y %Y:%H:%S 12%%")
print(f"Fecha formateada: {format_date}") # Fecha formateada: 08/03/25 2025:10:15 12%

# Formatear el ideoma por defecto
format_date = now.strftime("%A %B %Y %Y:%H:%S")
print(f"Fecha: {format_date}") # Fecha: Saturday March 2025 2025:11:22
# Para formatear el ideoma en el que devuelve por defecto se debe importar la libreria'locale'
import locale
# Espesificar la zona horaria que se va a utilizar para formatear
locale.setlocale(locale.LC_TIME, 'es_ES.utf-8')
format_date = now.strftime("%A %B %Y %Y:%H:%S")
print(f"Fecha: {format_date}") # Fecha: sÃ¡bado marzo 2025 2025:11:55

''' Regla - Reaal Academia Española (RAE) '''
##################################################################################
# Los nombres de 'dias','semanas','meses','estaciones' se escriben en minusculas #
##################################################################################

# Operaciones con fechas (sumar/restar semanas, dias, horas, minutos, minutos) -> values (int or float)
yesterday = datetime.now() - timedelta(days=1)
print(f"El dia de ayer: {yesterday}") # El dia de ayer: 2025-03-07 11:03:44.657824

# Obtener componentes individuales de una fecha:
year = now.year
month = now.month
print(f"El año es: {year} y el mes es: {month}") # El año es: 2025 y el mes es: 3

# Calcular la diferencia entre dos fechas
date1 = datetime.now()
date2 = datetime(2025,2,12,15,30,0)
difference = date2 - date1
print(f"La diferencia entre las fechas es: {difference}") # La diferencia entre las fechas es: -24 days, 4:13:21.490785
