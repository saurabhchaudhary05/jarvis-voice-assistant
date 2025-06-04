import json
import os

NOTES_FILE = "notes.json"

def load_notes():
    if not os.path.exists(NOTES_FILE):
        return []
    with open(NOTES_FILE, "r") as file:
        return json.load(file)

def save_notes(notes):
    with open(NOTES_FILE, "w") as file:
        json.dump(notes, file, indent=4)

def add_note(note):
    notes = load_notes()
    notes.append(note)
    save_notes(notes)

def get_notes():
    return load_notes()

def clear_notes():
    save_notes([])
