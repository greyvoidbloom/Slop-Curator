from moviepy.video.io.VideoFileClip import VideoFileClip
from moviepy.audio.io.AudioFileClip import AudioFileClip
from moviepy.video.compositing.CompositeVideoClip import CompositeVideoClip
from moviepy.video.VideoClip import TextClip
from moviepy import concatenate_videoclips
import os
import random
import json

class VDGEngine:
    def __init__(self,bg_dir="background_videos",audio_in_dir="generated_audio",story_dir="cleaned_stories",output_dir="generated_videos"):
        self.backgroundvid_dir = bg_dir
        self.audio_input_dir = audio_in_dir
        self.story_dir = story_dir
        self.output_dir = output_dir
        print(f"\033[33m[SLOP CURATOR::VIDEO ENGINE]\033[37m Video Generation Engine is ready ...")
    def choose_background(self):
        vid_bg = [f for f in os.listdir(self.backgroundvid_dir) if os.path.isfile(os.path.join(self.backgroundvid_dir, f))]
        if not vid_bg:
            return None
        return random.choice(vid_bg)

    def synthesize_video(self):
        
        for sub in os.listdir(self.story_dir):
            sub_path = os.path.join(self.story_dir,sub)
            if not os.path.isdir(sub_path):
                continue
            print(f"\033[33m[SLOP CURATOR::VIDEO ENGINE]\033[37m Processing the {sub} subreddit..")
            output_path = os.path.join(self.output_dir,sub)
            os.makedirs(output_path,exist_ok=True)

            for story in os.listdir(sub_path):
                #print(story.split("_cleaned.json")[0])
                audio_path = os.path.join(self.audio_input_dir,sub,f"{story.split("_cleaned.json")[0]}.mp3")
                story_path = os.path.join(sub_path,story)
                output_path =  os.path.join(self.output_dir,sub,f"{story.split("_cleaned.json")[0]}.mp4")
                bg_clip = os.path.join(self.backgroundvid_dir,self.choose_background())
                print(f"\033[32m[SLOP CURATOR::VIDEO ENGINE]\033[37m Using the \033[36m{bg_clip}\033[37m background..")
                clip = VideoFileClip(bg_clip)
                audio = AudioFileClip(audio_path)
                if clip.duration < audio.duration:
                    loops = int(audio.duration // clip.duration) + 1
                    clip = concatenate_videoclips([clip] * loops)
                clip = clip.subclipped(0, audio.duration)
                clip = clip.resized(height=1920)
                x_center = clip.w / 2
                clip = clip.cropped(x_center=x_center, width=1080)
                clip = clip.with_audio(audio)
                with open(story_path, "r", encoding="utf-8") as f:
                    story = json.load(f)
                text = story["rewritten_text"]
                words = text.split()
                chunks = [' '.join(words[i*7:(i+1)*7]) for i in range((len(words)+6)//7)]
                duration_per_chunk = audio.duration / len(chunks)
                subtitle_clips = []
                for i, chunk in enumerate(chunks):
                    start = i * duration_per_chunk
                    end = start + duration_per_chunk

                    txt_clip = TextClip(
                        text=chunk,
                        font_size=90,
                        font="/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",          # Make sure this font is installed
                        color="white",
                        stroke_color="black",
                        stroke_width=5,
                        method="caption",
                        size=(1080, None),
                        text_align="center",
                        horizontal_align="center",
                        vertical_align="center",
                        duration=duration_per_chunk
                    ).with_position(("center", "center")).with_start(start).with_end(end)

                    subtitle_clips.append(txt_clip)

                # Combine video + subtitles
                final_clip = CompositeVideoClip([clip, *subtitle_clips])
                final_clip.write_videofile(output_path, fps=30)


                print(f"{story_path} and {audio_path}")



if __name__ == "__main__":
    vdg = VDGEngine()
    vdg.synthesize_video()
