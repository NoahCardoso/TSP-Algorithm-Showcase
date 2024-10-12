import json

# File path to the JSON file
file_path = 'coordinates.json'

def getPoints():
	# Open the JSON file and read its content
	with open(file_path, 'r') as json_file:
		data = json.load(json_file)

	# Print the data to see what was read
	points = []
	for point in data:
		points.append((point['x'], point['y']))
	print(points)
	return points
