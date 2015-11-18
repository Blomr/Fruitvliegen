swapcount = 0

def playSwap (alist, first, second):
    swapLength = len(alist[alist.index(first) : alist.index(second) +1 ])
    alist[alist.index(first) : alist.index(second) +1 ] = reversed(alist[alist.index(first) : alist.index(second) +1 ])
    print("\n", "swap length is:", swapLength)
    print(alist)


melano = [23, 1, 2, 11, 24, 22, 19, 6, 10, 7, 25, 20, 5, 8, 18, 12, 13, 14, 15, 16, 17, 21, 3, 4, 9]
miranda = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]

print(miranda)
print (melano)


while melano != miranda:
    first = input("enter first number of swap: ")
    second = input("enter last number of swap swap: ")
    swapcount += 1
    print(swapcount)
    playSwap(melano, first, second)
    
print("Done! in", swapcount, "swaps!")
