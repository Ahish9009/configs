#!/bin/bash
osascript -e 'tell application "Safari" to get URL of tabs of window 1' > /users/Ahish/Desktop/Ahish/Scripts/MusicDownload/temp.txt
python3 /users/Ahish/Desktop/Ahish/Scripts/MusicDownload/change.py
