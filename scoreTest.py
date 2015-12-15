def chunkFinder(alist):
    counter = 0
    elements = 0
    chunklength = 0
    score = 0
    biggestChunk = 0
    
    for i in range(len(alist)):
        #detects if numbers are already sorted and counts those numbers
        #here we call those numbers sorted numbers a chunk
        if alist[(i+1)% len(alist)] == alist[i]+1 or alist[(i-1)% len(alist)] == alist[i]-1:
            #print("herkend", alist[i])
            #represents te size of the chunk
            chunklength += 1
            counter += 1
            if alist[(i-1)% len(alist)] == alist[i]-1 and alist[(i+1)% len(alist)] != alist[i]+1:
                counter += 1
        
        elif alist[(i+1)% len(alist)] == alist[i]-1 or alist[(i-1)% len(alist)] == alist[i]+1:
            #print("herkend!", alist[i])
            chunklength += 1
            counter += 1
            if alist[(i-1)% len(alist)] == alist[i]+1 and alist[(i+1)% len(alist)] != alist[i]-1:
                counter += 1
        else:
            counter += 1

    elements = counter - chunklength
    score = chunklength / elements
    print("elements", elements, "total chunk length", chunklength)
    return score
    
alist = [23,  1,2,  11,  24,  22,  19,  6,  10,  7,  25,  20,  5,  8, 18,17,16,15,14,13,12,  21,  3,4,  9]
blist = [23,  1,2,  11,  24,  22,  19,  6,  10,  7,  25,  20,  5,  8,  18,  12,13,14,15,16,17,  21,  3,4,  9]
score = chunkFinder(alist)
print(score)