import json

import requests

import pyttsx3



city =input("enter the name of the city:")
url = f"https://api.weatherapi.com/v1/current.json?key=a9ba5ee215cf4bd1bb3152948232807&q={city}"


r = requests.get(url)
print(r.text)

# print(type(r.text))
wdic = json.loads(r.text)
w= wdic["current"]["temp_c"]

engine = pyttsx3.init()

engine.say(f"the current weather of the {city} is {w} degrees")

engine.runAndWait()

