
def calculator(age) :
    DAYS_IN_YEAR=365.25
    HOURS_IN_DAY=24
    MINUTUS_IN_HOUR=60

    total_days = age * DAYS_IN_YEAR
    total_Hours = total_days * HOURS_IN_DAY
    total_minutes = total_Hours * MINUTUS_IN_HOUR

    return round(total_days), round(total_Hours) , round(total_minutes)


while True :
    try :
        age = float(input("Enter your age : "))
        days, hours, minutes = calculator(age)

        print("\n you are approx ")
        print(f" - {days} days old")
        print(f" - {hours} hours old")
        print(f" - {minutes} minutes old")

        again = input("Would you want to try again (y/n)").strip().lower()

        if again != 'y' :
            print("Good bye")
            break

    except: 
        print("Please enter the valid age")

