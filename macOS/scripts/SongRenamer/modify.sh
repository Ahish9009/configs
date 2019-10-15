#!/bin/bash
mkdir /users/Ahish/Desktop/Ahish/Music/temp2
ls /users/Ahish/Desktop/Ahish/Music/temp/ > /users/Ahish/Desktop/Ahish/Scripts/SongRenamer/songs.txt
# mv /users/Ahish/Desktop/Ahish/Music/temp2/songs.txt /users/Ahish/Desktop/Ahish/Music/temp/songs.txt 
rm -rf /users/Ahish/Desktop/Ahish/Music/temp2
echo /users/Ahish/Desktop/Ahish/Music/temp/ > /users/Ahish/Desktop/Ahish/Scripts/SongRenamer/path.txt
python3 /users/Ahish/Desktop/Ahish/Scripts/SongRenamer/mod-files.py
/users/Ahish/Desktop/Ahish/Scripts/SongRenamer/tagsongs.sh
