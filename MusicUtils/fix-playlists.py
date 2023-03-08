import os

for root, dirs, files in os.walk("."):
	for name in files:
		if name.endswith('.m3u'):
			fname = os.path.join(root, name)
			print(fname)
			with open (fname, 'r', encoding="utf8") as f: 
				old_data = f.read()

			new_data = old_data.replace('D:\YandexDisk\music', 'D:\MUSIC-LIBRARY')

			with open (fname, 'w', encoding="utf8") as f: 
				f.write(new_data)
