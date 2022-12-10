xVal = 1
cycle = 1
ans = 0
crt = []

for i in range(0,6):
	crt.append([False]*40)

def checkCycle(crt):
	row = cycle // 40
	idx = (cycle-1) % 40

	if idx == xVal -1 or idx == xVal or idx == xVal+1:
		crt[row][idx] = True
	return crt

with open('input.txt') as f:
	lines = f.readlines()
	for line in lines:
		line = line.strip()
		instruction = line.split(" ")

		if instruction[0] == "addx":
			delta = int(instruction[1])
			for cycleIncrease in range(1,2):
				cycle += cycleIncrease
				crt = checkCycle(crt)
			cycle += 1
			xVal += delta
		else:
			cycle += 1
		# print("xVal at {} == {}".format(cycle, xVal))
		crt = checkCycle(crt)
crt = checkCycle(crt)


for row in crt:
	line = ""
	for val in row:
		if val:
			line += "#"
		else:
			line += "."
	print(line)


