score = 0
with open('input.txt') as f:
	lines = f.readlines()
	for line in lines:
		# Rock
		if line[0] == "A":
			if line[2] == "X":
				score = score + 0
				score = score + 3
			elif line[2] == "Y":
				score = score + 3
				score = score + 1
			elif line[2] =="Z":
				score = score + 6
				score = score + 2
				# Paper		
		elif line[0] == "B":
			if line[2] == "X":
				score = score + 0
				score = score + 1
			elif line[2] == "Y":
				score = score + 3
				score = score + 2
			elif line[2] =="Z":
				score = score + 6
				score = score + 3
				# Scissors
		elif line[0] == "C":
			if line[2] == "X":
				score = score + 0
				score = score + 2
			elif line[2] == "Y":
				score = score + 3
				score = score + 3
			elif line[2] =="Z":
				score = score + 6
				score = score + 1
		print(score)


print(score)