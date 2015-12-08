from collections import defaultdict
from copy import deepcopy

def beamSearch(alist):

    queue = []
    count = 0
    for i in range(len(alist)):
        #print(i)
        for j in range(i + 1, len(alist)):
            blist = deepcopy(alist)
            blist[i:j+1] = reversed(blist[i:j+1])
            #print(blist)
            queue.append(blist)
            count += 1
            
    return queue
      
def chunkFinder(alist):
    count = 0
    chunk = 0
    blist = [None]*len(alist)
    
    
    for i in range(len(alist)):
        #detects if numbers are already sorted and counts those numbers
        #here we call those numbers sorted numbers a chunk
        if alist[(i+1)% len(alist)] == alist[i]+1 or alist[(i-1)% len(alist)] == alist[i]-1:
            #represents te size of the chunk
            chunk += 1
            #optional, just to show the chunks in an empty list
            blist[i] = alist[i]
            
            #gives end and begin index of chunk
            if alist[(i+1)% len(alist)] != alist[i]+1:
                beginChunk = alist.index(alist[i])-chunk+1
                endChunk = alist.index(alist[i])
                #print("chunsize is",chunk, "begin index chunk is",beginChunk,"end index chunk is", endChunk)
                # reset chunk size for next chunk
                #chunk = 0
        
    
    return chunk
    
def threeLayerSearch(layerOne):
    countk = 0
    templayer = []
    layerTwo = []
    repLayerTwo = []
    repLayerTrhee = []
    longestChunk = 0
    currentChunk = 0
    for i in range(len(layerOne)):
        templayer = beamSearch(layerOne[i])
        for j in range(len(templayer)):
            layerTwo.append(templayer[j])

    for k in range(len(layerTwo)):
        templayer = beamSearch(layerTwo[k])
        for m in range(len(templayer)):
            countk += 1
            
            # decides which list is the best
            currentChunk = chunkFinder(templayer[m])
            if currentChunk > longestChunk:
                longestChunk = currentChunk
                repLayerTwo = layerTwo[k]
                repLayerTrhee = templayer[m]

    print("total adjecent numbers is", longestChunk)
    print("layer two is",repLayerTwo, "layer three is", repLayerTrhee)
    return repLayerTrhee
    
def threeLayerSearchTest(layerOne):
    countk = 0
    tempLayerTwo = []
    tempLayerThree = []
    layerTwo = []
    repLayerOne = []
    repLayerTwo = []
    repLayerTrhee = []
    longestChunk = 0
    currentChunk = 0
    for i in range(len(layerOne)):
        templayerTwo = beamSearch(layerOne[i])
        #print(templayerTwo)
        for j in range(len(tempLayerTwo)):
            tempLayerThree = beamSearch(tempLayerTwo[j])
            print(tempLayerTwo[j])
            for m in range(len(templayerThree)):
                countk += 1
                
                # decides which list is the best
                currentChunk = chunkFinder(templayer[m])
                if currentChunk > longestChunk:
                    longestChunk = currentChunk
                    repLayerOne = layerOne[i]
                    repLayerTwo = tempLayerTwo[j]
                    repLayerTrhee = templayer[m]

    print(countk)
    print("total adjecent numbers is", longestChunk)
    print("layer one is",repLayerOne,"layer two is",repLayerTwo, "layer three is", repLayerTrhee)
    return repLayerTrhee

    
alist = [23,1,2,11,24,22,19,6,10,7,25,20,5,8,18,12,13,14,15,16,17,21,3,4,9]
layerOne = beamSearch(alist)
layerThree = threeLayerSearchTest(layerOne)


