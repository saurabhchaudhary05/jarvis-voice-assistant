# weatherModule.py

import requests
from gtts import gTTS
import pygame
import os
import time
from dotenv import load_dotenv
from speakModule import speak

load_dotenv()
WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")



def get_weather(city):
    try:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API_KEY}&units=metric"
        data = requests.get(url).json()
        if data.get("cod") != "404":
            temp = data["main"]["temp"]
            desc = data["weather"][0]["description"]
            report = f"The current temperature in {city} is {temp}°C with {desc}."
            print(report)
            speak(report)
        else:
            speak("City not found.")
    except:
        speak("Error fetching weather.")
