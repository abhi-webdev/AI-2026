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
