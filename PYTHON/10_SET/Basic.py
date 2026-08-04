
""""
1. Set are mutable
2. Set doesn't carry duplicates value
3. sets are unorderd, and you not access via index
4. Set is semi-heterogenous it can store some data types like string, numbers, tuples but not everything
"""

s = {1,"abhi", True, 1, 3}
print(type(s))

print(s)

#  access of set elements
s.add("Kumar")
print(s)


#  set untracked 

a,b,c,d = (1,2,4,5)

print(a,b,c,d)

# hashed value

b = "hello"
c = 10
hashed = hash(b)

print(hashed)
print(hash(c))


# Set Methods ----------------------

s = {8,2,4,5}

s.add("Hello")
s.remove("Hello")
s.pop()
s.clear()
print(s)

# Sets -> union, intersection, difference
 
p = {1,2,3}
q = {3,4,5}

union_set = p.union(q)   # p | q
print(union_set)

intersection_set = p.intersection(q)   # p&q
print(intersection_set)

difference_set = p.difference(q) # (b-a) -> 3 common hai ur q - p kar rehe ho so ans p ka aayega
print(difference_set)

symmetric_difference = p.symmetric_difference(q)

print(symmetric_difference)

