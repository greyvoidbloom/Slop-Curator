from utils import *
import datetime
if __name__ == "__main__":
    security = CredentialsManager(config_path="config.json")
    redbot = RedditBot(client_id=security.red_client_id,
                        client_secret=security.red_client_secret,
                        bot_string=security.user_agent)
    scup = StoryCleaner(openai_Key=security.openai_key)
    tts = TTSEngine(speed_factor=1.5)
    vdg = VDGEngine()


    print(f"\033[32m[SLOP CURATOR]\033[37m Welcome {security.owner}. You're good to go, \033[31m FEED THE PIGGIES!!!\033[37m")


    subs = ["TrueOffMyChest", "AmItheAsshole","TIFU"]
    folders = ["rawjson","cleaned_stories","generated_audio","generated_videos"]

    cleanUp(folders=folders)
    redbot.generateN(subs=subs,topN=5)
    scup.storyCleanup()
    tts.singToMe()
    vdg.synthesize_video()
    print(f"\033[32m[SLOP CURATOR]\033[37m My work is done Boss, finished at {datetime.datetime.now()}..")

