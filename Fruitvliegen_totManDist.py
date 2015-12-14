# The next algorithm is the as the original FindandSwap.
# The only difference is that the sorting begins at the end of the list
# instead of at the begin.
from collections import deque

class Genome(object):
	array = []
	totalManDist = 0
	swaps = 0
	swapLengthTotal = 0
	
	def __init__(self, array, totalManDist, swaps, swapLengthTotal):
		self.array = array
		self.totalManDist = totalManDist
		self.swaps = swaps
		self.swapLengthTotal = swapLengthTotal
		
"""class PosManDist(object):
	
	def __init__(self, curPos, manDist):
		self.curPos = curPos
		self.manDist = manDist"""
		

melanoStartTuple = (23, 1, 2, 11, 24, 22, 19, 6, 10, 7, 25, 20, 5, 8, 18, 12, 13, 14, 15, 16, 17, 21, 3, 4, 9)
melanoStart = [23, 1, 2, 11, 24, 22, 19, 6, 10, 7, 25, 20, 5, 8, 18, 12, 13, 14, 15, 16, 17, 21, 3, 4, 9]

noResult = 1
swaps = 0
swapLengthTotal = 0
totalManDist = 0
prQueue = []
results = []

print "\n" + "Start: " + str(melanoStart)

# determine total manhattan distance of first array
for a in range(len(melanoStart)):
	totalManDist += abs(melanoStart.index(a + 1) - a)

print "Total Manhattan Distance: " + str(totalManDist) + "\n"
prQueue.append(Genome(melanoStart, totalManDist, swaps, swapLengthTotal))
newBest = True

# make new objects until one object is fully sorted
while noResult != 25:

	if prQueue[0].totalManDist != 0:
		results.append(prQueue[0])
		
		prQueue = []
		noResult += 1
		swaps = 1
		
		melanoStart = list(melanoStartTuple)
		swapLengthTotal = len(melanoStart[0:noResult])
		melanoStart[0:noResult] = reversed(melanoStart[0:noResult])
		
		totalManDist = 0
		for a in range(len(melanoStart)):
			totalManDist += abs(melanoStart.index(a + 1) - a)
			
		prQueue.append(Genome(melanoStart, totalManDist, swaps, swapLengthTotal))

	if newBest == False:
		prQueue = []
		noResult += 1
		swaps = 1

		melanoStart = list(melanoStartTuple)
		swapLengthTotal = len(melanoStart[0:noResult])
		melanoStart[0:noResult] = reversed(melanoStart[0:noResult])
		
		totalManDist = 0
		for a in range(len(melano)):
			totalManDist += abs(melanoStart.index(a + 1) - a)
			
		prQueue.append(Genome(melanoStart, totalManDist, swaps, swapLengthTotal))
		
		"""prQueue[0].array[5:17] = reversed(prQueue[0].array[5:17])
		prQueue[0].swapLengthTotal += len(prQueue[0].array[5:17])
		prQueue[0].swaps += 1"""
		
		"""print "bla"
		bigManDist = []
		for x in range(len(prQueue[0].array)):
			manDist = abs(prQueue[0].array.index(x + 1) - x)
			if len(bigManDist) <= 2:
				bigManDist.append(PosManDist(x, manDist))
			else:
				smallestMD = 100
				for obj in bigManDist:
					if obj.manDist < smallestMD:
						smallestMD = obj.manDist
				if manDist > smallestMD:
					for obj in bigManDist:
						if smallestMD == obj.manDist:
							obj = PosManDist(x, manDist)
		
		print bigManDist[0].curPos
		print bigManDist[1].curPos
		latestPos = 0
		objNum = 0
		for y in range(len(bigManDist)):
			if bigManDist[y].curPos > latestPos:
				latestPos = bigManDist[y].curPos
				objNum = y
				
		if objNum == 1:
			prQueue[0].swaps += 1
			prQueue[0].swapLengthTotal += len(prQueue[0].array[bigManDist[0].curPos:bigManDist[1].curPos + 1])
			prQueue[0].array[bigManDist[0].curPos:bigManDist[1].curPos + 1] = reversed(prQueue[0].array[bigManDist[0].curPos:bigManDist[1].curPos + 1])
		else:
			prQueue[0].swaps += 1
			prQueue[0].swapLengthTotal += len(prQueue[0].array[bigManDist[1].curPos:bigManDist[0].curPos + 1])
			prQueue[0].array[bigManDist[1].curPos:bigManDist[0].curPos + 1] = reversed(prQueue[0].array[bigManDist[1].curPos:bigManDist[0].curPos + 1])
		
		print prQueue[0].swapLengthTotal
		print prQueue[0].array
		
		totalManDist = 0
		for r in range(len(melano)):
			totalManDist += abs(melano.index(r + 1) - r)
			
		prQueue[0].totalManDist = totalManDist
		print prQueue[0].totalManDist"""
		
		"""prevTotManDist = prQueue[0].totalManDist
		myDeque = deque(prQueue)
		myDeque.popleft()
		prQueue = list(myDeque)"""
		
	newBest = False
	# take array with best manhattan distance so far
	melanoBest = prQueue[0]
	
	""" #UNDER CONSTRUCTION
	if melanoBest.totalManDist == prevTotManDist:
		sameTotManDist += 1
		if sameTotManDist == 5:
			while prQueue[0].totalManDist == prevTotManDist:"""
			
	print "Array: " + str(melanoBest.array)
	print "Total Manhattan Distance: " + str(melanoBest.totalManDist)
	print "Swaps: " + str(melanoBest.swaps)
	print "Total Swap Length: " + str(melanoBest.swapLengthTotal) + "\n"
	melanoTuple = tuple(melanoBest.array)
	# iterate over all possible swaps
	for i in range(len(melanoBest.array)):
		if i == 24:
			break
		for j in range(len(melanoBest.array)):
			if i + j + 2 > 25:
				break
				
			#print i
			#print i + j + 2
			melano = list(melanoTuple)
			##print "melano: " + str(melano)
			swaps = melanoBest.swaps
			swapLengthTotal = melanoBest.swapLengthTotal
			
			swapLengthTotal += len(melano[i:i + j + 2])
			melano[i:i + j + 2] = reversed(melano[i:i + j + 2])
			#print "revMelano" + str(melano)
			swaps += 1
			
			# determine total manhattan distance of new array
			totalManDist = 0
			for a in range(len(melano)):
				totalManDist += abs(melano.index(a + 1) - a)
				
			#print "totalManDist: " + str(totalManDist)
			
			# make object and put in right place of priority queue
			# if total manhattan distance is bigger than the last in queue, add object to the end
			if totalManDist >= prQueue[-1].totalManDist:
				prQueue.append(Genome(melano, totalManDist, swaps, swapLengthTotal))
				#print "pos in queue: last" 
				#print "length queue: " + str(len(prQueue)) + "\n"
			else:
				# find the right place in queue
				pos = 0
				while prQueue[pos].totalManDist <= totalManDist:
					pos += 1
				#print "pos in queue: " + str(pos + 1)
					
				# move old objects ON and AFTER right place by one to the right
				listLength = len(prQueue)
				prQueue.append(prQueue[listLength - 1])

				while listLength - 1 != pos:
					prQueue[listLength] = prQueue[listLength - 1]
					listLength -= 1
						
				if pos == 0:
					newBest = True
				# put new object on right place
				prQueue[pos] = Genome(melano, totalManDist, swaps, swapLengthTotal)
				#print "length queue: " + str(len(prQueue)) + "\n"
	
print "---------------RESULT---------------"
for r in results:
	print "Array: " + str(r.array)
	print "Total Manhattan Distance: " + str(r.totalManDist)
	print "Swaps: " + str(r.swaps)
	print "Total Swap Length: " + str(r.swapLengthTotal)

"""print "---------------RESULT---------------"
print "Array: " + str(prQueue[0].array)
print "Total Manhattan Distance: " + str(prQueue[0].totalManDist)
print "Swaps: " + str(prQueue[0].swaps)
print "Total Swap Length: " + str(prQueue[0].swapLengthTotal)"""