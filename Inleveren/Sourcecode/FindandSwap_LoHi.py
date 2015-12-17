# The next algorithm searches for the lowest number in the array (1).
# When it finds the number it inverses all numbers from the most left till the number itself.
# Now the numbers that are swapped are mirrored compared to their previous state.
# 1 is now in the right position. Now the algorithm searches for 25.
# When it is found, it repeats the process except that 1 stays in place.
# After 25, the algorithm searches for 2, than 24 etcetera.
# The algorithm is done when the whole array is sorted.

def sorting(genome):
	melano = genome
	swaps = 0
	i = 0
	swapLengthTotal = 0
	done = False 

	print "\n" + "Start: " + str(melano)

	# run algorithm until array is sorted
	while done == False:

		# replace number at left side
		print "Replace: " + str(i + 1)
		
		# if number is already in the right place, go to next number
		if i + 1 == melano[i]:
			print "NO SWAP!\n"
		else:
			# do inversion, add swaplength to swapLengthTotal and add 1 to swaps
			swapLengthTotal += len(melano[i:melano.index(i + 1) + 1])
			print "Swap length: " + str(len(melano[i:melano.index(i + 1) + 1]))
			melano[i:melano.index(i + 1) + 1] = reversed(melano[i:melano.index(i + 1) + 1])
			swaps = swaps + 1
			print str(melano) + "\n"
			
		# replace number at right side
		print "Replace: " + str(25 - i)
		
		# if number is already in the right place, go to next number
		if 25 - i == melano[24 - i]:
			print "NO SWAP!\n"
		else:
			# do inversion, add swaplength to swapLengthTotal and add 1 to swaps
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