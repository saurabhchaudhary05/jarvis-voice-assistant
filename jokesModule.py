import requests
from speakModule import speak  # if speak() is also modularized

def tell_joke():
    headers = {
        "Accept": "application/json",
        "User-Agent": "Jarvis Voice Assistant"
    }

    try:
        response = requests.get("https://icanhazdadjoke.com/", headers=headers)
        if response.status_code == 200:
            joke_data = response.json()
            joke = joke_data.get("joke", "Sorry, I couldn't fetch a joke right now.")
            speak(joke)
        else:
            speak("Sorry, I'm unable to get a joke from the server.")
    except Exception as e:
        speak("Something went wrong while getting a joke.")
        print(f"Joke API error: {e}")
