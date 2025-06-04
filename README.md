

```markdown
# 🤖 Jarvis - Your Personal Python Voice Assistant

A fully functional voice assistant built with Python, inspired by Iron Man's Jarvis. This assistant listens, responds, performs system-level tasks, and integrates APIs for dynamic info.

---

## ✨ Features

- 🎙️ Wake word: "Jarvis"
- 🌐 Open websites (Google, YouTube, Facebook, LinkedIn, etc.)
- 🎵 Play music from a predefined library
- 📚 Wikipedia search (with translation support)
- 🧠 AI Q&A with OpenAI (GPT)
- 🌤️ Live Weather updates using OpenWeather API
- 🗞️ Latest News using NewsAPI
- 🗒️ Note-taking (add, recall, clear notes)
- 😂 Jokes on command using Joke API
- 🕒 Tells time and date
- 🧠 Remembers things you say
- 💻 Opens apps like VS Code, WhatsApp, Excel, etc.
- 🔐 System commands: shutdown, restart, lock, sleep
- 🎬 Get movie info using OMDB API

---

## 🛠 Tech Stack

- **Python**
- `speech_recognition`, `gTTS`, `pygame`
- `openai`, `requests`, `dotenv`, `wikipedia`
- APIs: OpenWeather, NewsAPI, OMDB, Joke API
- System commands via `os`

---

## 📁 Project Structure

```

project/
│
├── main.py                  # Entry point
├── musicLibrary.py          # Song URL map
├── .env                     # API keys (not pushed to GitHub)
├── requirements.txt
├── modules/
│   ├── wikiSearch.py
│   ├── datetimeModule.py
│   ├── notesManager.py
│   ├── jokesModule.py
│   └── applauncher.py

````

---

## 🚀 Getting Started

### 🔧 Installation

```bash
git clone https://github.com/yourusername/jarvis-voice-assistant.git
cd jarvis-voice-assistant
pip install -r requirements.txt
````

### 🔐 Setup

Create a `.env` file with:

```env
OPENAI_API_KEY=your_key_here
WEATHER_API_KEY=your_key_here
NEWS_API_KEY=your_key_here
OMDB_API_KEY=your_key_here
```

---

## 🗣️ Usage

Run `main.py` and say "Jarvis" to activate. Give commands like:

* `"What's the weather in Delhi?"`
* `"Tell me a joke"`
* `"Open YouTube"`
* `"Remember that I have a meeting at 3PM"`
* `"What did I ask you to remember?"`
* `"Shutdown the system"`
* `"Tell me about Elon Musk"`

---



## 🙌 Acknowledgements

* [OpenAI](https://openai.com/)
* [NewsAPI](https://newsapi.org/)
* [OpenWeather](https://openweathermap.org/)
* [OMDb API](https://www.omdbapi.com/)

---

