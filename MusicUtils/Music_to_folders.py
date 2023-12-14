import os
import eyed3

directory = input()
if directory == "":
    directory = os.getcwd()

for filename in os.scandir(directory):
    if filename.is_file():
        dir = filename.path.replace(filename.name, "")
        if filename.path.endswith(".mp3"):
            try:
                audiofile = eyed3.load(filename.path)
                artist = audiofile.tag.artist
                if os.path.exists(dir + artist) == False:
                    os.mkdir(dir + artist)

                os.rename(filename.path, dir + artist + "\\" + filename.name)
            except Exception as e:
                print(f"file {filename.name} failed")