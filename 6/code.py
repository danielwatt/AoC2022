with open('input.txt') as f:
	lines = f.readlines()
	for line in lines:
		frontIdx = 13;
		backIdx = 0;
		dupe = {}
		for i in range(0,14):
			val = line[i]
			if val not in dupe:
				dupe[val] = 1
			else:
				dupe[val] += 1

		for i in range(0,len(line)):
			if len(dupe) == 14:
				print(frontIdx+1)
				break
			val = line[backIdx]
			if dupe[val] == 1:
				del dupe[val]
			else: 
				dupe[val] -= 1
			backIdx += 1
			frontIdx += 1
			val = line[frontIdx]
			if val not in dupe:
				dupe[val] = 1
			else:
				dupe[val] += 1




