# The next algorithm searches for the lowest number in the array (1).
# When it finds the number it inverses all numbers from the most left till the number itself.
# Now the numbers that are swapped are mirrored compared to their previous state.
# 1 is now in the right position. Now the algorithm searches for 2.
# When it is found, it repeats the process except that 1 stays in place.
# The algorithm is done when the whole array is sorted.

melano = [23, 1, 2, 11, 24, 22, 19, 6, 10, 7, 25, 20, 5, 8, 18, 12, 13, 14, 15, 16, 17, 21, 3, 4, 9]
swaps = 0

#iterate over all numbers
for i in range(len(melano)):

	# if number is already in position, continue
	if i + 1 == melano[i]:
		print "NO SWAP!"
		continue
		
	# if not, swap part of the list
	melano[i:melano.index(i + 1) + 1] = reversed(melano[i:melano.index(i + 1) + 1])
	swaps = swaps + 1
	print melano
	
print "swaps: " + str(swaps)