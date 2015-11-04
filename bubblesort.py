def bubbleSort(alist):
    count = 0
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):  
            if alist[i]>alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp
                print(alist)
                count += 1
                
    print("Maximum nuber of moves is:",count)
                

alist = [23,1,2,11,24,22,19,6,10,7,25,20,5,8,18,12,13,14,15,16,17,21,3,4,9]
bubbleSort(alist)
#print(alist)
