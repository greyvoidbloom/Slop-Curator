import praw
import json
from datetime import datetime
import os

class RedditBot():
    def __init__(self,client_id,client_secret,bot_string):
        self.redditbot = praw.Reddit(
            client_id = client_id,
            client_secret = client_secret,
            user_agent = bot_string
        )
        print(f"\033[33m[SLOP CURATOR::REDDITBOT]\033[37m Reddit Bot is active..")

    def generateN(self,subs,topN):
        self.subreddits = subs
        self.stories = []

        for sub in self.subreddits:
            self.subreddit = self.redditbot.subreddit(sub)
            print(f"\033[32m[SLOP CURATOR::REDDITBOT]\033[37m Fetching top {topN} post(s) from r/{sub}")

            for post in self.subreddit.top(time_filter="day",limit=topN):
                if post.over_18 or len(post.selftext) < 250 : 
                    continue
                story = {
                    "subreddit": sub,
                    "title" : post.title,
                    "text": post.selftext,
                    "score": post.score,
                    "url": post.url,
                    "id":  post.id
                }
                self.stories.append(story)
        os.makedirs("rawjson", exist_ok=True)
        self.filename = f"./rawjson/reddit_stories_{datetime.now().strftime('%H_%d_%m_%Y')}.json"
        with open(self.filename,"w",encoding="utf-8") as f:
            json.dump(self.stories,f,ensure_ascii=False,indent=2)

        print(f"\033[32m[SLOP CURATOR::REDDITBOT]\033[37m Saved {len(self.stories)} stories to \033[36m{self.filename}\033[37m")

if __name__ == "__main__":
    redditscraper = RedditBot(client_id="x-x-x-x",
                              client_secret="x-x-x-x",
                              bot_string="x-x-x-x")
    
    subs = ["TrueOffMyChest", "AmItheAsshole","TIFU"]
    redditscraper.generateN(subs=subs,topN=5)