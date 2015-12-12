import random
from copy import deepcopy
from collections import deque


########################################################################
# FIND AND SWAP
########################################################################


def FindAndSwap(genoom):
    melano = genoom
    swaps = 0
    swapLengthTotal = 0
    
    elements = 1
    for a in range(len(melano)):
	if a == 24:
		break
	if melano[a] + 1 != melano[a + 1] and melano[a] - 1 != melano[a + 1]:
		elements += 1

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
    file = open("mutaties_alg1_r.txt", "a")
    file.write(str(swaps) + "\r\n")
    file.close()
    
    # schrijf totaal aantal genen verplaatst naar file
    file = open("totaalgenen_alg1_r.txt", "a")
    file.write(str(swapLengthTotal) + "\r\n")
    file.close()

    # schrijf gemiddelde grootte mutatie naar file
    file = open("gemgroottemutatie_alg1_r.txt", "a")
    file.write(str(swapLengthTotal / swaps) + "\r\n")
    file.close()
    
    # schrijf element score per ding naar file
    file = open("elementscore_alg1_r.txt", "a")
    file.write(str(elements) + "\r\n")
    file.close()


########################################################################
# FIND AND SWAP REVERSED
########################################################################

def FindAndSwapReversed(genoom):
    melano = genoom
    swaps = 0
    swapLengthTotal = 0
    
    elements = 1
    for a in range(len(melano)):
	if a == 24:
		break
	if melano[a] + 1 != melano[a + 1] and melano[a] - 1 != melano[a + 1]:
		elements += 1

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
    file = open("mutaties_alg2_r.txt", "a")
    file.write(str(swaps) + "\r\n")
    file.close()
    
    # schrijf totaal aantal genen verplaatst naar file
    file = open("totaalgenen_alg2_r.txt", "a")
    file.write(str(swapLengthTotal) + "\r\n")
    file.close()

    # schrijf gemiddelde grootte mutatie naar file
    file = open("gemgroottemutatie_alg2_r.txt", "a")
    file.write(str(swapLengthTotal / swaps) + "\r\n")
    file.close()
    
    # schrijf element score per ding naar file
    file = open("elementscore_alg2_r.txt", "a")
    file.write(str(elements) + "\r\n")
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
    
    elements = 1
    for a in range(len(melano)):
	if a == 24:
		break
	if melano[a] + 1 != melano[a + 1] and melano[a] - 1 != melano[a + 1]:
		elements += 1

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
    file = open("mutaties_alg3_r.txt", "a")
    file.write(str(swaps) + "\r\n")
    file.close()
    
    # schrijf totaal aantal genen verplaatst naar file
    file = open("totaalgenen_alg3_r.txt", "a")
    file.write(str(swapLengthTotal) + "\r\n")
    file.close()

    # schrijf gemiddelde grootte mutatie naar file
    file = open("gemgroottemutatie_alg3_r.txt", "a")
    file.write(str(swapLengthTotal / swaps) + "\r\n")
    file.close()
    
    # schrijf element score per ding naar file
    file = open("elementscore_alg3_r.txt", "a")
    file.write(str(elements) + "\r\n")
    file.close()
    
    
    
    
########################################################################
# FIND AND SWAP KEEP INTACT
########################################################################   
    
def FindAndSwapKeepChunk(genoom):
    melano = genoom
    swaps = 0
    swapLengthTotal = 0
    totalManDist = 0
    
    elements = 1
    for a in range(len(melano)):
	if a == 24:
		break
	if melano[a] + 1 != melano[a + 1] and melano[a] - 1 != melano[a + 1]:
		elements += 1

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
    file = open("mutaties_alg4_r.txt", "a")
    file.write(str(swaps) + "\r\n")
    file.close()
    
    # schrijf totaal aantal genen verplaatst naar file
    file = open("totaalgenen_alg4_r.txt", "a")
    file.write(str(swapLengthTotal) + "\r\n")
    file.close()

    # schrijf gemiddelde grootte mutatie naar file
    file = open("gemgroottemutatie_alg4_r.txt", "a")
    file.write(str(swapLengthTotal / swaps) + "\r\n")
    file.close()
    
    # schrijf element score per ding naar file
    file = open("elementscore_alg4_r.txt", "a")
    file.write(str(elements) + "\r\n")
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
    
    elements = 1
    for a in range(len(melano)):
	if a == 24:
		break
	if melano[a] + 1 != melano[a + 1] and melano[a] - 1 != melano[a + 1]:
		elements += 1
    
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
    file = open("mutaties_alg5_r.txt", "a")
    file.write(str(swaps) + "\r\n")
    file.close()
    
    # schrijf totaal aantal genen verplaatst naar file
    file = open("totaalgenen_alg5_r.txt", "a")
    file.write(str(swapLengthTotal) + "\r\n")
    file.close()

    # schrijf gemiddelde grootte mutatie naar file
    file = open("gemgroottemutatie_alg5_r.txt", "a")
    file.write(str(swapLengthTotal / swaps) + "\r\n")
    file.close()
    
    # schrijf element score per ding naar file
    file = open("elementscore_alg5_r.txt", "a")
    file.write(str(elements) + "\r\n")
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
    
    elements = 1
    for a in range(len(melano)):
	if a == 24:
		break
	if melano[a] + 1 != melano[a + 1] and melano[a] - 1 != melano[a + 1]:
		elements += 1

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
    file = open("mutaties_alg6.txt_r", "a")
    file.write(str(swaps) + "\r\n")
    file.close()
    
    # schrijf totaal aantal genen verplaatst naar file
    file = open("totaalgenen_alg6_r.txt", "a")
    file.write(str(swapLengthTotal) + "\r\n")
    file.close()

    # schrijf gemiddelde grootte mutatie naar file
    file = open("gemgroottemutatie_alg6_r.txt", "a")
    file.write(str(swapLengthTotal / swaps) + "\r\n")
    file.close()
    
    # schrijf element score per ding naar file
    file = open("elementscore_alg6_r.txt", "a")
    file.write(str(elements) + "\r\n")
    file.close()






def AStarElements(genoom):
    class Genome(object):
        array = []
        history = []
        swaps = 0
        elements = 0
        score = 0
        swapLengthTotal = 0
	
	def __init__(self, array, history, swaps, elements, score, swapLengthTotal):
	    self.array = array
	    self.history = history
	    self.swaps = swaps
	    self.elements = elements
	    self.score = score
	    self.swapLengthTotal = swapLengthTotal
		
    # initialize variables
    melanoStart = genoom
    #melanoStart = [1, 23, 2, 11, 24, 22, 21, 6, 10, 25, 7, 20, 9, 8, 18, 13, 12, 14, 15, 16, 17, 3, 19, 4, 5]
    history = []
    swaps = 0
    score = 0
    swapLengthTotal = 0
    prQueue = []
    prQueueScore = []
    archive = dict()
    print "Initialized variables" 

    # minimum future swaps
    elements = 1
    for a in range(len(melanoStart)):
	    if a == 24:
		    break
	    if melanoStart[a] + 1 != melanoStart[a + 1] and melanoStart[a] - 1 != melanoStart[a + 1]:
		    elements += 1

    score = swaps + elements
    startelements = elements
    print "Calculated minimum amount of swaps" 

    archive[tuple(melanoStart)] = True
    prQueue.append(Genome(melanoStart, history, swaps, elements, score, swapLengthTotal))
    prQueueScore.append(score)

    # make new objects until one object is fully sorted
    while prQueue[0].elements != 1:
	
	    # take array with best score so far and put in archive
	    melanoBest = prQueue[0]
	    myDeque = deque(prQueue)
	    myDeque.popleft()
	    prQueue = list(myDeque)
	
	    scoreBest = prQueueScore[0]
	    myScoreDeque = deque(prQueueScore)
	    myScoreDeque.popleft()
	    prQueueScore = list(myScoreDeque)
	
	    melanoTuple = tuple(melanoBest.array)
	    historyTuple = tuple(melanoBest.history)
	
	    # iterate over all possible swaps
	    for i in range(len(melanoBest.array)):
		    if i == 24:
			    break
		    for j in range(len(melanoBest.array)):
			    if i + j + 2 > 25:
				    break
				
			    melano = list(melanoTuple)
			    addToHistory = list(historyTuple)
			    addToHistory.append(melanoTuple)
			    swaps = melanoBest.swaps
			    swapLengthTotal = melanoBest.swapLengthTotal

			    # do swap and add to swapLengthTotal and swaps
			    swapLengthTotal += len(melano[i:i + j + 2])
			    melano[i:i + j + 2] = reversed(melano[i:i + j + 2])
			    swaps += 1

			    # compare array with archive
			    inArchive = False
			    if tuple(melano) not in archive:
				    archive[tuple(melano)] = True
			    else:
				    inArchive = True
				
			    # if not in archive, determine minimum future swaps of new array
			    if inArchive == False:
				    elements = 1
				    for m in range(len(melano)):
					    if m == 24:
						    break
					    if melano[m] + 1 != melano[m + 1] and melano[m] - 1 != melano[m + 1]:
						    elements += 1

				    # determine score of new array
				    score = swaps + elements

				    # make object and put in right place of priority queue
				    # if score is bigger than the last in queue, add object to the end
				    if len(prQueue) == 0 or score >= prQueue[-1].score:
					    prQueueScore.append(score)
					    prQueue.append(Genome(melano, addToHistory, swaps, elements, score, swapLengthTotal))
				    # else, find the right place in queue and insert
				    else:
					    placeInQueue = prQueueScore.index(score + 1)
					    prQueueScore.insert(placeInQueue, score)
					    prQueue.insert(placeInQueue, Genome(melano, addToHistory, swaps, elements, score, swapLengthTotal))

    # schrijf mutaties per genoom naar file
    file = open("mutaties_alg7.txt_r", "a")
    file.write(str(swaps) + "\r\n")
    file.close()
    
    # schrijf totaal aantal genen verplaatst naar file
    file = open("totaalgenen_alg7_r.txt", "a")
    file.write(str(swapLengthTotal) + "\r\n")
    file.close()

    # schrijf gemiddelde grootte mutatie naar file
    file = open("gemgroottemutatie_alg7_r.txt", "a")
    file.write(str(swapLengthTotal / swaps) + "\r\n")
    file.close()
    
    # schrijf element score per ding naar file
    file = open("elementscore_alg7_r.txt", "a")
    file.write(str(startelements) + "\r\n")
    file.close()

    print "done"


########################################################################
# RANDOM GENERATOR
########################################################################


# zet array klaar om de genomen in te stoppen
genomen2 = []
i = 0

while i < 100:

    # genereer random genenset die relatief goed staat
    genenset_deel1 = []
    genenset_deel2 = []
    genenset_deel1 = random.sample(xrange(1, 13), 12)
    genenset_deel2 = random.sample(xrange(13, 26), 13)
    genenset_compleet = []
    genenset_compleet = genenset_deel1 + genenset_deel2
    
    
    # genereer volledig random genenset
    genenset = []
    genenset = random.sample(xrange(1, 26), 25)
    
    # gebruik genenset of genenset compleet
    genomen2.append(genenset)
    i = i + 1
    
    
# copy genomes so every algorithm has the same set    
genomen_2 = deepcopy(genomen2)
genomen_3 = deepcopy(genomen2)  
genomen_4 = deepcopy(genomen2)  
genomen_5 = deepcopy(genomen2)  
genomen_6 = deepcopy(genomen2)
genomen_7 = deepcopy(genomen2) 

for p in range(len(genomen_7)):
    AStarElements(genomen_7[p])
    p = p + 1

print "7 done"
 
    









