import random



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

# print de lijst van genomen met daar in lijsten van genen
for j in range(len(genomen)):
    FindAndSwap(genomen[j])
    j = j + 1
    

#########################################################################

genomen2 = []
i = 0    
    
while i < 2000:

    # genereer random genenset
    genenset2 = []
    genenset2 = random.sample(xrange(1, 26), 25)
    genomen2.append(genenset2)
    i = i + 1

# print de lijst van genomen met daar in lijsten van genen
for k in range(len(genomen2)):
    FindAndSwapReversed(genomen2[k])
    k = k + 1
    
    

#########################################################################

genomen3 = []
i = 0    
    
while i < 2000:

    # genereer random genenset
    genenset3 = []
    genenset3 = random.sample(xrange(1, 26), 25)
    genomen3.append(genenset3)
    i = i + 1

# print de lijst van genomen met daar in lijsten van genen
for k in range(len(genomen3)):
    FindAndSwapIterative(genomen3[k])
    k = k + 1
    









