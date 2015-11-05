"""
Bubble sort that recognizes chunks of already sorted data and moves the as a whole.
Right now its not working properly.
Look at chunkFinder.py for a demonstration of how these chunk are found.
"""
def bubbleSort(alist):
    count = 0
    chunk = 0
    chunkList = [None]*len(alist)
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum): 
            #detects if numbers are already sorted and counts those numbers
            #here we call those numbers sorted numbers a chunk
            if alist[(passnum+1)% len(alist)] == alist[passnum]+1 or alist[(passnum-1)% len(alist)] == alist[passnum]-1 and alist[passnum]>alist[passnum+1]:
                #represents te size of the chunk
                chunk += 1
                #fills chunk list for chunk checking
                chunkList[i] = alist[i] """"List is not filling properly, probably due to the second loop construct """
                
                if alist[(i+1)% len(alist)] != alist[i]+1:
                    #gives end and begin index of chunk
                    beginChunk = alist.index(alist[i])-chunk+1
                    endChunk = alist.index(alist[i])
                    print(chunk, beginChunk, endChunk)

                    """
                    something is going wrong here!!
                    """
                    #if number after the chunk is smaller than last number in chunk, 
                    #swap that number with the whole chunk
                    if alist[endChunk]>alist[endChunk+1]:
                        temp = alist[beginChunk:endChunk+1]
                        alist[beginChunk] = alist[endChunk+1]
                        alist[endChunk+1:endChunk+chunk+1] = temp
                        
                    print(alist)
                    # reset chunk size for next chunk
                    chunk = 0
                    
            #if number is in the chunk list ignore it      
            for j in chunkList:
                if alist[i] == j:
                    print("no swap", j)
                    break
            
            #swap all number not in a chunk of orderred numbers    
            if alist[i]>alist[i+1] and alist[(passnum-1)% len(alist)] != alist[passnum]-1:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp
                #print(alist)
                count += 1
    print("Maximum nuber of moves is:",count)
    print(chunkList)
                

alist = [23,1,2,11,24,22,19,6,10,7,25,20,5,8,18,12,13,14,15,16,17,21,3,4,9]
bubbleSort(alist)
print(alist)
