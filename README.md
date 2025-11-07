# Slop Curator  🐷🐷
**Slop Curator** is an automated Reddit to YouTube pipeline that scrapes popular Reddit stories, cleans them for narration, and prepares them for voice-over and video production. 
---

## Features

* **Reddit Scraper:** Automatically fetches top posts from subreddits like `AskReddit`, `TIFU`, `AmItheAsshole`, and `TrueOffMyChest`.
* **Story Cleaner:** Rewrites stories using OpenAI to be engaging, conversational, and safe for narration. Removes usernames, explicit content, and Reddit references.
* **Voice Generation:** Converts cleaned stories into audio narration, speedup available( defaults to 1.5 ).
* **Video Generation:** Generates slop-style videos and adds subtitles before stitching with audio. ( Have a folder called "background_videos" ready with background clips ready, could be of any length as it loops around if len(audio) > len(video) ) {preferably around 2}
* **Credential Manager:** Handles sensitive API keys for Reddit and OpenAI securely.


---

## Project Structure

```
Slop-Curator/
├── config.json                   # Auto generated the config(credential) file
├── main.py                       # Consolidation of everything
├── background_videos/            # *keep ur background videos here*
├── README.md                     # Documentation
├── requirements.txt              # do pip install -r rerequirements.txt
└── utils
    ├── cleanup.py                # Waste directory/file cleaner
    ├── credentialsmanager.py     # Creates/Reads the saved configs
    ├── __init__.py               # Just so its a nice module
    ├── redditstorygenerator.py   # Scrapes reddits for stories
    ├── audiogen.py               # Generates audio with edge-TTS
    ├── videogen.py               # video gen + subs + stitching 
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

6. make a directory with the name "**generated_videos**" and then put as many background clips as you want in them. The program randomly picks one out of all the present ones.
---

## Usage
#### To ensure everything works  nicely,
```bash
./sloprunner.sh
```
or
```bash
python3 main.py
```
Incase you want to run it as a cron job:
```bash
sudo pacman -S cronie
sudo systemctl enable --now cronie.service
#optional 
systemctl status cronie.service 
```
Then you do
```bash
crontab -e 
```
then you make a command like:
```bash
<min> <hour> * * * systemd-inhibit --why="runnin da slop" --mode=block /path/to/sloprunner.sh >> /path/to/sloplog.log 2>&1
```
**Example (cron at 9pm each day) :**
```bash
0 21 * * * systemd-inhibit --why="Running Slop Curator" --mode=block /home/grey/Desktop/ytauto/sloprunner.sh >> /home/grey/Desktop/ytauto/sloplog.log 2>&1
```
Incase you need to check it out yourself..
### Scrape Reddit Stories

```bash
python3 utils/redditstorygenerator.py
```

Stories are saved in the `rawjson/` folder.

### Clean Stories

```bash
python3 utils/storycleaner.py
```
Cleaned stories are saved in `cleaned_stories/<subreddit>/`.

### Generate Audio

```bash
python3 utils/audiogen.py
```
Cleaned audio files are saved in `generated_audio/<subreddit>/`.
### Generate Video

```bash
python3 utils/videogen.py
```
Cleaned audio files are saved in `generated_videos/<subreddit>/`.


## Roadmap

1. **Voice Narration:** Convert cleaned stories into audio using TTS (OpenAI or gTTS). [DONE]
2. **Video Generation:** Overlay story text on images or clips for YouTube Shorts. [DONE]
3. **Automated Upload:** Schedule uploads directly to YouTube. [IDK IF IMMA DO THIS]
4. **Enhanced UI:** Add keyboard shortcuts, progress bars, and story search. [NOT DONE]
5. **Analytics:** Track which stories perform best. [NOT DONE]

---

## Contributing

Pull requests and suggestions are welcome! If you make improvements to TTS, video generation, or UI, feel free to contribute back.

---

