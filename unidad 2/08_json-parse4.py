'''
 Autor: jesus eduardo salazar
        Fecha: 6-ene-23
'''
#Importación de modulos existentes

import urllib.parse
import requests

#Declaración de variables
main_api = "https://www.mapquestapi.com/directions/v2/route?"
orig = ""
dest = ""
key  = "RviDNX6lvy58NDKYBhxHATAC6kjDZ4Z9"
url  = main_api + urllib.parse.urlencode({"key":key, "from":orig, "to":dest})

print("URL: " + (url))

#Declaración de una variable que obtenga información de jason rquest por medio de una URL
json_data = requests.get(url).json()
json_status = json_data["info"]["statuscode"]

if json_status == 0:
    print("API Status: " + str(json_status) + " = A successful route call.\n")

while True:
    orig = input("Starting Location: ")
    if orig == "quit" or orig == "q":
        break
    dest = input("Destination: ")
    if dest == "quit" or dest == "q":
        break