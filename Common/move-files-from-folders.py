import os
import shutil

self_name = __file__
#self_name = os.path.normpath(self_name)
print(self_name)

source = os.getcwd()
destination = os.path.dirname(source) + "\\RES\\"

if not os.path.exists(destination):
    os.mkdir(destination)

print("s:\t", source)
print("d:\t", destination)

# files = os.listdir(source)
# for file in files:
#     file_name = os.path.join(source, file)
#     shutil.move(file_name, destination)

for path, dir_folder, files in os.walk(source):
    for file in files:
        full_path = os.path.join(path, file)

        print("MOVE FILE:\t", full_path)

        if os.path.samefile(str(full_path), str(self_name)):
            print("SKIP SELF")
            continue

        if os.path.exists(os.path.join(destination, file)):
            print("FILE ALREADY EXISTS")
            continue

        print("TARGET PATH:\t", destination)
        
        shutil.move(full_path, destination)

input()