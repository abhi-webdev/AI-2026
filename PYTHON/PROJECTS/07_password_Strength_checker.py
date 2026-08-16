
import string
import getpass
import random


def pass_strength_check(password) :
    issues = []
    if len(password) < 8:
        issues.append("Too short, (Minimum 8 character)")

    if not any(c.islower() for c in password) :
        issues.append("Missing Lowercase character")
    if not any(c.isupper() for c in password) :
        issues.append("Missing uppercase character")
    if not any(c.isdigit() for c in password) :
        issues.append("Missing digit")
    if not any(c in string.punctuation for c in password) :
        issues.append("Missing special characters")

    return issues

def generate_strong_password(length=12) :
    # char = string.ascii_letters + string.digits + string.punctuation
    char_lower = "abcdefghijklmnopqrstuvwxyz"
    char_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    char_digit = "0123456789"
    char_special = "!@#$%^&*()_+"
    char = char_lower + char_upper + char_digit + char_special
    return "".join(random.choice(char) for _ in range(length))


password = getpass.getpass("Enter the password: ")
issue = pass_strength_check(password)

if not issue:
    print("You are good to go!")
else :
    print("Your password is week")
    print(issue)

suggesstion = generate_strong_password()
print("suggesting strong password: ") 
print(suggesstion)
    
    
    
