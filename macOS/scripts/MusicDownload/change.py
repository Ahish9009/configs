import os

with open ("/users/Ahish/Desktop/Ahish/Scripts/MusicDownload/temp.txt", "r") as fread:

	text = fread.read().split(', ')

	# print(text)

	try:
		with open("/users/Ahish/Desktop/Ahish/Scripts/MusicDownload/temp2.txt", 'r') as fwrite:
			old = fwrite.read()
	except:
		old = ''

	with open("/users/Ahish/Desktop/Ahish/Scripts/MusicDownload/temp2.txt", "a") as fwrite:

		# print(old)
		# print(old, text)

		for i in range(len(text)):

			if old.find(text[i]) == -1 and text[i].find('youtube.com') != -1:

				# print(text[i])

				if i != len(text)-1:
					fwrite.write(text[i]+"\n")
				else:
					fwrite.write(text[i])

os.remove("/users/Ahish/Desktop/Ahish/Scripts/MusicDownload/temp.txt")
