# RandomSwapper sorts the array in a random way. If the begin and end numbers are in the right place
# then the algorithm keep them in place.

from random import randint

melano = [23, 1, 2, 11, 24, 22, 19, 6, 10, 7, 25, 20, 5, 8, 18, 12, 13, 14, 15, 16, 17, 21, 3, 4, 9]
miranda = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]

counter = 0
lowest = 0
highest = 25
totalManDist = 0

print "\n" + "Start: " + str(melano)

# determine total manhattan distance of numbers
for a in range(len(melano)):
	totalManDist += abs(melano.index(a + 1) - a)

print "Total Manhattan Distance: " + str(totalManDist) + "\n"

# swap till fully sorted
while melano != miranda:

	# if lowest number is in place, add 1 to lowest
	if melano[lowest] == lowest + 1:
		lowest = lowest + 1
		
	# if highest number is in place, subtract 1 from highest
	if melano[highest - 1] == highest:
		highest = highest - 1

	# determine swaplength
	j = randint(lowest,highest - 2)
	k = randint(j + 2, highest)

	# do swap, add 1 to counter
	print "Swap #" + str(counter + 1)
	print "Swap length: " + str(len(melano[j:k]))
	melano[j:k] = reversed(melano[j:k])
	print str(melano) + "\n"
	counter = counter + 1
	
print "Swaps: " + str(counter) + "\n"


	