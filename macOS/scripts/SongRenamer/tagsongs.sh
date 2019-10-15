#!/bin/bash

# python3 /users/Ahish/Desktop/Ahish/Scripts/SongRenamer/totallen.py > /users/Ahish/Desktop/Ahish/Scripts/SongRenamer/total.txt
for ((i = 1; i < $(python3 /users/Ahish/Desktop/Ahish/Scripts/SongRenamer/totallen.py)+1; i++))
do
	echo $i > /users/Ahish/Desktop/Ahish/Scripts/SongRenamer/current.txt
	l1="$(python3 /users/Ahish/Desktop/Ahish/Scripts/SongRenamer/get-line1.py)"
	l2="$(python3 /users/Ahish/Desktop/Ahish/Scripts/SongRenamer/get-line2.py)"
	mv "$l1" "$l2"
	id3v2 -a "$(python3 /users/Ahish/Desktop/Ahish/Scripts/SongRenamer/get-artist.py)" -t "$(python3 /users/Ahish/Desktop/Ahish/Scripts/SongRenamer/get-name.py)" "$l2"
	cp "$l2" /users/Ahish/Desktop/Ahish/Music
	open "$l2"
	open "$l2"
	open "$l2"
done

rm -rf /users/Ahish/Desktop/Ahish/Music/temp
