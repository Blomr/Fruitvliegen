# The next algorithm searches for inversions whereby the amount of
# elements shrinks. Shrinks of 1 and 2 are collected in two different
# queues. The next algorithm chooses the shortest inversion of shrink 2.
# if this queue is empty the algorithm chooses the shortest inversion of
# shrink 1. Then it will make the next 300 inversions and chooses the
# next shortest inversion.

from collections import deque

class Genome(object):
	def __init__(self, array, history, swaps, elements, swapLengthTotal):
		self.array = array
		self.history = history
		self.swaps = swaps
		self.elements = elements
		self.swapLengthTotal = swapLengthTotal
		
def sorting(genome):
	# initialize variables
	melanoStart = genome
	history = []
	swaps = 0
	swapLengthTotal = 0
	prQueue1 = []
	prQueue2 = []
	prQueue1Score = []
	prQueue2Score = []
	archive = dict()
	result = 0

	print "\n" + "Start: " + str(melanoStart)

	# count elements of start genome
	elements = 1
	for a in range(len(melanoStart)):
		if a == 24:
			break
		if melanoStart[a] + 1 != melanoStart[a + 1] and melanoStart[a] - 1 != melanoStart[a + 1]:
			elements += 1

	archive[tuple(melanoStart)] = True
	prQueue1.append(Genome(melanoStart, history, swaps, elements, swapLengthTotal))
	prQueue1Score.append(swapLengthTotal)

	# make new objects until one object is fully sorted
	while result == 0:
		
		# take shortest swap from prQueue2, else shortest swap from prQueue1
		if len(prQueue2) != 0:
			melanoBest = prQueue2[0]
			scoreBest = prQueue2Score[0]
		else:
			melanoBest = prQueue1[0]
			scoreBest = prQueue1Score[0]
			
		# make priority queues empty
		prQueue2 = []
		prQueue1 = []
		prQueue2Score = []
		prQueue1Score = []

		print "Array: " + str(melanoBest.array)
		print "History: " + str(melanoBest.history)
		print "Swaps: " + str(melanoBest.swaps)
		print "Elements: " + str(melanoBest.elements)
		print "Total Swap Length: " + str(melanoBest.swapLengthTotal) 
		print "Last Swap: " + str(scoreBest) + "\n"
		
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
				swapLength = len(melano[i:i + j + 2])
				swapLengthTotal += len(melano[i:i + j + 2])
				melano[i:i + j + 2] = reversed(melano[i:i + j + 2])
				swaps += 1

				# count elements of new array
				elements = 1
				for m in range(len(melano)):
					if m == 24:
						break
					if melano[m] + 1 != melano[m + 1] and melano[m] - 1 != melano[m + 1]:
						elements += 1
					
				# put in queue1 or queue2 if amount of elements is less than parent
				putInQueue2 = False
				putInQueue1 = False
				elementShrink = False
				if elements < melanoBest.elements:
					elementShrink = True
					if melanoBest.elements - elements == 2:
						putInQueue2 = True
					else:
						putInQueue1 = True
					
				# compare array with archive, if amount of elements shrinked
				inArchive = True
				if elementShrink == True:
					if tuple(melano) not in archive:
						archive[tuple(melano)] = True
						inArchive = False
					
				# if not in archive, put in queue
				if inArchive == False:
					# if elements shrinked by 2
					if putInQueue2 == True:
						# if score is bigger than the last in queue, add object to the end
						if len(prQueue2) == 0 or swapLength >= prQueue2Score[-1]:
							prQueue2Score.append(swapLength)
							prQueue2.append(Genome(melano, addToHistory, swaps, elements, swapLengthTotal))
						# else, find the right place in queue and insert
						else:
							k = 1
							while swapLength + k not in prQueue2Score:
								k += 1
							placeInQueue = prQueue2Score.index(swapLength + k)
							prQueue2Score.insert(placeInQueue, swapLength)
							prQueue2.insert(placeInQueue, Genome(melano, addToHistory, swaps, elements, swapLengthTotal))
						putInQueue2 = False
						
					# if elements shrinked by 1
					else:
						# if score is bigger than the last in queue, add object to the end
						if len(prQueue1) == 0 or swapLength >= prQueue1Score[-1]:
							prQueue1Score.append(swapLength)
							prQueue1.append(Genome(melano, addToHistory, swaps, elements, swapLengthTotal))
						# else, find the right place in queue and insert
						else:
							k = 1
							while swapLength + k not in prQueue1Score:
								k += 1
							placeInQueue = prQueue1Score.index(swapLength + k)
							prQueue1Score.insert(placeInQueue, swapLength)
							prQueue1.insert(placeInQueue, Genome(melano, addToHistory, swaps, elements, swapLengthTotal))
						putInQueue1 = False
			
		# if an object has only 1 element, stop algorithm
		if len(prQueue2) != 0:
			if prQueue2[0].elements == 1:
				result = 2
				break;
		if len(prQueue1) != 0:
			if prQueue1[0].elements == 1:
				result = 1
				break;

	if result == 2:
		print "---------------RESULT---------------"
		print "Array: " + str(prQueue2[0].array)
		print "History: " + str(prQueue2[0].history)
		print "Swaps: " + str(prQueue2[0].swaps)
		print "Elements: " + str(prQueue2[0].elements)
		print "Total Swap Length: " + str(prQueue2[0].swapLengthTotal)
		print "Last Swap: " + str(prQueue2Score[0])
	if result == 1:
		print "---------------RESULT---------------"
		print "Array: " + str(prQueue1[0].array)
		print "History: " + str(prQueue1[0].history)
		print "Swaps: " + str(prQueue1[0].swaps)
		print "Elements: " + str(prQueue1[0].elements)
		print "Total Swap Length: " + str(prQueue1[0].swapLengthTotal)
		print "Last Swap: " + str(prQueue1Score[0])
	

sorting([23, 1, 2, 11, 24, 22, 19, 6, 10, 7, 25, 20, 5, 8, 18, 12, 13, 14, 15, 16, 17, 21, 3, 4, 9])