"""
    1. Dictionary mutable hoti hai
    2. Key must be unique, value may be duplicate
    3. Dictonary follow insertion order
    4. Dictonary can store multiple types of keys and values Like : Integer, string, list or even another dictonary

"""

#  Dictionary == hashmaps

d = {
    'id': 1,
    '1': "Abhi",
    "age": 21
}

print(d['1'])

d['age'] = 22

print(d)


# ------ Hetrogeneous nature ----------------

dataSet = {
    id: 1,
    "details" : {
        "name" : "Anand",
        "address" : {
            "village" : "Mairwa"
        }
    }
}
print(dataSet)
print(dataSet["details"]["address"]["village"])
# -------Dictonary traversing ----------------

data = {
    "id" : 1,
    "name" : "Abhimanyu",
    "city" : "Mairwa",
    "country" : "India"
}

# in dictionary if you are updating the not existing value, so that they will create inside the dictonary, if existing value is there then you can update using key

data.update({"pincode" : "841239"})  # creating
data.update({"city" : "Siwan"})  # updating

data["mob"] = "32838238238" # creating

del data["mob"]  # deleting

print(data.keys())
for i in data :
    print(data[i])


# help(dict)

# Question 1. Merge two dictionary into one dictonary

d1 = {10:100, 20:200, 30:300}
d2 = {40:400, 50:500, 60:600}

for i in d2 :
    d1[i] = d2[i]

print(d1)


# ---------- Sum all the value of dictionary----------
sum = 0
for i in d2: 
    sum += d2[i]

print(sum)

# -------- count frequency in List ------------

numbers = [1, 2, 1, 3, 2, 1]
freq = {}

for i in numbers :
    if i in freq :
        freq[i] += 1
    else :
        freq[i] = 1

print(freq)


