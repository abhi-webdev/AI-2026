
#  --------------- Logical operator -------------------
print("------------ Logical operator ------------------")

print(13>12 and 13==13 and 14>20)   # false  -> all condition should be true
print(13>12 and 13==13 or 14>20)    # true  -> two condition must be true but either one be false 
print((456 == 456) != (235 == 236))
print((456 == 456) == (235 == 236))
print(True != False)
print(True == False)


print(True and bool(0)) # false
print(True or bool(0))  # true

#  Not -> reverse the boolean value
print(not 13 == 13)  # true -> false  or   false -> true