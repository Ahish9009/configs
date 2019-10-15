try:
	with open("/users/Ahish/Desktop/Ahish/Scripts/MusicDownload/current.txt", "r") as f:
		n = int(f.read())
		
	with open("/users/Ahish/Desktop/Ahish/Scripts/MusicDownload/temp2.txt", 'r') as f:

		lines = f.readlines()
		# print(lines)
		print(lines[n-1][:len(lines[n-1])-1])
	
except:
	assert "No files to download!"