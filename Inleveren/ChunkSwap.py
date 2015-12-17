# The next algorithm searches for numbers that forms chunks with other numbers.
# A chunk could be row of numbers that are incrementing of decrementing by 1.
# Like 9,10,11,12 or 7,6,5,4. If the algorithm wants to make a swap, it has to
# let the chunk intact and swap the whole chunk.

def sorting(genome):
	melano = genome
	swaps = 0
	swapLengthTotal = 0
	totalManDist = 0

	print "\n" + "Start: " + str(melano)

	# determine total manhattan distance of numbers
	for a in range(len(melano)):
		totalManDist += abs(melano.index(a + 1) - a)

	print "Total Manhattan Distance: " + str(totalManDist) + "\n"

	#iterate over all numbers
	for i in range(len(melano)):

		print "Replace: " + str(i + 1)

		# if number is already in position, continue
		if i + 1 == melano[i]:
			print "NO SWAP!\n"
			continue

		noLast = []

		# search for numbers that can't be the end of the swap
		for j in range(len(melano)):
			if j == 24:
				break
			if melano[j + 1] == melano[j] + 1:
				noLast.append(melano[j])
			if melano[j + 1] == melano[j] - 1:
				noLast.append(melano[j])

		print "noLast = " + str(noLast)
		
		isOtherLast = False
		
		# if the last number in the swap is in noLast, take the next number as last number
		last = i + 1
		changeLast = 0
		while last in noLast:
			last = last + 1
			changeLast = changeLast + 1
			isOtherLast = True
		
		# swap part of the list
		swapLengthTotal += len(melano[i:melano.index(last) + 1])
		print "Swap length: " + str(len(melano[i:melano.index(last) + 1]))
		melano[i:melano.index(last) + 1] = reversed(melano[i:melano.index(last) + 1])
		swaps = swaps + 1
		print str(melano) + "\n"
		
		# if last number is changed, do swap again to put numbers in the right place
		if isOtherLast == True:
			swapLengthTotal += len(melano[i:i + changeLast + 1])
			print "Swap length: " + str(len(melano[i:i + changeLast + 1]))
			melano[i:i + changeLast + 1] = reversed(melano[i:i + changeLast + 1])
			swaps += 1
			print str(melano) + "\n"
		
	print "---> Swaps: " + str(swaps)
	print "---> Total swap length: " + str(swapLengthTotal)
	print "---> Average: " + str(swapLengthTotal / swaps) + " genes per swap"
	
sorting([23, 1, 2, 11, 24, 22, 19, 6, 10, 7, 25, 20, 5, 8, 18, 12, 13, 14, 15, 16, 17, 21, 3, 4, 9])