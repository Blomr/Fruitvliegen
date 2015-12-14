from collections import defaultdict
from copy import deepcopy

def beamSearch(alist):

    queue = []
    count = 0
    for i in range(len(alist)):
        for j in range(i + 1, len(alist)):
            blist = deepcopy(alist)
            blist[i:j+1] = reversed(blist[i:j+1])
            queue.append(blist)
            count += 1     
    return queue
      
def chunkFinder(alist):
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
    score = elements
    return score

def threeLayerSearch(layerOne):
    countk = 0
    endResult = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
    tempLayerTwo = []
    tempLayerThree = []
    repLayerOne = []
    repLayerTwo = []
    repLayerTrhee = []
    lowestScore = 100
    currentScore = 0
    for i in layerOne:
        if i == endResult:
            print("\n",i)
            return i
        templayerTwo = beamSearch(i)   
        for j in templayerTwo:
            if j == endResult:
                print("\n",i, "\n",j)
                return j
            tempLayerThree = beamSearch(j)
            for m in tempLayerThree:
                countk += 1
                # saves the best out of 27000000 
                currentScore = chunkFinder(m)
                if currentScore < lowestScore:
                    lowestScore = currentScore
                    repLayerOne = i
                    repLayerTwo = j
                    repLayerTrhee = m
    #print(tempLayerTwo)
    print(countk)
    print("\n",repLayerOne,"\n",repLayerTwo, "\n", repLayerTrhee, "chosen out of 27 000 000")
    print("current score is", lowestScore)
    return repLayerTrhee

    
alist = [23,1,2,11,24,22,19,6,10,7,25,20,5,8,18,12,13,14,15,16,17,21,3,4,9]
#layerOne = beamSearch(elist)
#layerThree = threeLayerSearch(layerOne)

endResult = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
result = []

while result != endResult:
    if not result:
        firstLayer = beamSearch(alist)
    else:
        firstLayer = beamSearch(result)
        
    result = threeLayerSearch(firstLayer)
   



"""
blist = [23, 1, 2, 11, 10, 7, 6, 19, 22, 24, 25, 20, 5, 4, 3, 21, 17, 16, 15, 14, 13, 12, 18, 8, 9]
clist = [12, 13, 14, 15, 16, 17, 21, 3, 4, 5, 6, 7, 10, 11, 2, 1, 23, 22, 24, 25, 20, 19, 18, 8, 9]
dlist = [25, 24, 22, 23, 1, 2, 3, 4, 5, 6, 7, 10, 11, 12, 13, 14, 15, 16, 17, 21, 20, 19, 18, 8, 9]
elist = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 25, 24, 22, 23, 1, 2, 3, 4, 5, 6, 7, 8, 9]
"""

