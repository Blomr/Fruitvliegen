# The next algorithm is the as the original FindandSwap.
# The only difference is that the sorting begins at the end of the list
# instead of at the begin.

class Genome(object):
	array = []
	totalManDist = 0
	
	def __init__(self, array, totalManDist):
		self.array = array
		self.totalManDist = totalManDist
		
def makeGenome(array, totalManDist):
	genome = Genome(array, totalManDist)
	return genome

melano = [23, 1, 2, 11, 24, 22, 19, 6, 10, 7, 25, 20, 5, 8, 18, 12, 13, 14, 15, 16, 17, 21, 3, 4, 9]
swaps = 0
swapLengthTotal = 0
totalManDist = 0

print "\n" + "Start: " + str(melano)

# determine total manhattan distance of numbers
for a in range(len(melano)):
	totalManDist += abs(melano.index(a + 1) - a)
	
	print str(a + 1) + ": " + str(abs(melano.index(a + 1) - a))

print "Total Manhattan Distance: " + str(totalManDist) + "\n"


for i in range(len(melano)):
	if i == 24:
		break
	for j in range(len(melano)):
		melano = [23, 1, 2, 11, 24, 22, 19, 6, 10, 7, 25, 20, 5, 8, 18, 12, 13, 14, 15, 16, 17, 21, 3, 4, 9]
		if i + j + 2 > 25:
			break
		melano[i:i + j + 2] = reversed(melano[i:i + j + 2])
		print melano
		
		totalManDist = 0
		for a in range(len(melano)):
			totalManDist += abs(melano.index(a + 1) - a)
		print "Total Manhattan Distance: " + str(totalManDist) + "\n"
		
