
stacks = []
size = 0
addingStacks = True
with open('input.txt') as f:
	lines = f.readlines()
	for line in lines:
		if size == 0:
			size = len(line)//4
			for i in range(0,size):
				stacks.append([])
		if addingStacks:
			if line[1].isdigit():
				addingStacks = False
			else:
				for i in range(0,size):
					item = line[i*4+1] 
					item.strip()
					if not item.isspace():
						stacks[i].insert(0,item)
		else:
			if line.isspace():
				continue
			else:
				line = line.strip()
				line = line.replace("move ", "")
				line = line.replace("from ", "")
				line = line.replace("to ","")
				output = line.split(" ")

				amount = int(output[0])
				fromIndex = int(output[1])-1
				toIndex = int(output[2])-1

				tempList = stacks[fromIndex][len(stacks[fromIndex])-amount:]
				# tempList.reverse()
				stacks[toIndex].extend(tempList)
				stacks[fromIndex] = stacks[fromIndex][:len(stacks[fromIndex])-amount]
				print(stacks)

for stack in stacks:
	print(stack[-1])