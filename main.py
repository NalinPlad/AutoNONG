import youtube_dl

from colorama import *
from halo import Halo

import sys
import os
import shutil

from os.path import expanduser
import fnmatch

print("Welcome to AutoNONG \N{rocket}\n")

VID_URL = input("Enter URL to youtube video:   ")
ID_NAME = input("Enter ID to replace:   ")

VID_INFO = youtube_dl.YoutubeDL().extract_info(url=VID_URL, download=False)

ydl_opts = {
    "format": "bestaudio/best",
    "postprocessors": [
        {
            "key": "FFmpegExtractAudio",
            "preferredcodec": "mp3",
            "preferredquality": "192",
        }
    ],
    "keepvideo": False,
    "quiet": True,
}

string = (
    Fore.MAGENTA
    + f"\n\N{rocket} NONG Automation for "
    + Fore.LIGHTGREEN_EX
    + VID_INFO["title"]
    + Fore.MAGENTA
    + " has begun \N{airplane departure} \n"
)
print(string)

# Downloading the video
spinner_DOWNLOADING = Halo(
    text=Fore.RED + "\N{stopwatch}  Downloading...", spinner="dots"
)
spinner_DOWNLOADING.start()

with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download([VID_URL])

cwd = os.getcwd()
downloaded_loc = ""
for root, dirs, files in os.walk(cwd):
    for file in files:
        if file.endswith(".mp3"):
            downloaded_loc = root + "/" + str(file)


os.rename(downloaded_loc, ID_NAME + ".mp3")

spinner_DOWNLOADING.stop_and_persist("\N{check mark}")

# Replacing the video
spinner_REPLACING = Halo(text=Fore.RED + f"\N{minibus} Replacing Song ID {ID_NAME}...")
spinner_REPLACING.start()

source = os.path.abspath(ID_NAME + ".mp3")
destination = expanduser("~") + "/Library/Caches/"
filename = os.path.basename(source)
dest = os.path.join(destination, filename)
shutil.move(source, dest)

spinner_REPLACING.stop_and_persist("\N{check mark}")

print(
    Fore.MAGENTA
    + "\nSuccess! ID "
    + Fore.RED
    + ID_NAME
    + Fore.GREEN
    + " replaced! \N{desktop computer}"
)
