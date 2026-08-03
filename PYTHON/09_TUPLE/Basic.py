
"""
Immutable - Tuples are not mutable you cannot change
the values of tuple
Duplicate - You can have duplicate values in tuple there
are no restriction
Ordered - Tuple are ordered and you can access them
through index values
Heterogenous - Tuple also have heterogenous nature and
can have different types of data structure in tuple.
"""


t = (1,2,4,5,4)

print(type(t))

index = t.index(4)
count = t.count(4)

print(f"first occurance is : {index}")
print(f"totoal occurence is {count}")