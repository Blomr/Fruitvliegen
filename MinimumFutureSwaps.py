melanoStart = [23, 1, 2, 11, 24, 22, 19, 6, 10, 7, 25, 20, 5, 8, 18, 12, 13, 14, 15, 16, 17, 21, 3, 4, 9]

# Minimum Future Swaps
counter = 1
for i in range(len(melanoStart)):
	if i == 24:
		break
	if melanoStart[i] + 1 != melanoStart[i + 1] and melanoStart[i] - 1 != melanoStart [i + 1]:
		counter += 1
		
print "Number groups:"
print counter
print "Minimum future swaps:"
print counter / 2
