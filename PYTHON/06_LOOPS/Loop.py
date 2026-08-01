
#  Doing same repeatation work 
"""
 Types of loop in python
    1. For Loop  -> if you know how many times loop will run then use for loop
    2. While Loop  -> if You don't know how many times loop will run 


    For Loop-----------
    In for loop there is a "range" function that syntax is range(start, stop, steps)
    if you will not mentioned the start value, then default will be 0,
    if you will not mentioned the steps value, By default it will take 1,
    if you will not mentioned the stop value, then loop will not execute

"""


for i in range(1, 5) :   # 1 to 4
    print(i)


# --------- Loop for String ------------

name = "abhimanyu"
for i in range(len(name)) :     #  Itterate through indexing
    print(name[i])
  
a = "nature"
for char in a :      # Itterate through character
    print(char)


#  ------------ Break Statement ----------------

for i in range(10) :
    if ( i == 5) :
        break
    print(i)


# ----------------- For loop questions ------------------

# 1. Accept an integer and Print hello world n times
# val = int(input("Enter how many times: "))

# for i in range(val) : 
#     print("Hello")


# 2. - Print natural number up to n

# start = int(input("Enter start: "))
# times = int(input("Enter times: "))
# for i in range(start, start + times) :
#     print(i) 



# 3. - Reverse for loop. Print n to 1

for i in reversed(range(10, 29)) :
    print(i)


# 4. - Sum up to n terms

val = 1
for i in range(1,6) :
    val += i

print(val)

# 5. Factorial of a number  -> 5! = 1*2*3*4*5

# num = int(input("Enter the n : "))
# result = 1
# for i in range(1, num+1) :
#    result = result * i
   
# print(f"your fact is {result}")

# 6. - Print the sum of all even & odd numbers in a range separately

# evenSum = 0
# oddSum = 0
# n = int(input("Enter n: "))

# for i in range(0, n+1) :
#     if(i % 2 == 0) :
#         evenSum += i
#     else :
#         oddSum += i

# print(f"Even Sum : {evenSum}")
# print(f"Odd Sum : {oddSum}")


# 7. Print all the factors of a number

# fac = int(input("Enter the number: "))

# for i in range(1, fac+1) :
#     if(fac % i == 0) : 
#         print(i)

# - Accept a number and check if it a perfect number or not. A number whose sum of factors is equal to the number itself

# number = int(input("Enter the number: "))
# match = 1
# for i in range(1, number) : 
#     if (number % i == 0) : 
#         match = match * i
    
# if number == match :
#     print("Perfect number")
# else :
#     print("Not perfect Number")


# 8. - Check wether the number is prime or not

# pNum = int(input("Enter the number: "))
# isPrime = False
# for i in range(1, pNum + 1) :
#     if(pNum % i == 0) :
#         isPrime = True


# print(isPrime)


# 9. Reverse a string without using in build functions.4

s = "abhimanyu"
for i in range(len(s)-1, -1, -1) :
    print(s[i])


# 10. Check string is Pallindrome or not

string = "momy"
s1 = ""
for i in range(len(string)-1, -1, -1) :
    s1 += string[i]

if s1 == string :
    print("palindrome")
else :
    print("Not palindrome")


"""
Count all letters, digits, and special symbols from a given
string
Given: str1 = "P@#yn26at^&i5ve"
Expected Outcome:
Total counts of chars, digits, and symbols
Chars = 8
Digits = 3
Symbol = 4
"""

str1 = "P@#yn26at^&i5ve"
chars = 0
digits = 0
symbols = 0

for i in range(len(str1)) : 
    if(ord(str1[i]) >= 32 and ord(str1[i]) < 47 or ord(str1[i]) >= 58 and ord(str1[i]) < 64 or ord(str1[i]) >= 91 and ord(str1[i]) < 96 or ord(str1[i]) >= 33 and ord(str1[i]) < 47 or ord(str1[i]) >= 123 and ord(str1[i]) < 126) :
        symbols += 1
    elif (ord(str1[i]) >= 65 and ord(str1[i]) < 90 or ord(str1[i]) >= 97 and ord(str1[i]) < 122) :
        chars += 1
    else :
        digits += 1

print(f"symbols is : {symbols}")
print(f"digits is : {digits}")
print(f"chars is : {chars}")