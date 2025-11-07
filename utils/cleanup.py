import shutil

def cleanUp(folders):
    for folder in folders:
        try:
            shutil.rmtree(folder)
            print(f"\033[32m[SLOP CURATOR::CLEANER]\033[37m Removed {folder}..")
        except:
            print(f"\033[31m[SLOP CURATOR::CLEANER]\033[37m Couldn't remove {folder}..")

if __name__ == "__main__":
    folders = ["rawjson","cleaned_stories","generated_audio","generated_videos"]
    cleanUp(folders=folders)