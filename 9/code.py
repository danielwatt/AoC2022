import math

trees = []
positions = []
for i in range(0,10):
	positions.append((0,0))
traversedPositions = set()
traversedPositions.add(positions[0])

def newTPosition(h,t):
	x = pow(h[0]-t[0],2)
	y = pow(h[1]-t[1],2)
	dist = math.sqrt(x+y)
	# Greater less than 1.4 means outside radius 1
	if dist < 1.5:
		return t

	if h[0] != t[0] and h[1] != t[1]:
		if (h[0]-t[0] == 2 and h[1]-t[1] == 1) or (h[0]-t[0] == 1 and h[1]-t[1] == 2) or (h[0]-t[0] == 2 and h[1]-t[1] == 2):
			return (t[0]+1,t[1]+1)
		if (h[0]-t[0] == 2 and h[1]-t[1] == -1) or (h[0]-t[0] == 1 and h[1]-t[1] == -2) or (h[0]-t[0] == 2 and h[1]-t[1] == -2):
			return (t[0]+1,t[1]-1)
		if (h[0]-t[0] == -2 and h[1]-t[1] == -1) or (h[0]-t[0] == -1 and h[1]-t[1] == -2) or (h[0]-t[0] == -2 and h[1]-t[1] == -2):
			return (t[0]-1,t[1]-1)
		return (t[0]-1,t[1]+1)

	if h[0] == t[0]:
		if h[1] > t[1]:
			return (t[0], t[1]+ 1)
		return (t[0], t[1] - 1) 
	
	if h[0] > t[0]:
		return (t[0] + 1, t[1])
	return (t[0] - 1, t[1])


with open('input.txt') as f:
	lines = f.readlines()
	for line in lines:
		line = line.strip()
		movement = line.split(" ")
		direction = movement[0]
		distance = int(movement[1])
		for i in range(0,distance):
			if direction == "R":
				positions[0] = (positions[0][0]+1, positions[0][1]) 
			if direction == "L":
				positions[0] = (positions[0][0]-1, positions[0][1]) 
			if direction == "U":
				positions[0] = (positions[0][0], positions[0][1] + 1) 
			if direction == "D":
				positions[0] = (positions[0][0], positions[0][1] - 1)

			for i in range (1,10): 
				tPosition = newTPosition(positions[i-1], positions[i])
				positions[i] = tPosition
				if i == 9:
					traversedPositions.add(positions[9])

print(len(traversedPositions))


