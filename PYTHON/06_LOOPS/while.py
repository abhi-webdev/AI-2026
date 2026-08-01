

a = 1
while a<30 : 
    # print(a)
    a = a+1


n = 234
while n>0 :
    rem = n % 10
    # print(rem)
    n = n // 10


# num= int(input("Enter the num: "))

# while num > 0 :
#     rem = num % 10
#     # print(rem)
#     num = num//10



# Create a random number guessing game with python.-------------

import random
num = random.randint(1,10)
tries = 0

while True : 
    guess = int(input("Guess the number between 1 to 10 : "))
    if guess == num: 
        print("You are right")
        break
    else : 
        print("Sorry you are wrong")
        tries += 1

print(tries)
