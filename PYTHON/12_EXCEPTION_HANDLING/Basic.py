#  Error in python
#  1. Syntax error 2. Indentation error 



# ----- Exceptions --------
"""
    exception are unexpected events or error that occurs during the execution of program, which distrupt the normal flow of program
"""


a = int(input("Enter the number: "))
    # print(10/a)   -> divisionByZero error

try:
    print(10/a)
    print("Code success✅")
except Exception as err :
    print("Error in your type block❌", err)
else :
    print("Good there is no exception")
finally :
    print("Code end")


# ------- raise(manually throw exception error) ----------

age = int(input("tell me your age: "))
try :
    if age > 18 :
        print("Eligible for vote")
    else :
        raise ValueError("Not eligible")
except Exception as err :
    print(err)

