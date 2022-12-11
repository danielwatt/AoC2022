class Monkey:
    def __init__(self, items, operation, test, testNum):
        self.items = items
        self.operation = operation
        self.test = test
        self.testNum = testNum
        self.inspections = 0
#Test
# monkeys = [
# 	Monkey([79, 98], lambda old : old*19, lambda item: 2 if item%23 == 0 else 3, 23),
# 	Monkey([54, 65, 75, 74], lambda old : old +6, lambda item: 2 if item%19 == 0 else 0,19),
# 	Monkey([79, 60, 97], lambda old : old * old, lambda item: 1 if item%13 == 0 else 3,13),
# 	Monkey([74], lambda old : old + 3, lambda item: 0 if item%17 == 0 else 1,17)
# ]



monkeys = [
	Monkey([91, 58, 52, 69, 95, 54], lambda old : old*13, lambda item: 1 if item%7 == 0 else 5,7),
	Monkey([80, 80, 97, 84], lambda old : old * old, lambda item: 3 if item%3 == 0 else 5,3),
	Monkey([86, 92, 71], lambda old : old + 7, lambda item: 0 if item%2 == 0 else 4,2),
	Monkey([96, 90, 99, 76, 79, 85, 98, 61], lambda old : old + 4, lambda item: 7 if item%11 == 0 else 6,11),
	Monkey([60, 83, 68, 64, 73], lambda old : old * 19, lambda item: 1 if item%17 == 0 else 0,17),
	Monkey([96, 52, 52, 94, 76, 51, 57], lambda old : old + 3, lambda item: 7 if item%5 == 0 else 3,5),
	Monkey([75], lambda old : old + 5, lambda item: 4 if item%13 == 0 else 2,13),
	Monkey([83, 75], lambda old : old + 1, lambda item: 2 if item%19 == 0 else 6,19)
]

largestNum = 1

for monkey in monkeys:
	largestNum *= monkey.testNum

for i in range(0,10000):
	for idx,monkey in enumerate(monkeys):
		while len(monkey.items) > 0:
			itemToTest = monkey.items.pop(0)
			newLevel = monkey.operation(itemToTest) % largestNum
			newMonkey = monkey.test(newLevel)
			monkeys[newMonkey].items.append(newLevel)
			monkey.inspections += 1

ans = []
for monkey in monkeys:
	ans.append(monkey.inspections)
ans.sort()
print(ans)
print(ans[len(ans)-1] * ans[len(ans)-2])
