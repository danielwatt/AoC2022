priority = 0
with open('input.txt') as f:
	lines = f.readlines()
	group = 0
	items = set()
	matchingItem = ""
	for line in lines:
		if group >= 3:
			group = 0
			if matchingItem.isupper():
				oneBased = ord(matchingItem) - 64 + 26
				priority = oneBased + priority
			else:
				oneBased = ord(matchingItem) - 96
				priority = oneBased + priority

		newItems = set()
		for idx, item in enumerate(line):
			if item != "\n":
				if group == 0:
					newItems.add(item)
				elif group == 1 and item in items:
					newItems.add(item)
				elif group == 2 and item in items:
					matchingItem = item
					break
		group += 1
		items = newItems
	if matchingItem.isupper():
		oneBased = ord(matchingItem) - 64 + 26
		priority = oneBased + priority
	else:
		oneBased = ord(matchingItem) - 96
		priority = oneBased + priority

print(priority)