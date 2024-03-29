'''
 Autor: jesus eduardo salazar
        Fecha: 6-ene-23
'''
#Importación de modulos existentes

import urllib.parse
import requests

#Declaración de variables
main_api = "https://www.mapquestapi.com/directions/v2/route?"
orig = "Dolores Hidalgo"
dest = "México"
key  = "RviDNX6lvy58NDKYBhxHATAC6kjDZ4Z9"
url  = main_api + urllib.parse.urlencode({"key":key, "from":orig, "to":dest})

print("URL: " + (url))

#Request status if the statuscode key is set to value 0
json_data = requests.get(url).json()
json_status = json_data["info"]["statuscode"]
print (json_data)

if json_status == 0:
    print("API Status: " + str(json_status) + " = A successful route call.\n")