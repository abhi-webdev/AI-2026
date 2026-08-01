
""""
List has a power to :
    1. Mutable : Object value can be changes after creation
    2. Duplicates: Duplication allow in this list
    3. Ordered: List maintion their order. So we can access their value using index/position
    4. Hetrogeneous: we can store multiple data type inside list
"""

data = [12,3,"abhi", True, 'S', 12]

print(data)

print(data[0])
print(data[3])

for i in range(len(data)) :
    print(data[i])



numbers = [5,2,5,6,3]
numbers.append(10)
numbers.insert(0, True)
numbers.remove(2)
copy = numbers.copy()
print(copy)
numbers.extend(["abhi", "kumar"])
numbers.remove("kumar")
numbers.pop(2)
numbers.reverse()

numbers[0] = "sonu"

print(numbers)



# ---------- Print positive and negative elements from the list ----------

nums = [-1,35,3,-30, -59, 6]

pos = []
neg = []

for i in range(len(nums)) :
    if(nums[i] < 0) :
        pos.append(nums[i])
    else :
        neg.append(nums[i])


print(f"positive value is {pos}")
print(f"Negative value is {neg}")



#  ------------ Mean of list element ------------
print("Mean of list element-----------")

numVal = [1,2,45,6,7,8]

sum = 0
avg = 0
for i in numVal:
    sum = sum + i
    avg = sum / len(numVal)

print(avg)



print("Find the greatest element and print it index to -------------")

numVal = [1,2,45,6,7,14]

maximum = 0
index = 0
for i in range(len(numVal)):
    if numVal[i] > maximum :
        maximum = numVal[i]
        index = i
print(f"index {index} : greatest value is : {maximum}")



print("Find the second greatest element?----------------------")

numVal2 = [1,2,45,6,7,14]

firstLargest = numVal2[0]
secondLargest = numVal2[0]

for i in numVal2 :
    if(i > firstLargest) :
        secondLargest = firstLargest
        firstLargest = i
    elif i > secondLargest :
        secondLargest = i

print(f"First greater element : {firstLargest}")
print(f"Second gerater element : {secondLargest}")


print("Check if List is sorted or not.----------------")

checkList = [54,6,426,7,843,4,2]
# checkList = [1,2,3,4]
n = len(checkList)
for i in range(n-1) :
    if checkList[i] < checkList[i+1] :
        continue
    else :
        print("list is not sorted")
        break
else :
    print("Your list is sorted")

