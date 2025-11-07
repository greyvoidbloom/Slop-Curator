import os
import json
from openai import OpenAI, RateLimitError, APITimeoutError, APIConnectionError
import time
class StoryCleaner():
    def __init__(self, openai_Key):
        self.client = OpenAI(api_key=openai_Key, timeout=90.0) 
        print(f"\033[33m[SLOP CURATOR::STORY CLEANER]\033[37m Story Cleaner is active..")
    def textPrompt(self, text, style="reddit-drama"):
        prompt = f"""
        Rewrite the following Reddit story so it sounds natural and engaging when read aloud in a YouTube short.
        - Keep the narrative conversational and vivid.
        - Remove usernames, Reddit references, and explicit content.
        - Keep it concise but emotionally resonant.
        - Maintain the same story meaning and tone.
        Style: {style}
        Story:
        {text}
        """
        for attempt in range(3):
            try:
                response = self.client.chat.completions.create(
                    model="gpt-4o-mini",
                    messages=[{"role": "user", "content": prompt}]
                )
                return response.choices[0].message.content.strip()
            except (APITimeoutError, APIConnectionError) as e:
                print(f"\033[31m[SLOP CURATOR::STORY CLEANER]\033[37m Timeout/Connection error ({e}). Retrying in 15s... ({attempt+1}/3)")
                time.sleep(15)
        print("\033[31m[SLOP CURATOR::STORY CLEANER]\033[37m Failed after 3 attempts. Skipping story.")
        return text

    def storyCleanup(self):
        self.storyfile = [f for f in os.listdir("./rawjson/") if f.startswith("reddit_stories") and f.endswith(".json")]
        if not self.storyfile:
            print("\033[31m[SLOP CURATOR::STORY CLEANER]\033[37mNo reddit stories file found...\n \033[33mAborting Mission...\033[37m")
            exit()
        print(f"\033[32m[SLOP CURATOR::STORY CLEANER]\033[37m Found file(s) \033[36m{self.storyfile}..\033[37m")

        for filename in self.storyfile:
            print(f"\033[32m[SLOP CURATOR::STORY CLEANER]\033[37m Processing \033[36m{filename}\033[37m..")
            file_path = os.path.join("rawjson", filename)
            with open(file_path , "r", encoding="utf-8") as f:
                stories = json.load(f)
            for story in stories:
                while True:
                    try:
                        rewritten_story = self.textPrompt(story["text"])
                        break
                    except RateLimitError:
                        print("\033[31m[SLOP CURATOR::STORY CLEANER]\033[37m Rate limit exceeded, trying again in 30 seconds...")
                        time.sleep(30)
                story["rewritten_text"] = rewritten_story

                story.pop("text", None)
                os.makedirs(f'cleaned_stories/{story["subreddit"]}',exist_ok=True)
                outputFile = f"./cleaned_stories/{story["subreddit"]}/{story["id"]}_cleaned.json"
                with open(outputFile,"w",encoding="utf-8") as f:
                    json.dump(story,f,ensure_ascii=False, indent=2)
                print(f"\033[32m[SLOP CURATOR::STORY CLEANER]\033[37m Rewrote to \033[36m{outputFile}\033[37m..")

        
if __name__ == "__main__":
    scup = StoryCleaner(openai_Key="x-x-x-x")
    scup.storyCleanup()