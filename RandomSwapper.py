from random import randint

melano = [23, 1, 2, 11, 24, 22, 19, 6, 10, 7, 25, 20, 5, 8, 18, 12, 13, 14, 15, 16, 17, 21, 3, 4, 9]
miranda = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]

counter = 0

while melano != miranda:

	j = randint(0,23)
	k = randint(j + 2, 25)

	print "Swap #" + str(counter + 1)
	print "Swap length: " + str(len(melano[j:k]))
	melano[j:k] = reversed(melano[j:k])
	print str(melano) + "\n"
	counter = counter + 1
	
print "Swaps: " + str(counter) + "\n"
	