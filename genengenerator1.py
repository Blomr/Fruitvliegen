
import random


genomen = []
i = 0

while i < 100:

    # genereer random genenset
    genenset = []
    genenset = random.sample(xrange(1, 26), 25)
    genomen.append(genenset)
    i = i + 1

# print de lijst van genomen met daar in lijsten van genen
for j in range(len(genomen)):
    print genomen[j]
    j = j + 1




