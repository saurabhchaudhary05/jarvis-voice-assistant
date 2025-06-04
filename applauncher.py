# appLauncher.py
import os
import subprocess
import platform
from speakModule import speak

def open_excel():
    speak("Opening Excel.")
    os.system("start excel")

def open_word():
    speak("Opening Word.")
    os.system("start winword")

def open_powerpoint():
    speak("Opening PowerPoint.")
    os.system("start powerpnt")

def open_vscode():
    speak("Opening Visual Studio Code.")
    os.system("code")  # Make sure 'code' is in PATH

def open_whatsapp():
    speak("Opening WhatsApp.")
    whatsapp_path = os.path.expandvars(r"%LOCALAPPDATA%\WhatsApp\WhatsApp.exe")
    os.system(f'start "" "{whatsapp_path}"')

def open_chrome():
    speak("Opening Google Chrome.")
    os.system("start chrome")

def open_notepad():
    speak("Opening Notepad.")
    os.system("start notepad")

def open_spotify():
    speak("Opening Spotify.")
    spotify_path = os.path.expandvars(r"%APPDATA%\Spotify\Spotify.exe")
    os.system(f'start "" "{spotify_path}"')

# ---------------- SYSTEM COMMANDS ----------------
def shutdown():
    speak("Shutting down the system.")
    os.system("shutdown /s /t 1")

def restart():
    speak("Restarting the system.")
    os.system("shutdown /r /t 1")

def lock():
    speak("Locking the system.")
    os.system("rundll32.exe user32.dll,LockWorkStation")

def sleep():
    speak("Putting system to sleep.")
    os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
