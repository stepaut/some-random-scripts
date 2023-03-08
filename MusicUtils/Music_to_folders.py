import os
import eyed3

for root, dirs, files in os.walk("."):
	for name in files:
		if name.endswith('.mp3'):
			audiofile = eyed3.load(name)
			artist = audiofile.tag.artist
			if os.path.exists(artist)==False:
				os.mkdir(artist)
			os.rename(name, artist+"/"+name)