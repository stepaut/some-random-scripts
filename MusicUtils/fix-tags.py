import os
import eyed3

directory = input()
if directory == "":
    directory = os.getcwd()

for filename in os.scandir(directory):
    if filename.is_file():
        name = filename.path
        dir = name.replace(filename.name, "")
        if name.endswith(".mp3"):
            try:
                audiofile = eyed3.load(name)
                audiofile.tag.artist = audiofile.tag.artist.replace("\x00", " & ")
                audiofile.tag.save()
            except Exception as e:
                print(f"file {name} failed")