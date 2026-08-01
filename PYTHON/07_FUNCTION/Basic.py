
#  ----------- Normal function ----------
def hello() : 
    print("say hello")

hello()
hello()
hello()

#  ----------parameter and Argument function -------------

def greet(name: str, age : int) :
    print(f"hii, {name}. Your age is {age}")

greet("Abhimanyu", 20)

def add(a, b ) :
    print(a+b)

add('4', '5')
add(3,4)



# --------- return statement -----------

def intro(name, marks) :
    return f"{name} marks is {marks}"


print(intro("Amrit", 490))  
print(intro(marks=355, name="anand"))    # Keyword argument 


# ----------- default argument ------------------

def mul(a, b=2) :
    print(f"Multiple of a, b is {a*b}")

mul(4)
mul(4, 8)


# ---------- check string is palindrome or not --------------

def palindrome(s: str) :
    s1 = ""
    for i in range(len(s)-1, -1, -1) :
        s1 += s[i]
    if s1 == s :
        print(f"This {s} String is palindrome")
    else : 
        print(f"This {s} String is not palindrome")


palindrome("abhi")
palindrome("mom")