import asyncio
import edge_tts
import os
import json
from pydub import AudioSegment

class TTSEngine:
    def __init__(self, voice="en-US-AdamMultilingualNeural", speed_factor=1.5):
        self.voice = voice
        self.speed_factor = speed_factor
        print(f"\033[33m[SLOP CURATOR::TTS ENGINE]\033[37m TTS Engine is ready with voice \033[36m{voice}\033[37m and speed {speed_factor}x")

    async def asyncspeak(self, text, path):
        os.makedirs(os.path.dirname(path), exist_ok=True)
        communication = edge_tts.Communicate(text, self.voice)
        await communication.save(path)
        print(f"\033[32m[SLOP CURATOR::TTS ENGINE]\033[37m Saved audio: \033[36m{path}\033[37m")
        self.speed_up_audio(path)

    def speak(self, text, path):
        asyncio.run(self.asyncspeak(text=text, path=path))

    def speed_up_audio(self, path):
        try:
            audio = AudioSegment.from_file(path)
            faster_audio = audio._spawn(audio.raw_data, overrides={
                "frame_rate": int(audio.frame_rate * self.speed_factor)
            }).set_frame_rate(audio.frame_rate)
            faster_audio.export(path, format="mp3")
            print(f"\033[34m[SLOP CURATOR::TTS ENGINE]\033[37m Sped up {os.path.basename(path)} by {self.speed_factor}x")
        except Exception as e:
            print(f"\033[31m[SLOP CURATOR::TTS]\033[37m Failed to speed up {path}: {e}")

    def singToMe(self, input_dir="cleaned_stories", output_dir="generated_audio"):
        print(f"\033[33m[SLOP CURATOR::TTS ENGINE]\033[37m Looking for stories in {input_dir}..")
        for sub in os.listdir(input_dir):
            sub_path = os.path.join(input_dir, sub)
            if not os.path.isdir(sub_path):
                continue
            print(f"\033[33m[SLOP CURATOR::TTS ENGINE]\033[37m Processing the {sub} subreddit..")
            output_path = os.path.join(output_dir, sub)
            os.makedirs(output_path, exist_ok=True)

            for story in os.listdir(sub_path):
                if not story.endswith("_cleaned.json"):
                    continue
                story_path = os.path.join(sub_path, story)
                try:
                    with open(story_path, "r", encoding="utf-8") as f:
                        data = json.load(f)
                        text = data["rewritten_text"]
                        story_id = data["id"]

                        if not text:
                            print(f"\033[31m[SLOP CURATOR::TTS]\033[37m Skipping {story} cause no rewritten text..")
                            continue
                        audio_path = os.path.join(output_path, f"{story_id}.mp3")
                        if os.path.exists(audio_path):
                            print(f"\033[31m[SLOP CURATOR::TTS]\033[37m Skipping {story_id} (already exists)")
                            continue
                        self.speak(text=text, path=audio_path)
                except Exception as e:
                    print(f"\033[31m[SLOP CURATOR::TTS]\033[37m Failed on {story} : {e}")

if __name__ == "__main__":
    tts = TTSEngine(speed_factor=1.5)
    tts.singToMe()
