import speech_recognition as sr
import webbrowser
from wikiSearch import search_wikipedia
from notesManager import add_note, get_notes, clear_notes
from jokesModule import tell_joke
from datetimeModule import tell_time_and_date
from movieModule import get_movie_info
import pyttsx3
import musicLibrary
import requests
from openai import OpenAI
from currencyModule import get_exchange_rate
from weatherModule import get_weather
from gtts import gTTS
import pygame
import os
from dotenv import load_dotenv
import time
from applauncher import ( open_excel, open_word, open_powerpoint, open_vscode, open_whatsapp,
    open_chrome, open_notepad, open_spotify,
    shutdown, restart, lock, sleep
)
from speakModule import speak

# Load environment variables
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
NEWS_API_KEY = os.getenv("NEWS_API_KEY")



# OpenAI response
def aiProcess(command):
    client = OpenAI(api_key=OPENAI_API_KEY)
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are Jarvis, a helpful and concise assistant."},
            {"role": "user", "content": command}
        ]
    )
    return response.choices[0].message.content



# News
def get_news():
    try:
        url = f"https://newsapi.org/v2/top-headlines?country=in&apiKey={NEWS_API_KEY}"
        data = requests.get(url).json()
        articles = data.get("articles", [])
        for article in articles[:5]:
            speak(article['title'])
    except:
        speak("Error fetching news.")

# Process commands
def processCommand(command):
    command = command.lower().strip()

    if "open google" in command:
        webbrowser.open("https://www.google.com")
        speak("Opening Google.")

    elif "open youtube" in command:
        webbrowser.open("https://www.youtube.com")
        speak("Opening YouTube.")

    elif "open facebook" in command:
        webbrowser.open("https://www.facebook.com")
        speak("Opening Facebook.")

    elif "open linkedin" in command:
        webbrowser.open("https://www.linkedin.com")
        speak("Opening LinkedIn.")

    elif command.startswith("play"):
        song = command.replace("play", "").strip()
        if song in musicLibrary.music:
            webbrowser.open(musicLibrary.music[song])
            speak(f"Playing {song}")
        else:
            speak(f"Sorry, I couldn't find the song {song}")

    elif "news" in command:
        speak("Here are the latest headlines.")
        get_news()

    elif "weather in" in command:
        city = command.split("weather in")[-1].strip()
        get_weather(city)

    elif "joke" in command:
        tell_joke()

    elif "time" in command or "date" in command:
        tell_time_and_date() 

    elif "movie" in command or "film" in command:
        title = command.replace("tell me about the movie", "").replace("movie", "").replace("film", "").strip()
        get_movie_info(title)

    elif "exchange rate" in command or "convert" in command:
        try:
            words = command.lower().split()
            amount = 1
            base = "usd"
            target = "inr"

            for i, word in enumerate(words):
                if word.replace(".", "").isdigit():
                    amount = float(word)
                    base = words[i+1].upper() if i+1 < len(words) else base
                    target = words[i+3].upper() if "to" in words[i+2:i+4] else target
                    break
            get_exchange_rate(base, target, amount)
        except:
            speak("Sorry, I couldn't understand the currencies.")


    elif "open" in command or "computer" in command or "system" in command:
        if "excel" in command:
            open_excel()
        elif "word" in command:
            open_word()
        elif "powerpoint" in command:
            open_powerpoint()
        elif "code" in command or "vs code" in command:
            open_vscode()
        elif "whatsapp" in command:
            open_whatsapp()
        elif "chrome" in command:
            open_chrome()
        elif "notepad" in command:
            open_notepad()
        elif "spotify" in command:
            open_spotify()
        elif "shutdown" in command:
            shutdown()
        elif "restart" in command:
            restart()
        elif "lock" in command:
            lock()
        elif "sleep" in command:
            sleep()
        else:
            speak("I couldn't find that application.")

    elif "remember that" in command:
        note = command.split("remember that")[-1].strip()
        if note:
            add_note(note)
            speak("Okay, I will remember that.")
        else:
            speak("What would you like me to remember?")

    elif "what did i ask you to remember" in command or "recall notes" in command:
        notes = get_notes()
        if notes:
            speak("Here are your notes:")
            for note in notes:
                speak(note)
        else:
            speak("You haven't asked me to remember anything yet.")

    elif "forget everything" in command or "clear my notes" in command:
        clear_notes()
        speak("All your notes have been cleared.")

    elif "who is" in command or "tell me about" in command:
        topic = command.replace("who is", "").replace("tell me about", "").strip()
        detailed = "in detail" in command
        translate_to = "hi" if "in hindi" in command else None
        search_wikipedia(topic, detailed=detailed, translate_to=translate_to)

    else:
        reply = aiProcess(command)
        speak(reply)



# Main listening loop
def listen_for_wake_word():
    recognizer = sr.Recognizer()
    mic = sr.Microphone()

    while True:
        try:
            with mic as source:
                recognizer.adjust_for_ambient_noise(source, duration=0.5)
                print("Listening for wake word...")
                audio = recognizer.listen(source, timeout=3, phrase_time_limit=3)
                trigger = recognizer.recognize_google(audio).lower()

                if "jarvis" in trigger:
                    speak("Yes?")
                    print("Listening for command...")
                    audio = recognizer.listen(source, timeout=5, phrase_time_limit=6)
                    command = recognizer.recognize_google(audio)
                    print(f"Command recognized: {command}")
                    if "stop" in command or "exit" in command or "bye" in command:
                        speak("Goodbye! Shutting down.")
                        print("Jarvis stopped by user command.")
                        break  # Exit the while loop and stop the assistant
                    processCommand(command)

        except sr.WaitTimeoutError:
            continue
        except sr.UnknownValueError:
            continue
        except Exception as e:
            print(f"Error: {e}")




# Entry point
if __name__ == "__main__":
    speak("Initializing Jarvis.")
    listen_for_wake_word()
