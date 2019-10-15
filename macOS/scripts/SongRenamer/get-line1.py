try:
	with open('/users/Ahish/Desktop/Ahish/Scripts/SongRenamer/path.txt', 'r') as f:

		path = f.read()
		path = path[:len(path)-1]

except:
	path = ''

val = ''

with open("/users/Ahish/Desktop/Ahish/Scripts/SongRenamer/current.txt", 'r') as f:
	n = int(f.read())

with open("/users/Ahish/Desktop/Ahish/Scripts/SongRenamer/songs.txt", 'r') as f:

	lines = f.readlines()
	# print(lines)
	val += path
	val += lines[n-1][:len(lines[n-1])-1]

print(val)