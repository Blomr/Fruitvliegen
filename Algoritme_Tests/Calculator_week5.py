import random
from copy import deepcopy


########################################################################
# FIND AND SWAP
########################################################################


def FindAndSwap(genoom):
    melano = genoom
    swaps = 0
    swapLengthTotal = 0

    #iterate over all numbers
    for i in range(len(melano)):

	    # if number is already in position, continue
	    if i + 1 == melano[i]:
		    continue
		
	    # if not, swap part of the list
	    swapLengthTotal += len(melano[i:melano.index(i + 1) + 1])
	    melano[i:melano.index(i + 1) + 1] = reversed(melano[i:melano.index(i + 1) + 1])
	    swaps = swaps + 1
	
    # schrijf mutaties per genoom naar file
    file = open("mutaties_alg1.txt", "a")
    file.write(str(swaps) + "\r\n")
    file.close()
    
    # schrijf totaal aantal genen verplaatst naar file
    file = open("totaalgenen_alg1.txt", "a")
    file.write(str(swapLengthTotal) + "\r\n")
    file.close()

    # schrijf gemiddelde grootte mutatie naar file
    file = open("gemgroottemutatie_alg1.txt", "a")
    file.write(str(swapLengthTotal / swaps) + "\r\n")
    file.close()


########################################################################
# FIND AND SWAP REVERSED
########################################################################

def FindAndSwapReversed(genoom):
    melano = genoom
    swaps = 0
    swapLengthTotal = 0

    #iterate over all numbers (from 24 to 0)
    for i in range(len(melano) - 1, -1, -1):

	    # if number is already in position, continue
	    if i + 1 == melano[i]:
		    continue
		
	    # if not, swap part of the list
	    swapLengthTotal += len(melano[melano.index(i + 1):i + 1])
	    melano[melano.index(i + 1):i + 1] = reversed(melano[melano.index(i + 1):i + 1])
	    swaps = swaps + 1
	
     # schrijf mutaties per genoom naar file
    file = open("mutaties_alg2.txt", "a")
    file.write(str(swaps) + "\r\n")
    file.close()
    
    # schrijf totaal aantal genen verplaatst naar file
    file = open("totaalgenen_alg2.txt", "a")
    file.write(str(swapLengthTotal) + "\r\n")
    file.close()

    # schrijf gemiddelde grootte mutatie naar file
    file = open("gemgroottemutatie_alg2.txt", "a")
    file.write(str(swapLengthTotal / swaps) + "\r\n")
    file.close()





########################################################################
# FIND AND SWAP ITERATIVE
########################################################################

def FindAndSwapIterative(genoom):
    melano = genoom
    swaps = 0
    i = 0
    swapLengthTotal = 0
    done = False 

    while done == False:

	    if (i + 1 == melano[i]) == False:
		    swapLengthTotal += len(melano[i:melano.index(i + 1) + 1])
		    melano[i:melano.index(i + 1) + 1] = reversed(melano[i:melano.index(i + 1) + 1])
		    swaps = swaps + 1
		
	    if (25 - i == melano[24 - i]) == False:
		    swapLengthTotal += len(melano[melano.index(25 - i):25 - i])
		    melano[melano.index(25 - i):25 - i] = reversed(melano[melano.index(25 - i):25 - i])
		    swaps = swaps + 1
		    
	    if i == 12:
		    done = True
		
	    i = i + 1
	    
	# schrijf mutaties per genoom naar file
    file = open("mutaties_alg3.txt", "a")
    file.write(str(swaps) + "\r\n")
    file.close()
    
    # schrijf totaal aantal genen verplaatst naar file
    file = open("totaalgenen_alg3.txt", "a")
    file.write(str(swapLengthTotal) + "\r\n")
    file.close()

    # schrijf gemiddelde grootte mutatie naar file
    file = open("gemgroottemutatie_alg3.txt", "a")
    file.write(str(swapLengthTotal / swaps) + "\r\n")
    file.close()
    
    
    
    
########################################################################
# FIND AND SWAP KEEP INTACT
########################################################################   
    
def FindAndSwapKeepChunk(genoom):
    melano = genoom
    swaps = 0
    swapLengthTotal = 0
    totalManDist = 0

    # determine total manhattan distance of numbers
    for a in range(len(melano)):
	    totalManDist += abs(melano.index(a + 1) - a)

    #iterate over all numbers
    for i in range(len(melano)):

	    # if number is already in position, continue
	    if i + 1 == melano[i]:
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
	    melano[i:melano.index(last) + 1] = reversed(melano[i:melano.index(last) + 1])
	    swaps = swaps + 1
	
	    # if last number is changed, do swap again to put numbers in the right place
	    if isOtherLast == True:
		    swapLengthTotal += len(melano[i:i + changeLast + 1])
		    melano[i:i + changeLast + 1] = reversed(melano[i:i + changeLast + 1])
		    swaps += 1

    # schrijf mutaties per genoom naar file
    file = open("mutaties_alg4.txt", "a")
    file.write(str(swaps) + "\r\n")
    file.close()
    
    # schrijf totaal aantal genen verplaatst naar file
    file = open("totaalgenen_alg4.txt", "a")
    file.write(str(swapLengthTotal) + "\r\n")
    file.close()

    # schrijf gemiddelde grootte mutatie naar file
    file = open("gemgroottemutatie_alg4.txt", "a")
    file.write(str(swapLengthTotal / swaps) + "\r\n")
    file.close()
    
    
    
########################################################################
# FIND AND SWAP OPTIMIZED
########################################################################    
    
def FindAndSwapOptimized(genoom):
    melano = genoom
    swaps = 0
    swapLengthTotal = 0
    lowestNumber = min(melano)
    highestNumber = max(melano)
    totalManDist = 0
    
    # determine total manhattan distance of numbers
    for a in range(len(melano)):
	    totalManDist += abs(melano.index(a + 1) - a)

    #iterate over all numbers
    for i in range(len(melano)):

	    while melano.index(highestNumber) == highestNumber - 1:
		    if highestNumber == lowestNumber:
			    break
		    highestNumber = highestNumber - 1
		
	    if melano[melano.index(highestNumber) + 1] == highestNumber - 1:
		    swapLengthTotal += len(melano[melano.index(highestNumber):highestNumber])
		    melano[melano.index(highestNumber):highestNumber] = reversed(melano[melano.index(highestNumber):highestNumber])
		    swaps = swaps + 1
		    	
	    # if number is already in position, continue
	    if i + 1 != melano[i]:
		    swapLengthTotal += len(melano[i:melano.index(i + 1) + 1])
		    melano[i:melano.index(i + 1) + 1] = reversed(melano[i:melano.index(i + 1) + 1])
		    swaps = swaps + 1
		        
    # schrijf mutaties per genoom naar file
    file = open("mutaties_alg5.txt", "a")
    file.write(str(swaps) + "\r\n")
    file.close()
    
    # schrijf totaal aantal genen verplaatst naar file
    file = open("totaalgenen_alg5.txt", "a")
    file.write(str(swapLengthTotal) + "\r\n")
    file.close()

    # schrijf gemiddelde grootte mutatie naar file
    file = open("gemgroottemutatie_alg5.txt", "a")
    file.write(str(swapLengthTotal / swaps) + "\r\n")
    file.close()
    

    
########################################################################
# FIND AND SWAP REVERSED OPTIMIZED
########################################################################   
		    
def FindAndSwapRevOptimized(genoom):
    melano = genoom
    swaps = 0
    swapLengthTotal = 0
    lowestNumber = min(melano)
    highestNumber = max(melano)
    totalManDist = 0

    # determine total manhattan distance of numbers
    for a in range(len(melano)):
	    totalManDist += abs(melano.index(a + 1) - a)

    # iterate over all numbers (from 24 to 0)
    for i in range(len(melano) - 1, -1, -1):

	    while melano.index(lowestNumber) == lowestNumber - 1:
		    if lowestNumber != highestNumber:
			    lowestNumber += 1
		    else:
			    break
	    if melano[melano.index(lowestNumber) - 1] == lowestNumber + 1:
		    swapLengthTotal += len(melano[lowestNumber - 1:melano.index(lowestNumber) + 1])
		    melano[lowestNumber - 1:melano.index(lowestNumber) + 1] = reversed(melano[lowestNumber - 1:melano.index(lowestNumber) + 1])
		    swaps = swaps + 1
		
		    while melano.index(lowestNumber) == lowestNumber - 1:
			    if lowestNumber == highestNumber:
				    break
			    lowestNumber = lowestNumber + 1

	    # if number is already in position, continue
	    if i + 1 != melano[i]:
		    swapLengthTotal += len(melano[melano.index(i + 1):i + 1])
		    melano[melano.index(i + 1):i + 1] = reversed(melano[melano.index(i + 1):i + 1])
		    swaps = swaps + 1
		        
     # schrijf mutaties per genoom naar file
    file = open("mutaties_alg6.txt", "a")
    file.write(str(swaps) + "\r\n")
    file.close()
    
    # schrijf totaal aantal genen verplaatst naar file
    file = open("totaalgenen_alg6.txt", "a")
    file.write(str(swapLengthTotal) + "\r\n")
    file.close()

    # schrijf gemiddelde grootte mutatie naar file
    file = open("gemgroottemutatie_alg6.txt", "a")
    file.write(str(swapLengthTotal / swaps) + "\r\n")
    file.close()


########################################################################
# RANDOM GENERATOR
########################################################################


# zet array klaar om de genomen in te stoppen
genomen = []
i = 0

while i < 2000:

    # genereer random genenset
    genenset = []
    genenset = random.sample(xrange(1, 26), 25)
    genomen.append(genenset)
    i = i + 1
    
genomen2 = deepcopy(genomen)
genomen3 = deepcopy(genomen)  
genomen4 = deepcopy(genomen)  
genomen5 = deepcopy(genomen)  
genomen6 = deepcopy(genomen) 


# print de lijst van genomen met daar in lijsten van genen
for j in range(len(genomen)):
    FindAndSwap(genomen[j])
    j = j + 1
        
for k in range(len(genomen2)):
    FindAndSwapReversed(genomen2[k])
    k = k + 1
    
for l in range(len(genomen3)):
    FindAndSwapIterative(genomen3[l])
    l = l + 1
     
for m in range(len(genomen4)):
    FindAndSwapKeepChunk(genomen4[m])
    m = m + 1
    
for n in range(len(genomen5)):
    FindAndSwapOptimized(genomen5[n])
    n = n + 1
    
for o in range(len(genomen6)):
    FindAndSwapRevOptimized(genomen6[o])
    o = o + 1


 
    









