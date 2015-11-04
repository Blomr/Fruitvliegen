# The next algorithm is the as the original FindandSwap.
# The only difference is that the sorting begins at the end of the list
# instead of at the begin.

melano = [23, 1, 2, 11, 24, 22, 19, 6, 10, 7, 25, 20, 5, 8, 18, 12, 13, 14, 15, 16, 17, 21, 3, 4, 9]
swaps = 0

#iterate over all numbers (from 24 to 0)
for i in range(len(melano) - 1, -1, -1):
	print "Replace: " + str(i + 1)

	# if number is already in position, continue
	if i + 1 == melano[i]:
		print "NO SWAP!\n"
		continue
		
	# if not, swap part of the list
	print "Swap length: " + str(len(melano[melano.index(i + 1):i + 1]))
	melano[melano.index(i + 1):i + 1] = reversed(melano[melano.index(i + 1):i + 1])
	swaps = swaps + 1
	print str(melano) + "\n"
	
print "---> Swaps: " + str(swaps)