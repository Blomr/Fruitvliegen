# The next algorithm is the as the original FindandSwap.
# The only difference is that the sorting begins at the end of the list
# instead of at the begin.
from collections import deque

class Genome(object):
	def __init__(self, array, history, swaps, elements, score, swapLengthTotal):
		self.array = array
		self.history = history
		self.swaps = swaps
		self.elements = elements
		self.score = score
		self.swapLengthTotal = swapLengthTotal

def sorting(genome):		
	# initialize variables
	melanoStart = genome
	history = []
	swaps = 0
	startScore = 0
	swapLengthTotal = 0
	prQueue = []
	archive = dict()
	results = []

	print "\n" + "Start: " + str(melanoStart)

	# minimum future swaps
	elements = 1
	for a in range(len(melanoStart)):
		if a == 24:
			break
		if melanoStart[a] + 1 != melanoStart[a + 1] and melanoStart[a] - 1 != melanoStart[a + 1]:
			elements += 1

	startScore = swaps + elements
	print "Score: " + str(startScore) + "\n"

	archive[tuple(melanoStart)] = True
	prQueue.append(Genome(melanoStart, history, swaps, elements, startScore, swapLengthTotal))

	# make new objects until one object is fully sorted
	while len(prQueue) != 0:
		
		# take array with best score so far and put in archive
		melanoBest = prQueue[0]
		myDeque = deque(prQueue)
		myDeque.popleft()
		prQueue = list(myDeque)
				
		print "Array: " + str(melanoBest.array)
		print "History: " + str(melanoBest.history)
		print "Swaps: " + str(melanoBest.swaps)
		print "Elements: " + str(melanoBest.elements)
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

				# do swap and add to swapLengthTotal and swaps
				swapLengthTotal += len(melano[i:i + j + 2])
				melano[i:i + j + 2] = reversed(melano[i:i + j + 2])
				swaps += 1

				# compare array with archive
				inArchive = False
				if tuple(melano) not in archive:
					archive[tuple(melano)] = True
				else:
					inArchive = True
					
				# if not in archive, determine minimum future swaps of new array
				if inArchive == False:
					elements = 1
					for m in range(len(melano)):
						if m == 24:
							break
						if melano[m] + 1 != melano[m + 1] and melano[m] - 1 != melano[m + 1]:
							elements += 1

					# determine score of new array
					score = swaps + elements

					# make object and put in right place of priority queue
					# if score is bigger than the last in queue, add object to the end
					if score <= startScore:
						if elements == 1:
							results.append(Genome(melano, addToHistory, swaps, elements, score, swapLengthTotal))
						else:
							prQueue.append(Genome(melano, addToHistory, swaps, elements, score, swapLengthTotal))
					
	print "---------------RESULT---------------"
	for r in results:
		print "Array: " + str(r.array)
		print "History: " + str(r.history)
		print "Swaps: " + str(r.swaps)
		print "Elements: " + str(r.elements)
		print "Score: " + str(r.score)
		print "Total Swap Length: " + str(r.swapLengthTotal)
		
sorting([23, 1, 2, 11, 24, 22, 19, 6, 10, 7, 25, 20, 5, 8, 18, 12, 13, 14, 15, 16, 17, 21, 3, 4, 9])