import os, shutil

print("Enter source directory - ")
source = str(input())

directory = os.fsencode(source)

try:
    os.listdir(directory)
except:
    print("No source directory exists")
    exit()


print("Enter destination directory - ")
destination = str(input())


for file in os.listdir(directory):
    filename = os.fsdecode(file)

    if filename.endswith(".img"):
        if not os.path.exists(f"./{destination}/images"):
            os.mkdir(f"./{destination}/images")
        shutil.move(f"./{source}/{filename}", f"./{destination}/images/{filename}")
        print("moved image files")

    elif filename.endswith(".txt"):
        if not os.path.exists(f"./{destination}/text"):
            os.mkdir(f"./{destination}/text")
        shutil.move(f"./{source}/{filename}", f"./{destination}/text/{filename}")
        print("moved text files")

    elif filename.endswith(".mp3"):
        if not os.path.exists(f"./{destination}/audio"):
            os.mkdir(f"./{destination}/audio")
        shutil.move(f"./{source}/{filename}", f"./{destination}/audio/{filename}")
        print("moved audio files")

    elif filename.endswith(".mp4"):
        if not os.path.exists(f"./{destination}/video"):
            os.mkdir(f"./{destination}/video")
        shutil.move(f"./{source}/{filename}", f"./{destination}/video/{filename}")
        print("moved video files")
