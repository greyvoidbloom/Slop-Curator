import os
import json
class CredentialsManager:
    def __init__(self,config_path):
        print(f"\033[33m[SLOP CURATOR::CREDENTIALS MANAGER]\033[37m Credential Manager is active..")
        self.config_file = config_path
        if not os.path.exists(self.config_file):
            print(f"\033[31m[SLOP CURATOR::CREDENTIALS MANAGER]\033[37m No Config Found.. Let's set it up for you..")
            self.owner = input("\033[36m[SLOP CURATOR::CREDENTIALS MANAGER]\033[37m What do we call you? (Username) : ").strip()
            self.red_client_id = input("\033[36m[SLOP CURATOR::CREDENTIALS MANAGER]\033[37m Enter the reddit app client ID : ").strip()
            self.red_client_secret = input("\033[36m[SLOP CURATOR::CREDENTIALS MANAGER]\033[37m Enter the reddit client secret : ").strip()
            self.user_agent = input("\033[36m[SLOP CURATOR::CREDENTIALS MANAGER]\033[37m Enter the bot string : ").strip()
            self.openai_key = input("\033[36m[SLOP CURATOR::CREDENTIALS MANAGER]\033[37m Enter your openAI key : ").strip()
            self.configs = {
                    "owner" : self.owner,
                    "reddit_client_id" : self.red_client_id,
                    "reddit_client_secret" : self.red_client_secret,
                    "user_agent" : self.user_agent,
                    "openai_key" : self.openai_key
            }
            with open(self.config_file,"w") as f:
                    json.dump(self.configs,f,indent=2)
                    print("033[32m[SLOP CURATOR::CREDENTIALS MANAGER]\033[37m Configs have been saved ..")
        else:
            with open(self.config_file,"r") as f:
                details = json.load(f)
                self.owner = details["owner"]
                self.red_client_id = details["reddit_client_id"]
                self.red_client_secret = details["reddit_client_secret"]
                self.user_agent = details["user_agent"]
                self.openai_key = details["openai_key"]
                 
                        




