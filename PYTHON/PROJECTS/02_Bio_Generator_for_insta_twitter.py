
name = input("Enter your name: ")
username = input("Enter your username: ")
profession = input("What do you do? ")
skills = input("Your top skills (comma separated): ")
passion = input("What are you passionate about? ")
current_goal = input("What are you currently building/learning? ")
location = input("Your location: ")
emoji = input("Favorite emoji: ")
website = input("Portfolio/GitHub/Website (optional): ")

url = f"{website}"

bio = f"""
{emoji} {name}
{profession}

💻 {passion}
📚 Currently: {current_goal}
🛠️ Skills: {skills}
📍 {location}

🔗 {website}
"""

output_text = input(f"Do you want to save your Bio in .txt file? (yes/no): ").lower().strip()

if output_text == "yes" :
    txt_file_name = input("Write your file name (without .txt) : ").strip()
    with open(f"{txt_file_name}.txt", "w", encoding="utf-8") as f :
        f.write(bio)

    print("File created successfully")
elif output_text == "no" :
    print(bio)
else :
    print("Please enter only 'yes' or 'no")
