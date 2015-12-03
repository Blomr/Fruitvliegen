# The next algorithm is the as the original FindandSwap.
# The only difference is that the sorting begins at the end of the list
# instead of at the begin.
from collections import deque

class Genome(object):
	array = []
	history = []
	totalManDist = 0
	swaps = 0
	minFutureSwaps = 0
	score = 0
	swapLengthTotal = 0
	
	def __init__(self, array, history, totalManDist, swaps, minFutureSwaps, score, swapLengthTotal):
		self.array = array
		self.history = history
		self.totalManDist = totalManDist
		self.swaps = swaps
		self.minFutureSwaps = minFutureSwaps
		self.score = score
		self.swapLengthTotal = swapLengthTotal
		
# initialize variables
melanoStart = [23, 1, 2, 11, 24, 22, 19, 6, 10, 7, 25, 20, 5, 8, 18, 12, 13, 14, 15, 16, 17, 21, 3, 4, 9]
history = []
swaps = 0
minFutureSwaps = 0
score = 0
swapLengthTotal = 0
totalManDist = 0
prQueue = []
archive = []

print "\n" + "Start: " + str(melanoStart)

# minimum future swaps
elements = 1
for a in range(len(melanoStart)):
	if a == 24:
		break
	if melanoStart[a] + 1 != melanoStart[a + 1] and melanoStart[a] - 1 != melanoStart [a + 1]:
		elements += 1
		
minFutureSwaps = elements / 2
print "Minimum Future Swaps: " + str(minFutureSwaps)

score = swaps + minFutureSwaps
print "Score: " + str(score)

# determine total manhattan distance of first array
for b in range(len(melanoStart)):
	totalManDist += abs(melanoStart.index(b + 1) - b)

print "Total Manhattan Distance: " + str(totalManDist) + "\n"
prQueue.append(Genome(melanoStart, history, totalManDist, swaps, minFutureSwaps, score, swapLengthTotal))

# make new objects until one object is fully sorted
while prQueue[0].minFutureSwaps != 0:
	
	# take array with best score so far
	melanoBest = prQueue[0]
	archive.append(melanoBest.array)
	myDeque = deque(prQueue)
	myDeque.popleft()
	prQueue = list(myDeque)
			
	print "Array: " + str(melanoBest.array)
	print "History: " + str(melanoBest.history)
	print "Total Manhattan Distance: " + str(melanoBest.totalManDist)
	print "Swaps: " + str(melanoBest.swaps)
	print "Minimum Future Swaps: " + str(melanoBest.minFutureSwaps)
	print "Score: " + str(melanoBest.score)
	print "Total Swap Length: " + str(melanoBest.swapLengthTotal) + "\n"
	
	melanoTuple = tuple(melanoBest.array)
	historyTuple = tuple(melanoBest.history)
	
	# iterate over all possible swaps
	for i in range(len(melanoBest.array)):
		if i == 24:
			break
		for j in range(len(melanoBest.array)):
			if i + j + 2 > 25:
				break
				
			melano = list(melanoTuple)
			addToHistory = list(historyTuple)
			addToHistory.append(melanoTuple)
			swaps = melanoBest.swaps
			swapLengthTotal = melanoBest.swapLengthTotal

			swapLengthTotal += len(melano[i:i + j + 2])
			melano[i:i + j + 2] = reversed(melano[i:i + j + 2])
			swaps += 1
			
			# compare array with archive
			for k in range(len(archive)):
				if cmp(melano, archive[k]) == 0:
					continue
					
			# determine total manhattan distance of new array
			totalManDist = 0
			for l in range(len(melano)):
				totalManDist += abs(melano.index(l + 1) - l)
			
			# determine minimum future swaps of new array
			elements = 1
			for m in range(len(melano)):
				if m == 24:
					break
				if melano[m] + 1 != melano[m + 1] and melano[m] - 1 != melano[m + 1]:
					elements += 1
					
			minFutureSwaps = elements / 2

			# determine score of new array
			score = swaps + minFutureSwaps

			# make object and put in right place of priority queue
			# if total manhattan distance is bigger than the last in queue, add object to the end
			if len(prQueue) == 0 or score >= prQueue[-1].score:
				prQueue.append(Genome(melano, addToHistory, totalManDist, swaps, minFutureSwaps, score, swapLengthTotal))
			else:
				# find the right place in queue
				pos = 0
				while prQueue[pos].score <= score:
					pos += 1
					
				# move old objects ON and AFTER right place by one to the right
				listLength = len(prQueue)
				prQueue.append(prQueue[listLength - 1])

				while listLength - 1 != pos:
					prQueue[listLength] = prQueue[listLength - 1]
					listLength -= 1
						
				# put new object on right place
				prQueue[pos] = Genome(melano, addToHistory, totalManDist, swaps, minFutureSwaps, score, swapLengthTotal)
				
print "---------------RESULT---------------"
print "Array: " + str(prQueue[0].array)
print "History: " + str(prQueue[0].history)
print "Total Manhattan Distance: " + str(prQueue[0].totalManDist)
print "Swaps: " + str(prQueue[0].swaps)
print "Minimum Future Swaps: " + str(prQueue[0].minFutureSwaps)
print "Score: " + str(prQueue[0].score)
print "Total Swap Length: " + str(prQueue[0].swapLengthTotal)