melano = [23, 1, 2, 11, 24, 22, 19, 6, 10, 7, 25, 20, 5, 8, 18, 12, 13, 14, 15, 16, 17, 21, 3, 4, 9]
#melano = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]

dictionary = { 	 1 : 1,
				 2 : 1,
				 3 : 1,
				 4 : 1,
				 5 : 1,
				 6 : 2,
				 7 : 2,
				 8 : 2,
				 9 : 2,
				10 : 2,
				11 : 3,
				12 : 3,
				13 : 3,
				14 : 3,
				15 : 3,
				16 : 4,
				17 : 4,
				18 : 4,
				19 : 4,
				20 : 4,
				21 : 5,
				22 : 5,
				23 : 5,
				24 : 5,
				25 : 5	}
				
class Group(object):
	
	def __init__(self, groupBegin, groupEnd, level):
		self.groupBegin = groupBegin
		self.groupEnd = groupEnd
		self.level = level
		
groups = 0
swapLengthTotal = 0
while groups != 5:
	groups = 1
	groupList = []
	groupBegin = 0

	for i in range(len(melano)):
		if i == 24:
			groupList.append(Group(groupBegin, i, dictionary[melano[i]]))
			break
		if dictionary[melano[i]] != dictionary[melano[i + 1]]:
			groupList.append(Group(groupBegin, i, dictionary[melano[i]]))
			groupBegin = i + 1
			groups += 1
			
	print "Groups: " + str(groups) + "\n"
	for group in groupList:
		print group.groupBegin
		print group.groupEnd
		print str(group.level) + "\n"

	swapScript = []
	beginChosen = False
	for k in range(len(groupList)):
		if beginChosen == False:
			swapBegin = k
			beginChosen = True
		if k == len(groupList) - 1:
			swapEnd = k
			if swapBegin != swapEnd:
				swapScript.append((swapBegin, swapEnd))
			break
		if groupList[k].level < groupList[k + 1].level:
			swapEnd = k
			beginChosen = False
			if swapBegin != swapEnd:
				swapScript.append((swapBegin, swapEnd))
				
				
	print swapScript
			
	for swap in swapScript:
		swapLengthTotal += len(melano[groupList[swap[0]].groupBegin:groupList[swap[1]].groupEnd + 1])
		print swapLengthTotal
		melano[groupList[swap[0]].groupBegin:groupList[swap[1]].groupEnd + 1] = reversed(melano[groupList[swap[0]].groupBegin:groupList[swap[1]].groupEnd + 1])
	print str(melano) + "\n"
	
print melano
print "swapLengthTotal: " + str(swapLengthTotal)

for x in range(len(melano)):
	if melano.index(x + 1) != x:
		swapLengthTotal += len(melano[x:melano.index(x + 1) + 1])
		melano[x:melano.index(x + 1) + 1] = reversed(melano[x:melano.index(x + 1) + 1])
		print melano
		print str(swapLengthTotal) + "\n"
		
			
		
"""group1 = []
for v in range(0,5):
	group1.append(melano[x])
	
group2 = []
for w in range(6,10):
	group2.append(melano[x])
	
group3 = []
for x in range(11,15):
	group3.append(melano[x])
	
group4 = []
for y in range(16,20):
	group4.append(melano[x])
	
group5 = []
for z in range(21,25):
	group5.append(melano[x])

melanoTuple = tuple(melano)
for	l in range(5):
	for m in range(5):
		group1."""
				