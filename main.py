from utils import *
security = CredentialsManager(config_path="config.json")
redbot = RedditBot(client_id=security.red_client_id,
                    client_secret=security.red_client_secret,
                    bot_string=security.user_agent)
scup = StoryCleaner(openai_Key=security.openai_key)
print(f"\033[32m[SLOP CURATOR]\033[37m Welcome {security.owner}. You're good to go, \033[31m FEED THE PIGGIES!!!\033[37m")
subs = ["TrueOffMyChest", "AmItheAsshole","TIFU"]
folders=["rawjson","cleaned_stories"]
redbot.generateN(subs=subs,topN=5)
scup.storyCleanup()
#cleanUp(folders=folders)
