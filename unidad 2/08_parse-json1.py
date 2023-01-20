'''
 Autor: jesus eduardo salazar
        Fecha: 6-ene-23
'''

#Importación de modulos existentes

import urllib.parse
import requests

#Declaración de variables
main_api = "https://www.mapquestapi.com/directions/v2/route?"
orig = "Washington"
dest = "Baltimore"
key  = "RviDNX6lvy58NDKYBhxHATAC6kjDZ4Z9"
url  = main_api + urllib.parse.urlencode({"key":key, "from":orig, "to":dest})
print(url)

#Declaración de una variable que obtenga información de jason rquest por medio de una URL
json_data = requests.get(url).json()
print(json_data)