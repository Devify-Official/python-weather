import json
import requests
import os

with open('config.json', 'r') as f:
    config = json.load(f)

API_KEY = config['api_key']

print("  _   _  U _____ u  _       _       U  ___ u ")
print(""" |'| |'| \| ___"|/ |"|     |"|       \/"_ \/""")
print("""/| |_| |\ |  _|" U | | u U | | u     | | | |""") 
print("U|  _  |u | |___  \| |/__ \| |/__.-,_| |_| |")
print(" |_| |_|  |_____|  |_____| |_____|\_)-\___/")  
print(" //   \\  <<   >>  //  \\  //  \\      \\")    
print("""(_") ("_)(__) (__)(_")("_)(_")("_)    (__)""")   
print("")
print("1. Search weather \n")

option1 = int(input('which option do you choose? \n> '))

if option1 == 1:
    os.system('cls')
    city = input('which city do you want to search? \n> ')
    url = f"https://api.weatherapi.com/v1/current.json?key={API_KEY}&q={city}/current.json"

    response = requests.request("GET", url)
    respjson = response.json()

    ville = respjson['location']['name']
    region = respjson['location']['region']
    country = respjson['location']['country']
    temperature = respjson['current']['temp_c']
    vvent = respjson['current']['wind_kph']

    print(f'Ville : {ville}, {region}, {country} \nTemperature : {temperature} Celcius \nVitesse du vent : {vvent} km/h')
