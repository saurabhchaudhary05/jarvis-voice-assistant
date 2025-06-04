import os
import requests
from dotenv import load_dotenv
from speakModule import speak  # if speak() is modularized, else define it here

load_dotenv()
OMDB_API_KEY = os.getenv("OMDB_API_KEY")

def get_movie_info(title):
    try:
        url = f"http://www.omdbapi.com/?t={title}&apikey={OMDB_API_KEY}"
        response = requests.get(url).json()

        if response.get("Response") == "True":
            name = response.get("Title", "N/A")
            year = response.get("Year", "N/A")
            rating = response.get("imdbRating", "N/A")
            plot = response.get("Plot", "N/A")

            result = f"{name} ({year}) has an IMDb rating of {rating}. Plot: {plot}"
            print(result)
            speak(result)
        else:
            speak("Movie not found.")
    except Exception as e:
        print(f"Error fetching movie info: {e}")
        speak("Something went wrong while fetching the movie info.")


