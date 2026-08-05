
from datetime import date 

name = input("What is your name? ").strip()
age = input("How old are you? ").strip()
city = input("Which city are you from? ")
country = input("Which country are you from? ")
profession = input("Are you a student or working professional? ")
college = input("Which college do you study in? ")
course = input("What course are you pursuing? ")
year = input("Which year/semester are you in? ")
favorite_subject = input("What is your favorite subject? ")
hobby = input("What is your hobby? ")
favorite_food = input("What is your favorite food? ")
favorite_sport = input("What is your favorite sport? ")
dream_company = input("Which company do you want to work for? ")
goal = input("What is your career goal? ")
language = input("Which programming language do you like the most? ")

intro =  f"""
Hello everyone!

My name is {name}, and I am {age} years old. I am from {city}, {country}. I am currently a {profession} pursuing {course} at {college}. I am in my {year}.

My favorite subject is {favorite_subject}, and I enjoy learning new technologies. In my free time, I love {hobby}. My favorite food is {favorite_food}, and I enjoy watching or playing {favorite_sport}.

I like programming, especially using {language}. My dream is to work at {dream_company} and achieve my goal of becoming {goal}.

Thank you for taking the time to know about me. It was nice meeting you!
"""

current_date = date.today().isoformat()
intro_date = f"\n ---- Created At : {current_date} -----"

intro = intro + intro_date

border = "*" * 80

intro = f"{border} \n {intro} \n {border}"

print(intro)

