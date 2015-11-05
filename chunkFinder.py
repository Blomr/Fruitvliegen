def bubbleSort(alist):
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
                print("chunsize is",chunk, "begin index chunk is",beginChunk,"end index chunk is", endChunk)
                # reset chunk size for next chunk
                chunk = 0
        
    
    print(blist)

alist = [23,1,2,11,24,22,19,6,10,7,25,20,5,8,18,12,13,14,15,16,17,21,3,4,9]

bubbleSort(alist)
print(alist)