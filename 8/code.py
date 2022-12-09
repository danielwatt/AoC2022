trees = []
with open('input.txt') as f:
	lines = f.readlines()
	for line in lines:
		line = line.strip()
		treeRow = []
		for val in line:
			treeRow.append(int(val))
		trees.append(treeRow)


lenX = len(trees[0])
lenY = len(trees)
viewableTrees = []
for y in range(0,lenY):
	xArr = []
	for x in range(0,lenX):
		xArr.append([0]*5)
	viewableTrees.append(xArr)
# print(viewableTrees)
# View from Top->Down
for x in range(0, lenX):
	for y in range(0, lenY):
		curTreeHeight = trees[y][x]
		viewable = 0
		for tempY in range(1,lenY-y):
			viewable += 1
			if trees[y+tempY][x] >= curTreeHeight:
				break
		viewableTrees[y][x][0] = viewable


# # View from Bottom->Top
for x in range(0, lenX):
	for y in reversed(range(0, lenY)):
		curTreeHeight = trees[y][x]
		viewable = 0
		for tempY in range(1,y+1):
			viewable += 1
			if trees[y-tempY][x] >= curTreeHeight:
				break
		viewableTrees[y][x][1] = viewable

# #Left->Right
for y in range(0, lenY):
	for x in range(0, lenX):
		curTreeHeight = trees[y][x]
		viewable = 0
		for tempX in range(1,lenX-x):
			# print("x:{}, y:{}, curTreeHeight:{}, tempX:{}, {}".format(x,y,curTreeHeight,tempX, trees[y][x+tempX]))
			viewable += 1
			if trees[y][x+tempX] >= curTreeHeight:
				break
		viewableTrees[y][x][2] = viewable

ans = 0
# #Right
for y in range(0, lenY):
	for x in reversed(range(0, lenX)):
		curTreeHeight = trees[y][x]
		viewable = 0
		for tempX in range(1,x+1):
			viewable += 1
			if trees[y][x-tempX] >= curTreeHeight:
				break
		viewableTrees[y][x][3] = viewable
		viewableTrees[y][x][4] = viewableTrees[y][x][0] * viewableTrees[y][x][1] * viewableTrees[y][x][2] * viewableTrees[y][x][3]
		ans = max(viewableTrees[y][x][4],ans)

# ans = 0
# for x in range(0, lenX):
# 	for y in range(0, lenY):
# 		if viewableTrees[y][x]:
# 			ans += 1
# print(viewableTrees)
print(ans)		





		
			





