import os
import eyed3

directory = os.getcwd()

# for root, dirs, files in os.walk("."):
# 	for name in files:
for filename in os.scandir(directory):
	if filename.is_file():
		name = filename.path
		if name.endswith('.mp3'):
			try:
				audiofile = eyed3.load(name)
				artist = audiofile.tag.artist
				if os.path.exists(artist) == False:
					os.mkdir(artist)
				os.rename(name, artist+"/"+name)
			except:
				print(f"file {name} failed")

input()