
if True: 
    print("hello")


if False: 
    print("hello")
else:
    print("kon")


marks = int(input("Enter the marks: "))
if (marks > 90) :
    print("1st division")
elif (marks > 70) :
    print("2st division")
elif (marks > 50) :
    print("3rd division")
elif (marks > 30) :
    print("4th division")
else :
    print("fail")




"""

Q2. Accept the gender from the user as char and print the respective greeting message
Ex - Good Morning Sir (on the basis of gender)

"""

Gender = str(input("Enter the gender: "))
if(Gender == "M") : 
    print("Good morning sir")
elif (Gender == "F") :
    print("Good morning mam")
else :
    print("Good morning chhaka")


"""
Q3. Accept an integer and check whether it is an even number or odd.
"""

num = int(input("Enter the value: "))

if(num % 2 == 0) :
    print("Even number")
else :
    print("Odd number")


"""Accept name and age from the user. Check if the user is a valid voter or not."""

name = str(input("Enter the name: "))
age = int(input("Enter the age: "))

if name != "" and age >= 18 :
    print("Eligible for vote")
else : 
    print("Not Eligible for vote")


"""
Q5. Accept a year and check if it a leap year or not (google to find out what is a leap year)
"""

year = int(input("Enter the year: "))

if (year % 4 == 0) :
    print("Leap year")
else :
    print("Not leap year")


"""
You can also create if elif ladder using multiple conditions of
elif.j
@ For understanding solve this questionj
@ take the input of temperature in celsiusX
@ Below 0°C → "Freezing Cold b
@ 0°C to 10°C → "Very Cold b
@ 10°C to 20°C → "Cold b
@ 20°C to 30°C → "Pleasant b
@ 30°C to 40°C → "Hot b
@ Above 40°C → "Very Hot "
Some Questions on Conditional

"""
temp = int(input("Enter the temp: "))

if temp >= 40 :
    print("Very Hot")
elif temp >= 30 and temp < 40 :
    print("Hot")
elif temp >= 20 and temp < 30 :
    print("Pleasent")
elif temp >= 10 and temp < 20 :
    print("Cold")
elif temp >= 0 and temp < 10 :
    print("Very cold")
else :
    print("Freezing cold")
