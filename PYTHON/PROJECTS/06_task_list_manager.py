

"""
    1. Add the task
    2. View Task
    3. display Task
    4. EXit

"""


import os
TASKS_FILE = "tasks.txt"

def load_task () :
    tasks = []
    if os.path.exists(TASKS_FILE) :
        with open(TASKS_FILE, "r" , encoding="utf-8") as f :
            for line in f:
                text, status = line.strip().rsplit("||", 1)
                tasks.append({"text" : text, "done" : status == "done"})

    return tasks

def save_task (tasks) :
    if not tasks :
        print(f"Task not found")
    else :
        with open(TASKS_FILE, "w", encoding="utf-8") as f:
            for task in tasks :
                status = "done" if task["done"] else "not done"
                f.write(f"{task['text']} || {status} \n")

def display_task (tasks) : 
    if not tasks :
        print(f"Task is not to display")
    else :
        for i, task in enumerate(tasks) :
            checkbox = "✅" if task["done"] else " "
            print(f"{i+1}. [{checkbox}] {task['text']}")

    print()


def task_manager () :
    tasks = load_task()

    while True:
        print("\n ---------- Task List manager ----------")
        print("1. Add the task")
        print("2. view task")
        print("3. Mark as a complete")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice (1-5) : ")

        match choice :
            case "1" :
                text = input("Add Task: ").strip()
                if text :
                    tasks.append({"text" : text, "done" : False})
                    save_task(tasks)

            case "2" :
                display_task(tasks)

            case "3" :
                display_task(tasks)
                try :
                    num = int(input("Enter the task number: "))
                    if 1<= num <= len(tasks) :
                        tasks[num-1]["done"] = True
                        save_task(tasks)
                        print("Task completed")

                    else :
                        print("Invalid Number")
                except ValueError:
                    print("Please enter the number")

            case "4" :
                display_task(tasks)
                try :
                    num = int(input("Enter the task number: "))
                    if 1<= num <= len(tasks) :
                        removed = tasks.pop(num - 1)
                        save_task(tasks)
                        print(f"Task removed : {removed['text']}")
                    else :
                        print("Invalid Number")
                except ValueError:
                    print("Please enter the number")

            case "5" :
                print("Exiting Task Manager")
                break

            case _:
                print("Please choose the valid number")


task_manager()