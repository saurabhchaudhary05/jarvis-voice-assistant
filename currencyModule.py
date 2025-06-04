# currencyModule.py

import requests
from speakModule import speak
import os
from dotenv import load_dotenv

load_dotenv()
EXCHANGE_API_KEY = os.getenv("EXCHANGE_API_KEY")

def get_exchange_rate(base="USD", target="INR", amount=1):
    try:
        url = f"https://v6.exchangerate-api.com/v6/{EXCHANGE_API_KEY}/pair/{base}/{target}/{amount}"
        response = requests.get(url)
        data = response.json()

        if data["result"] == "success":
            converted = data["conversion_result"]
            speak(f"{amount} {base} is equal to {converted:.2f} {target}")
            print(f"{amount} {base} = {converted:.2f} {target}")
        else:
            speak("Failed to fetch exchange rate.")
    except:
        speak("There was an error fetching currency conversion.")
