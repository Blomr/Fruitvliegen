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
		

melanoStart = [23, 1, 2, 11, 24, 22, 19, 6, 10, 7, 25, 20, 5, 8, 18, 12, 13, 14, 15, 16, 17, 21, 3, 4, 9]
swaps = 0
swapLengthTotal = 0
totalManDist = 0
prQueue = []

print "\n" + "Start: " + str(melanoStart)

# determine total manhattan distance of first array
for a in range(len(melanoStart)):
	totalManDist += abs(melanoStart.index(a + 1) - a)

print "Total Manhattan Distance: " + str(totalManDist) + "\n"
prQueue.append(Genome(melanoStart, totalManDist, swaps, swapLengthTotal))
newBest = True

# make new objects until one object is fully sorted
while prQueue[0].totalManDist != 0:
	
	if newBest == False and len(prQueue) != 1:
		prevTotManDist = prQueue[0].totalManDist
		myDeque = deque(prQueue)
		myDeque.popleft()
		prQueue = list(myDeque)
		
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
print "Array: " + str(prQueue[0].array)
print "Total Manhattan Distance: " + str(prQueue[0].totalManDist)
print "Swaps: " + str(prQueue[0].swaps)
print "Total Swap Length: " + str(prQueue[0].swapLengthTotal)