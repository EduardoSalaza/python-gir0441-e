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

#print("URL: " + (url))

while True:
    orig = input("Starting Location: ")
    if orig == "quit" or orig == "q":
        break
    dest = input("Destination: ")
    if dest == "quit" or dest == "q":
        break
    url  = main_api + urllib.parse.urlencode({"key":key, "from":orig, "to":dest})

#Request status if the statuscode key is set to value 0  
    json_data = requests.get(url).json()
    json_status = json_data["info"]["statuscode"]

    if json_status == 0:
        print("API Status: " + str(json_status) + " = A successful route call.\n") 
        print("Directions from " + (orig) + " to " + (dest))
        print("Trip Duration:   " + str(json_data["route"]["formattedTime"]))
        print("Miles:           " + str(json_data["route"]["distance"]))
        print("Fuel(Gal):       " + str(json_data["route"]["fuelUsed"])) 
        print("Kilometers:      " + str("{:.2f}".format((json_data["route"]["distance"])*1.61)))
        print("Fuel Used (Ltr): " + str("{:.2f}".format((json_data["route"]["fuelUsed"])*3.78)))      
        print("=============================================")
        for each in json_data["route"]["legs"][0]["maneuvers"]:
            print((each["narrative"]) + " (" + str("{:.2f}".format((each["distance"])*1.61) + " km)"))
        print("=============================================\n")