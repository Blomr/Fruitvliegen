# The next algorithm looks like FindandSwap but the difference is
# that it first searches for the lowest number and after that for
# the highest. After that it searches for the second lowest and
# the second highest, etcetera.

def sorting(genome):
	melano = genome
	swaps = 0
	i = 0
	swapLengthTotal = 0
	done = False 
	totalManDist = 0

	print "\n" + "Start: " + str(melano)

	# determine total manhattan distance of numbers
	for a in range(len(melano)):
		totalManDist += abs(melano.index(a + 1) - a)

	print "Total Manhattan Distance: " + str(totalManDist) + "\n"

	while done == False:

		print "Replace: " + str(i + 1)
		if i + 1 == melano[i]:
			print "NO SWAP!\n"
		else:
			swapLengthTotal += len(melano[i:melano.index(i + 1) + 1])
			print "Swap length: " + str(len(melano[i:melano.index(i + 1) + 1]))
			melano[i:melano.index(i + 1) + 1] = reversed(melano[i:melano.index(i + 1) + 1])
			swaps = swaps + 1
			print str(melano) + "\n"
			
		print "Replace: " + str(25 - i)
		if 25 - i == melano[24 - i]:
			print "NO SWAP!\n"
		else:
			swapLengthTotal += len(melano[melano.index(25 - i):25 - i])
			print "Swap length: " + str(len(melano[melano.index(25 - i):25 - i]))
			melano[melano.index(25 - i):25 - i] = reversed(melano[melano.index(25 - i):25 - i])
			swaps = swaps + 1
			print str(melano) + "\n"
			
		if i == 12:
			print "---> Swaps: " + str(swaps)
			print "---> Total swap length: " + str(swapLengthTotal)
			print "---> Average: " + str(swapLengthTotal / swaps) + " genes per swap"
			done = True
			
		i = i + 1
		
sorting([23, 1, 2, 11, 24, 22, 19, 6, 10, 7, 25, 20, 5, 8, 18, 12, 13, 14, 15, 16, 17, 21, 3, 4, 9])