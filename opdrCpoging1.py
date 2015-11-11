def shortSort(alist):
    swapLengthA = 0
    swapLengthB = 0
    blist = [None]*len(alist)
    swaps = 0
    revCounter = len(blist)
    j = 0
    for i in range(len(alist)):
        if i + 1 == alist[i]:
            continue

        blist[0:] = reversed(alist[0:])
        swapLengthA = len(alist[i:alist.index(i + 1) + 1]) 
        swapLengthB = len(blist[j:blist.index(revCounter) + 1]) #leest nog steeds van klein naar groot
        
        if swapLengthA < swapLengthB:
            print("links is kleiner", swapLengthA, swapLengthB)
            alist[i:alist.index(i + 1) + 1] = reversed(alist[i:alist.index(i + 1) + 1])
            swaps = swaps + 1
                
        else:
            print("rechts is kleiner", swapLengthA, swapLengthB)
            h = revCounter+swapLengthB
            alist[-h:-revCounter+1] = reversed(alist[-h:-revCounter+1]) #moet nog even naar gekeken worden
            revCounter -= 1
            # j houd positie blist bij, zodat niks word overgeslagen
            j += 1
            #print(swapLengthB)
            revCounter -= 1
            swaps = swaps + 1
            

    print ("---> Swaps: " + str(swaps))
    #print(blist)

alist = [23,1,2,11,24,22,19,6,10,7,25,20,5,8,18,12,13,14,15,16,17,21,3,4,9]
shortSort(alist)
print(alist)