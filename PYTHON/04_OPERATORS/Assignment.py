

# -------- Compound assignment operator --------------

print("--------- Compound assignment operator -------------")
a = 10
a += 1
print(a)

b = 5
b -= 2

print(b)

c = 4
c *= 8

print(c)


d = 20
d /= 2

print(d)


e = 12
e //= 7    # ye flore value dega 

print(e)


f = 35
f %= 6   # reminder

print(f)


g = 3
g **= 3   # exponent power

print(g)


print("--------Comparision operator -----------")

#   == -> Equal to

a = 10
b = 10
# b = "10"  -> false

print(a==b)

fname = "abhi"
lname = "abhi"
print(fname == lname)
print(fname != lname)


name1 = "and"
name2 = "anand"
print(name1 > name2)  # true -> because python compare char by char 
print(name1 < name2)   # false ->  because python compare char by char 
print(name1 <= name2)   # false ->  because python compare char by char 
print(name1 >= name2)   # true ->  because python compare char by char 

print("IF prefix of another string then... ")
print("ana" < "anand")   # True -> because all the char from the first matched with the second string
print("ana" > "anand")   # false -> first string end before ending the second string

val1 = 20
val2 = 4
print(val1 > val2)
print(val1 < val2)


# print('A' > 34)
print(ord('A') > 34)



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

