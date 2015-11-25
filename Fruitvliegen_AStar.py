# The next algorithm is the as the original FindandSwap.
# The only difference is that the sorting begins at the end of the list
# instead of at the begin.

class Genome(object):
	array = []
	totalManDist = 0
	
	def __init__(self, array, totalManDist):
		self.array = array
		self.totalManDist = totalManDist
		

melanoStart = [23, 1, 2, 11, 24, 22, 19, 6, 10, 7, 25, 20, 5, 8, 18, 12, 13, 14, 15, 16, 17, 21, 3, 4, 9]
swaps = 0
swapLengthTotal = 0
totalManDist = 0
prQueue = []

print "\n" + "Start: " + str(melano)

# determine total manhattan distance of first array
for a in range(len(melanoStart)):
	totalManDist += abs(melanoStart.index(a + 1) - a)
	
	print str(a + 1) + ": " + str(abs(melanoStart.index(a + 1) - a))

print "Total Manhattan Distance: " + str(totalManDist) + "\n"
prQueue.append(Genome(melanoStart, totalManDist)

# make new objects until one object is fully sorted
while prQueue[0].totalManDist != 0:
	
	# take array with best manhattan distance so far
	melanoBest = prQueue[0].array
	
	# iterate over all possible swaps
	for i in range(len(melanoBest)):
		if i == 24:
			break
		for j in range(len(melanoBest)):
			melano = melanoBest
			if i + j + 2 > 25:
				break
			melano[i:i + j + 2] = reversed(melano[i:i + j + 2])
			print melano
			
			# determine total manhattan distance of new array
			totalManDist = 0
			for a in range(len(melano)):
				totalManDist += abs(melano.index(a + 1) - a)
			print "Total Manhattan Distance: " + str(totalManDist) + "\n"
			
			
			# make object and put in right place of priority queue
			# if queue is empty, add object
			if len(prQueue) == 0
				prQueue.append(Genome(melano, totalManDist))
			# if total manhattan distance is bigger than the last in queue, add object to the end
			elif totalManDist >= prQueue[-1].totalManDist:
				prQueue.append(Genome(melano, totalManDist))
			else:
				# find the right place
				i = 0
				while prQueue[i].totalManDist <= totalManDist:
					i += 1
					
				# move old objects ON and AFTER right place by one to the right
				listLength = len(prQueue)
				while listLength - 1 != i:
					if listLength == len(prQueue):
						prQueue.append(prQueue[listLength - 1])
						listLength -= 1
					else:
						prQueue[listLength] = prQueue[listLength - 1]
						listLength -= 1
						
				# put new object on right place
				prQueue[i] = Genome(melano, totalManDist)
			
		
