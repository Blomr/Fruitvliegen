########################################################################
# ASTER TOTALEGENEN
########################################################################

def totalGenes(genome):

	class Genome(object):
	    
	    def __init__(self, array, history, swaps, elements, swapLengthTotal):
		    self.array = array
		    self.history = history
		    self.swaps = swaps
		    self.elements = elements
		    self.swapLengthTotal = swapLengthTotal

	# initialize variables
	melanoStart = genome
	history = []
	swaps = 0
	swapLengthTotal = 0
	prQueue1 = []
	prQueue2 = []
	prQueue1Score = []
	prQueue2Score = []
	archive = dict()

	# minimum future swaps
	elements = 1
	for a in range(len(melanoStart)):
		if a == 24:
			break
		if melanoStart[a] + 1 != melanoStart[a + 1] and melanoStart[a] - 1 != melanoStart[a + 1]:
			elements += 1

	archive[tuple(melanoStart)] = True
	prQueue1.append(Genome(melanoStart, history, swaps, elements, swapLengthTotal))
	prQueue1Score.append(swapLengthTotal)

	# make new objects until one object is fully sorted
	while prQueue1[0].elements != 1:
		
		# take array with best score so far and put in archive
		if len(prQueue2) != 0:
			melanoBest = prQueue2[0]
			scoreBest = prQueue2Score[0]
		else:
			melanoBest = prQueue1[0]
			scoreBest = prQueue1Score[0]
			
		prQueue2 = []
		prQueue1 = []
		prQueue2Score = []
		prQueue1Score = []
		
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
				swapLength = len(melano[i:i + j + 2])
				swapLengthTotal += len(melano[i:i + j + 2])
				melano[i:i + j + 2] = reversed(melano[i:i + j + 2])
				swaps += 1

				# if not in archive, determine elements of new array
				elements = 1
				for m in range(len(melano)):
					if m == 24:
						break
					if melano[m] + 1 != melano[m + 1] and melano[m] - 1 != melano[m + 1]:
						elements += 1
				#print elements
					
				gate2 = False
				gate1 = False
				elementShrink = False
				if elements < melanoBest.elements:
					elementShrink = True
					if melanoBest.elements - elements == 2:
						gate2 = True
					else:
						gate1 = True
					
				# compare array with archive, if amount of elements shrinked
				inArchive = True
				if elementShrink == True:
					if tuple(melano) not in archive:
						archive[tuple(melano)] = True
						inArchive = False
					
				# if not in archive, put in queue
				if inArchive == False:
					# determine score of new array
					#score = swaps + elements
					if gate2 == True:
						# make object and put in right place of priority queue
						# if score is bigger than the last in queue, add object to the end
						if len(prQueue2) == 0 or swapLength >= prQueue2Score[-1]:
							prQueue2Score.append(swapLength)
							prQueue2.append(Genome(melano, addToHistory, swaps, elements, swapLengthTotal))
						# else, find the right place in queue and insert
						else:
							k = 1
							while swapLength + k not in prQueue2Score:
								k += 1
							placeInQueue = prQueue2Score.index(swapLength + k)
							prQueue2Score.insert(placeInQueue, swapLength)
							prQueue2.insert(placeInQueue, Genome(melano, addToHistory, swaps, elements, swapLengthTotal))
						gate2 = False
							
					else:
						# make object and put in right place of priority queue
						# if score is bigger than the last in queue, add object to the end
						if len(prQueue1) == 0 or swapLength >= prQueue1Score[-1]:
							prQueue1Score.append(swapLength)
							prQueue1.append(Genome(melano, addToHistory, swaps, elements, swapLengthTotal))
						# else, find the right place in queue and insert
						else:
							k = 1
							while swapLength + k not in prQueue1Score:
								k += 1
							placeInQueue = prQueue1Score.index(swapLength + k)
							prQueue1Score.insert(placeInQueue, swapLength)
							prQueue1.insert(placeInQueue, Genome(melano, addToHistory, swaps, elements, swapLengthTotal))
						
                        gate1 = False

    # schrijf mutaties per genoom naar file
    file = open("mutaties_alg9_re.txt", "a")
    file.write(str(swaps) + "\r\n")
    file.close()
    
    # schrijf totaal aantal genen verplaatst naar file
    file = open("totaalgenen_alg9_re.txt", "a")
    file.write(str(swapLengthTotal) + "\r\n")
    file.close()

    # schrijf gemiddelde grootte mutatie naar file
    file = open("gemgroottemutatie_alg9_re.txt", "a")
    file.write(str(swapLengthTotal / swaps) + "\r\n")
    file.close()
    
    # schrijf element score per ding naar file
    file = open("elementscore_alg9_re.txt", "a")
    file.write(str(startelements) + "\r\n")
    file.close()



# zet array klaar om de genomen in te stoppen
genomen2 = []
i = 0

while i < 2000:

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
    genomen2.append(genenset_compleet)
    i = i + 1
    
    
# copy genomes so every algorithm has the same set    
genomen_6 = deepcopy(genomen2)


for q in range(len(genomen_6)):
    totalGenes(genomen_6[q])
    q = q + 1
