# The next algorithm searches for the highest number in the array (25).
# When it finds the number it inverses all numbers from the most right till the number itself.
# Now the numbers that are swapped are mirrored compared to their previous state.
# 25 is now in the right position. Now the algorithm searches for 24.
# When it is found, it repeats the process except that 25 stays in place.
# The algorithm is done when the whole array is sorted.

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

	#iterate over all numbers (from 24 to 0)
	for i in range(len(melano) - 1, -1, -1):
		print "Replace: " + str(i + 1)

		# if number is already in position, continue
		if i + 1 == melano[i]:
			print "NO SWAP!\n"
			
		# if not, swap part of the list
		else:
			swapLengthTotal += len(melano[melano.index(i + 1):i + 1])
			print "Swap length: " + str(len(melano[melano.index(i + 1):i + 1]))
			melano[melano.index(i + 1):i + 1] = reversed(melano[melano.index(i + 1):i + 1])
			swaps = swaps + 1
			print str(melano) + "\n"
		
	print "---> Swaps: " + str(swaps)
	print "---> Total swap length: " + str(swapLengthTotal)
	print "---> Average: " + str(swapLengthTotal / swaps) + " genes per swap"
	
sorting([23, 1, 2, 11, 24, 22, 19, 6, 10, 7, 25, 20, 5, 8, 18, 12, 13, 14, 15, 16, 17, 21, 3, 4, 9])