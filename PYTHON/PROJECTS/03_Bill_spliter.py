
total_bill = int(input("Enter total bill: "))

no_of_people = int(input("Enter the number of people: "))
peoples = []

for i in range(no_of_people) :
    people = input("")
    peoples.append(people)

per_person = round(total_bill / no_of_people, 2)

for i in range(len(peoples)) :
    print(f"{peoples[i]} owes : Rs {per_person}")





