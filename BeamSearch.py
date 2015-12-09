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
    biggestChunk = 0
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
                if chunk > biggestChunk:
                    biggestChunk = chunk
                chunk = 0
    return biggestChunk

def threeLayerSearch(layerOne):
    countk = 0
    tempLayerTwo = []
    tempLayerThree = []
    repLayerOne = []
    repLayerTwo = []
    repLayerTrhee = []
    longestChunk = 0
    currentChunk = 0
    for i in layerOne:
        templayerTwo = beamSearch(i)   
        for j in templayerTwo:
            tempLayerThree = beamSearch(j)
            for m in tempLayerThree:
                countk += 1
                # saves the first instance of the longest chunk
                currentChunk = chunkFinder(m)
                if currentChunk > longestChunk:
                    longestChunk = currentChunk
                    repLayerOne = i
                    repLayerTwo = j
                    repLayerTrhee = m
    #print(tempLayerTwo)
    print(countk)
    print("total adjecent numbers is", longestChunk)
    print("\n",repLayerOne,"\n",repLayerTwo, "\n", repLayerTrhee, "chosen out of 27 000 000")
    return repLayerTrhee

    
alist = [23,1,2,11,24,22,19,6,10,7,25,20,5,8,18,12,13,14,15,16,17,21,3,4,9]
layerOne = beamSearch(alist)
layerThree = threeLayerSearch(layerOne)


