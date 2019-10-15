
try:
	with open('/users/Ahish/Desktop/Ahish/Scripts/SongRenamer/path.txt', 'r') as f:

		path = f.read()
		path = path[:len(path)-1]

except:
	path = ''

with open("/users/Ahish/Desktop/Ahish/Scripts/SongRenamer/songs.txt", 'r') as f:

	lines = f.readlines()
	print(len(lines))