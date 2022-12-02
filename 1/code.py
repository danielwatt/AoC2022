cals = []
total = 0
with open('input.txt') as f:
	lines = f.readlines()
	for line in lines:
		print(line)
		if line == "\n":
			cals.append(total)
			total = 0
		else:
			if line[-1] == "\n":
				lines = line[:len(lines)-2]
			total = int(line) + total

cals.sort()
print(cals)