

# --------- type conversion---------

ch = 'A'
print(ord(ch))   # convert character to their value

ch2 = "✅"
print(ord(ch2))   # convert emoji to their value

# convert value to character, emoji, special character

print(chr(65))
print(chr(92))


# ------- Datatype conversion function int() float() str() boolean() --------
"""
Two types of conversion 
1. Implicit -> In python, a = 12  => print(a/6) output 2.0  <== it autimatically convert into int to float value
2. Explicit -> prebuilt datatype => int(), float(), complex(), str(), list(), tuple, set(), dict(), bool() 

"""


# -------- String to int, float---------
s = '12'
intConvertedValue = int(s)
floatConvertedValue = float(s)

print(intConvertedValue)
print(type(intConvertedValue))


print(floatConvertedValue)
print(type(floatConvertedValue))


# -------- integer, float to string ----------

intVal = 12

intConvertString = str(intVal)
print(intConvertString)
print(type(intConvertString))

floatVal = 39.53
floatConvertString = str(floatVal)

print(floatConvertString)
print(type(floatConvertString))

floatVal1 = 2.5
complexConvert =  complex(floatVal1)
print(type(complexConvert))
print(complexConvert)   # (2.5+0j)




# -------- complex datatype ----------

c = 12j    # j denote the value of c is complex
print(type(c))


