"""
This method look at both sides of the list (right and left)
depending on which side provides the shortest swap length, 
that side will be swapped.
"""
def shortSort(alist):
    swapLengthA = 0
    swapLengthB = 0
    swaps = 0
    revCounter = len(alist)
    swapLengthTotal = 0
    i = 0
    k = 0
    while k != len(alist):
        # break out of loop if i becomes length of alist
        if i == len(alist):
            break
            
        # break out of loop if i becomes length of alist, will also be caugth by while loop
        if k == len(alist):
            break
            
        # continue if i number is already in position
        if i + 1 == alist[i]:
            i += 1
            continue
            
        # continue if revCounter number is already in position
        if revCounter == alist[revCounter - 1]:
            revCounter -= 1
            continue        

        swapLengthA = len(alist[i:alist.index(i + 1) + 1]) 
        swapLengthB = len(alist[alist.index(revCounter):revCounter])
        
        if swapLengthA < swapLengthB:
            print("Left swap is smaller:", "left =", swapLengthA, "swaps, right =", swapLengthB, "swaps")
            print("replaced:", str(i+1))
            print("swap length:", swapLengthA)
            # swap part of the list
            alist[i:alist.index(i + 1) + 1] = reversed(alist[i:alist.index(i + 1) + 1])
            print(alist, "\n")
            # update total counter
            k += 1
            # update i counter
            i += 1
            # update total swap length
            swapLengthTotal += swapLengthB
            swaps += 1
            
        else:
            print("Right swap is smaller:", "left =", swapLengthA, "swaps, right =", swapLengthB, "swaps")
            print("replaced:", revCounter)
            print("swap length:", swapLengthB)
            # swap part of the list
            alist[alist.index(revCounter):revCounter] = reversed(alist[alist.index(revCounter):revCounter])
            print(alist, "\n")
            # update revCounter
            revCounter -= 1
            # update total counter
            k += 1
            # update total swap length
            swapLengthTotal += swapLengthB
            swaps += 1

    print ("---> Swaps: ", k)
    print ("---> Total swap length: " + str(swapLengthTotal))
    print ("---> Average: " + str(swapLengthTotal / swaps) + " genes per swap")

alist = [23,1,2,11,24,22,19,6,10,7,25,20,5,8,18,12,13,14,15,16,17,21,3,4,9]
shortSort(alist)