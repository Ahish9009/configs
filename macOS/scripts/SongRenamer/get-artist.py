try:
	with open('/users/Ahish/Desktop/Ahish/Scripts/SongRenamer/path.txt', 'r') as f:

		path = f.read()
		path = path[:len(path)-1]

except:
	path = ''

val = ''

with open("/users/Ahish/Desktop/Ahish/Scripts/SongRenamer/current.txt", 'r') as f:
	n = int(f.read())

with open("/users/Ahish/Desktop/Ahish/Scripts/SongRenamer/edited.txt", 'r') as f:

	lines = f.readlines()
	# print(lines)
	current = lines[n-1]
	maxind = current.find(' - ')
	print(current[:maxind])