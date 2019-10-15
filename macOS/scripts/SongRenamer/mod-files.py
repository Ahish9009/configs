toRemove = ['lyrics', 'lyric', 'lyrical', 'hd', '_', 'video', 'sub', 'letra', 'letras', 'clip','official', 'oficial', 'officiel', '+', 'subtitle', 'subtitles', 'subtitulada', 'youtube', 'paroles', 'audio', 'music', 'song', 'hq']

forAsking = ['|', '&', "'", '@',"#", 'version', 'english', 'hindi', 'french', 'spanish', 'arabic', '(', ')', 'series', 'full', 'with', 'by', 'starring', 'feat', 'screen', 'lyrical', 'lyric', 'on screen']

notFirst = ['_', '-', "'", '|', '!', '@', '$', "#", "^", '&', '*', '(', ')', 'and']

def removeWords(line):

	words = line.split()
	# print(words)

	newwords = []

	for i in words:

		flag = 1;
		for j in toRemove:

			if i.find(j) != -1:
				flag = 0

		if flag:
			newwords+=[i]

	newline = ''
	for i in newwords:

		newline += i+' '

	return newline.rstrip(' ')

def addSpace(line):

	words = line.split('-')
	for i in range(len(words)):
		words[i] = words[i].lstrip(' ')
		words[i] = words[i].rstrip(' ')
	return ' - '.join(words)

def makeCaps(line):

	line = line.title()
	line = line.replace("I'M", "I'm")
	line = line.replace("Ft.", "ft.")
	# line = line.replace(" A ", "I'm")

	return line

def toAsk(line):

	if line.count('-') != 1:
		return True

	for i in forAsking:
		if line.find(i) != -1:
			return True

	words = line.split()
	if words[0] in notFirst:
		return True

	return False

#main------


try:
	with open('/users/Ahish/Desktop/Ahish/Scripts/SongRenamer/path.txt', 'r') as f:

		path = f.read()
		path = path[:len(path)-1]

except:
	path = ''

with open("/users/Ahish/Desktop/Ahish/Scripts/SongRenamer/songs.txt", 'r') as f:

	songs = f.readlines()

	newsongs = []
	total = len(songs)
	count = 1

	for i in songs:

		i = i.rstrip(' ')

		# print(i[len(i)-5:], 'a')

		if i[len(i)-5:]=='.mp3\n':
			i = i[:len(i)-5]

		elif i[len(i)-6:]=='.mp3*\n':
			i = i[:len(i)-6]

		i = i.lower()
		i = removeWords(i)

		i = addSpace(i)

		#if line contains ' or | or & or certain words or multiple or no hyphens, ask user
		if toAsk(i):
			print(str(count)+'/'+str(total)+': '+i)
			ans = input('Change or press enter to leave as it is: ')
			if ans.lower() != '':
				i = ans
			else:
				pass

		i = makeCaps(i)
		i = i.rstrip(' ')
		newsongs += [i]

		count += 1

with open('/users/Ahish/Desktop/Ahish/Scripts/SongRenamer/edited.txt', 'w') as f:

	for i in newsongs:
		f.write(i+'.mp3\n')
