melano = [23, 1, 2, 11, 24, 22, 19, 6, 10, 7, 25, 20, 5, 8, 18, 12, 13, 14, 15, 16, 17, 21, 3, 4, 9]


dictionary = { 	 1 : 1
				 2 : 1
				 3 : 1
				 4 : 1
				 5 : 1 
				 6 : 2 
				 7 : 2 
				 8 : 2 
				 9 : 2 
				10 : 2 
				11 : 3
				12 : 3
				13 : 3
				14 : 3
				15 : 3
				16 : 4
				17 : 4
				18 : 4
				19 : 4
				20 : 4
				21 : 5
				22 : 5
				23 : 5
				24 : 5
				25 : 5	}
				
beginNumber = 0
endNumber = beginNumber
				
for i in range(len(melano)):
	if beginNumber == 0:
		beginNumber = i
		
	if dictionary[melano[i]] > dictionary[melano[i + 1]]:
	# 3e getal mag kleiner of gelijk aan 2e
	# 4e getal mag kleiner of gelijk aan 3e
	elif dictionary[melano[i]] < dictionary[melano[i + 1]]:
	# !! staat goed tov aan elkaar !!
	# !! ga naar volgende i !!
	# !! beginnumber = 0 !!
	else: 
	# 3e getal mag kleiner, groter of gelijk aan 2e			
				