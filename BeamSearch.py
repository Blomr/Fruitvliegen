from collections import defaultdict
from copy import deepcopy

"""
Gets a single list and performs every possible inversion with it appending every result of 
the inversions in a list that gets passed back. with a list of 25 numbers there will be 300 results.
"""
def getAllInversions(alist):
    queue = []
    count = 0
    for i in range(len(alist)):
        for j in range(i + 1, len(alist)):
            blist = deepcopy(alist)
            blist[i:j+1] = reversed(blist[i:j+1])
            queue.append(blist)
            count += 1     
    return queue
     
"""
score version 1.
Gives a point for every number inside a chunk, and divides it by the number of elements 
(single numbers and amount of chunnks).
"""     
def getScoreFromChunks(alist):
    counter = 0
    elements = 0
    chunklength = 0
    score = 0
    biggestChunk = 0
    
    for i in range(len(alist)):
        # looks if last number is part of a chunk, otherwise he ocasionally ignores those.
        if alist[i] == alist[-1]:
            if alist[i-1] == alist[i]-1 or alist[i-1] == alist[i]+1:
                counter += 1
        
        # looks for positive chunks
        if alist[(i+1)% len(alist)] == alist[i]+1 or alist[(i-1)% len(alist)] == alist[i]-1:

            #represents te size of the chunk
            chunklength += 1
            # if last number of chunk is reached, count the the chunk as element
            if alist[(i+1)% len(alist)] != alist[i]+1:
                # ignores last number if part of chunk as its already counted
                if alist[i] == alist[-1]:
                    break
                    
                counter += 1

        # looks for negative chunks
        elif alist[(i+1)% len(alist)] == alist[i]-1 or alist[(i-1)% len(alist)] == alist[i]+1:
            chunklength += 1
            # if last number of chunk is reached, count the the chunk as element
            if alist[(i+1)% len(alist)] != alist[i]-1:
                # ignores last number if part of chunk as its already counted
                if alist[i] == alist[-1]:
                    break
        
                counter += 1
        # counts single numbers as elements
        else :
            counter += 1

    elements = counter 
    score = chunklength / elements
    return score
    
"""
score version 2.
Gives a point for every number inside a chunk bigger than 2 numbers, and divides it by the number of elements 
(single numbers and amount of chunnks).
"""       
def getScoreFromBigChunks(alist):
    counter = 0
    extraPoints = 0
    extraScoreCounter = 0
    elements = 0
    chunklength = 0
    score = 0
    biggestChunk = 0
    
    for i in range(len(alist)):
        # looks if last number is part of a chunk, otherwise he ocasionally ignores those.
        if alist[i] == alist[-1]:
            if alist[i-1] == alist[i]-1 or alist[i-1] == alist[i]+1:
                counter += 1
                extraScoreCounter = 0
        # looks for positive chunks
        if alist[(i+1)% len(alist)] == alist[i]+1 or alist[(i-1)% len(alist)] == alist[i]-1:
            #represents te size of the chunk
            chunklength += 1
            
            # if the chunk is bigger than two numbers it get an extra point per number
            extraScoreCounter += 1
            if extraScoreCounter > 2:
                extraPoints += 1
            
            # if last number of chunk is reached, count the the chunk as element
            if alist[(i+1)% len(alist)] != alist[i]+1:
                # ignores last number if part of chunk as its already counted
                if alist[i] == alist[-1]:
                    continue
                    
                counter += 1
                extraScoreCounter = 0
        # looks for negative chunks
        elif alist[(i+1)% len(alist)] == alist[i]-1 or alist[(i-1)% len(alist)] == alist[i]+1:
            chunklength += 1
            
            # if the chunk is bigger than two numbers it get an extra point per number
            extraScoreCounter += 1
            if extraScoreCounter > 2:
                extraPoints =+ 1
            
            # if last number of chunk is reached, count the the chunk as element
            if alist[(i+1)% len(alist)] != alist[i]-1:
                # ignores last number if part of chunk as its already counted
                if alist[i] == alist[-1]:
                    continue
                counter += 1
                extraScoreCounter = 0
        # counts single numbers as elements
        else :
            counter += 1

    elements = counter 
    score = (chunklength / elements) + extraPoints
    return score

"""
score version 3.
gives a negative point for every step a number is away from its right place 
"""
def getScoreFromPosition(alist):
    addScore = 0
    score = 0 
    for i in alist:
        addScore = i - alist[i-1]
        if addScore > 0:
            addScore = addScore - (addScore * 2)
            
        score += addScore
    return score
    
"""
Iterates trough the given 300 lists creating 90000 results, and searches trough those creating 27 milion results.
The best result out of those 27 milion is chosen to return. 
"""
def threeLayerSearch(layerOne):
    # initiate necisary values
    countk = 0
    endResult = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
    tempLayerTwo = []
    tempLayerThree = []
    repLayerOne = []
    repLayerTwo = []
    repLayerTrhee = []
    repInversionLeni = 0
    repInversionLenj = 0
    repInversionLenm = 0
    highestScore = -1000
    currentScore = 0
    inversionLeni = 1
    inversionEndi = 25

    # iterate trough every element in given list (layer one 300 elements)
    for i in layerOne:
        # keeps track of the inversion length of every executed inversion in layer one
        inversionLeni += 1
        if inversionLeni > inversionEndi:
            inversionEndi -= 1
            inversionLeni = 2
        # prints results and returns if end result is found
        if i == endResult:
            print("\n",i, inversionLeni)
            return i
        # fills a list with 300 result from the i'th list in layer one (300 times 300 is 90000 results)
        templayerTwo = getAllInversions(i)
        # sets the inversion length of layer two back at the beginning of a new iteration.
        inversionLenj = 1
        inversionEndj = 25
        # iterate trough every result from temporary layer two (layer two)
        for j in templayerTwo:
            # keeps track of the inversion length of every executed inversion in layer two
            inversionLenj += 1
            if inversionLenj > inversionEndj:
                inversionEndj -= 1
                inversionLenj = 2
            # prints results and returns if end result is found
            if j == endResult:
                print("\n",i,inversionLeni, "\n",j, inversionLenj)
                return j
            # fills a list with 300 results from the j'th list in layer two (90000 times 300 is 27 million results)   
            tempLayerThree = getAllInversions(j)
            # sets the inversion length of layer three back at the beginning of a new iteration.
            inversionLenm = 1
            inversionEndm = 25
            # iterate trough every result from temporary layer three (layer three)
            for m in tempLayerThree:
                # keeps track of the inversion length of every executed inversion in layer three
                inversionLenm += 1
                if inversionLenm > inversionEndm:
                    inversionEndm -= 1
                    inversionLenm = 2
                # saves the best out of 27000000                   
                currentScore = getScoreFromPosition(m)
                if currentScore > highestScore:
                    highestScore = currentScore
                    repLayerOne = i
                    repLayerTwo = j
                    repLayerTrhee = m
                    repInversionLeni = inversionLeni
                    repInversionLenj = inversionLenj
                    repInversionLenm = inversionLenm
                    
    print("\n",repLayerOne,repInversionLeni,"\n",repLayerTwo,repInversionLenj, "\n", repLayerTrhee,repInversionLenm, "chosen out of 27 000 000")
    print("current score is", highestScore)
    return repLayerTrhee

    
alist = [23,1,2,11,24,22,19,6,10,7,25,20,5,8,18,12,13,14,15,16,17,21,3,4,9]
endResult = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
result = []

# searches three layers deep on every result until the end result is found.
while result != endResult:
    if not result:
        firstLayer = getAllInversions(alist)
    else:
        firstLayer = getAllInversions(result)
        
    result = threeLayerSearch(firstLayer)
   

