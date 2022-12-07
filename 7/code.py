class File:
	def __init__(self, name, isDirectory=False, size=0, parent=None):
		self.name = name
		self.isDirectory = isDirectory
		self.size = size
		self.parent = parent
		self.children = {}
headDir = None
currentFile = None
ans = 0

def recurseFile(file):
	totalSize = 0
	ans = []
	for childName in file.children:
		child = file.children[childName]
		if child.isDirectory:
			output = recurseFile(child)
			totalSize += output[0]
			ans += output[1]
		else:
			totalSize += child.size
	file.size = totalSize

	# 43313415-40000000 = 3313415
	if totalSize >= 3313415:
		ans.append(totalSize)
	return (totalSize, ans)


with open('input.txt') as f:
	lines = f.readlines()
	for line in lines:
		print(line)
		line = line.strip()
		# print(line)
		if line[0] == "$":
			if line[2:4] == "cd":
				if len(line) == 7 and line[5:7] == "..":
					currentFile = currentFile.parent
				else:
					enteringDir = line[5:]
					if enteringDir == "/":
						headDir = File(enteringDir, True)
						currentFile = headDir
					else:
						currentFile = currentFile.children[enteringDir]
		else:
			output = line.split(" ")
			fileName = output[1]
			file = None
			if output[0] == "dir":
				file = File(fileName,True,-99,currentFile)
			else:
				size = int(output[0])
				file = File(fileName,False,size,currentFile)
			currentFile.children[fileName] = file

	#traverse
	currentFile = headDir
	output = recurseFile(currentFile)
	output[1].sort()
	print(output[1][0])
	print(recurseFile(currentFile))


			





