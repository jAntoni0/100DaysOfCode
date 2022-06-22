import math
probs = {}
#we already know that cube of 13 is greater than 1729 Ramanujan-Hardy number
for first in range(1, 13):
    probs[first] = 1729-first**3 #I save in dic to know the pair of numbers
    round_number = round(math.pow(probs[first],1/3),3) #It looks that Py is little strict with decimals
    if round_number.is_integer(): #Just verify that cube root is an integer
        print(first, int(round_number))