encompased = 0
with open('input.txt') as f:
	lines = f.readlines()
	for line in lines:
		line.strip()
		pairs = line.split(",")
		rangePairs = []
		for pair in pairs:
			bounds = pair.split("-")
			rangePairs.append((int(bounds[0]),int(bounds[1])))
		rangePairs.sort()

		if (rangePairs[0][0] <= rangePairs[1][0] and rangePairs[0][1] >= rangePairs[1][0]) or (rangePairs[0][0] == rangePairs[1][0]) or (rangePairs[0][1] == rangePairs[1][1]):
			encompased += 1
		print(rangePairs)

print(encompased)