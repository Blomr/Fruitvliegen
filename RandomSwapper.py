from random import randint

melano = [23, 1, 2, 11, 24, 22, 19, 6, 10, 7, 25, 20, 5, 8, 18, 12, 13, 14, 15, 16, 17, 21, 3, 4, 9]

for i in range(5):

	j = randint(0,23)
	k = randint(j + 1, 25)

	print "Swap #" + str(i + 1)
	print "Swap length: " + str(len(melano[j:k]))
	melano[j:k] = reversed(melano[j:k])
	print str(melano) + "\n"
	