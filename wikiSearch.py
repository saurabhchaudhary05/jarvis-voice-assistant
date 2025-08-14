import wikipedia
import webbrowser
from speakModule import speak

def search_wikipedia(query, detailed=False, language='en', translate_to=None):
    try:
        wikipedia.set_lang(language)
        speak(f"Searching Wikipedia for {query}...")

        if detailed:
            result = wikipedia.page(query)
            summary = result.content[:1000]  # Limit for safety
            speak(summary)
            webbrowser.open(result.url)
        else:
            summary = wikipedia.summary(query, sentences=2)

            if translate_to:
                speak("Translation service is not available. Here's the summary in English:")
            speak(summary)

    except wikipedia.exceptions.DisambiguationError as e:
        speak("The topic is ambiguous, please be more specific.")
    except wikipedia.exceptions.PageError:
        speak("Sorry, I couldn't find any information on that.")
    except Exception as e:
        speak(f"An error occurred: {e}")
