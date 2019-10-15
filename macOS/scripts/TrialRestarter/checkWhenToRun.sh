#!/bin/bash

lastUpdate=$(cat /users/Ahish/Desktop/Ahish/Scripts/TrialRestarter/lastUpdated)
nextUpdate=`expr $lastUpdate + 518400`

curr=$(date +%s)

if [ $curr -gt $nextUpdate ]
then
	python3 /users/Ahish/Desktop/Ahish/Scripts/TrialRestarter/changeKey.py
	date +%s > /users/Ahish/Desktop/Ahish/Scripts/TrialRestarter/lastUpdated
fi

