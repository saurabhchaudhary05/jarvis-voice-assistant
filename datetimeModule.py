# datetimeModule.py
from datetime import datetime
from speakModule import speak  # Import your speak function

def tell_time_and_date():
    now = datetime.now()
    current_time = now.strftime("%I:%M %p")  # e.g., 04:30 PM
    current_date = now.strftime("%A, %d %B %Y")  # e.g., Tuesday, 03 June 2025

    response = f"Today is {current_date} and the current time is {current_time}."
    speak(response)
