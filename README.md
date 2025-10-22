# Slop Curator  🐷🐷
**Slop Curator** is an automated Reddit to YouTube pipeline that scrapes popular Reddit stories, cleans them for narration, and prepares them for voice-over and video production. 
---

## Features

* **Reddit Scraper:** Automatically fetches top posts from subreddits like `AskReddit`, `TIFU`, `AmItheAsshole`, and `TrueOffMyChest`.
* **Story Cleaner:** Rewrites stories using OpenAI to be engaging, conversational, and safe for narration. Removes usernames, explicit content, and Reddit references.
* **Voice Generation (Coming Soon):** Converts cleaned stories into audio narration.
* **Video Generation (Coming Soon):** Generates slop-style videos and adds subtitles before stitvhing with audio
* **Credential Manager:** Handles sensitive API keys for Reddit and OpenAI securely.


---

## Project Structure

```
Slop-Curator/
├── config.json                   # Auto generated the config(credential) file
├── main.py                       # Consolidation of everything
├── README.md                     # Documentation
├── requirements.txt              # do pip install -r rerequirements.txt
└── utils
    ├── cleanup.py                # Waste directory/file cleaner
    ├── credentialsmanager.py     # Creates/Reads the saved configs
    ├── __init__.py               # Just so its a nice module
    ├── redditstorygenerator.py   # Scrapes reddits for stories
    └── storycleaner.py           # Ai cleaner for raw reddit text
```

---

## Installation

1. Clone the repo:

```bash
git clone https://github.com/greyvoidbloom/Slop-Curator.git
cd Slop-Curator
```

2. Create and activate a virtual environment:

```bash
python3 -m venv env
source env/bin/activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Set up your **credentials**:

   * Reddit API (create an app on [Reddit Developer Portal](https://www.reddit.com/prefs/apps))
   * OpenAI API [key](https://platform.openai.com/api-keys)

5. Add your credentials securely using the **Credential Manager** or environment variables.

---

## Usage
#### To ensure everything works  nicely,

```bash
python3 main.py
```
everything has been synced nicely. 

Incase you need to check it out yourself..
### Scrape Reddit Stories

```bash
python3 src/redditstorygenerator.py
```
or 
```bash
python3 main.py  # works the same.
```
Stories are saved in the `rawjson/` folder.

### Clean Stories

```bash
python3 src/storycleaner.py
```
or 
```bash
python3 main.py  # works the same.
```

Cleaned stories are saved in `cleaned_stories/<subreddit>/`.


## Roadmap

1. **Voice Narration:** Convert cleaned stories into audio using TTS (OpenAI or gTTS).
2. **Video Generation:** Overlay story text on images or clips for YouTube Shorts.
3. **Automated Upload:** Schedule uploads directly to YouTube.
4. **Enhanced UI:** Add keyboard shortcuts, progress bars, and story search.
5. **Analytics:** Track which stories perform best.

---

## Contributing

Pull requests and suggestions are welcome! If you make improvements to TTS, video generation, or UI, feel free to contribute back.

---

