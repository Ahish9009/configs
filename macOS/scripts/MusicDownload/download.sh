#!/bin/bash	
mkdir /users/Ahish/Desktop/Ahish/Music/temp

for (( i=1; i<$(python3 /users/Ahish/Desktop/Ahish/Scripts/MusicDownload/totallen.py)+1; i++ )); do echo $i > /users/Ahish/Desktop/Ahish/Scripts/MusicDownload/current.txt ; youtube-dl -o "/users/Ahish/Desktop/Ahish/Music/temp/%(title)s.%(ext)s" --extract-audio --audio-format mp3 $(python3 /users/Ahish/Desktop/Ahish/Scripts/MusicDownload/get-line.py) ; done
rm /users/Ahish/Desktop/Ahish/Scripts/MusicDownload/temp2.txt

/users/Ahish/Desktop/Ahish/Scripts/SongRenamer/modify.sh
