import os
from datetime import datetime

def clear_terminal():
    """Clears the terminal screen."""
    if os.name == 'nt':  # For Windows
        os.system('cls')
    else:  # For macOS and Linux
        os.system('clear')

def get_input():

    print("\noptions")
    print("add - add a task")
    print("remove - remove a task")
    print("replace - replace a task" )
    print("view - view all tasks")
    print("reset - delete all tasks")
    print("exit - exit the program")

    return input()

def current_tasks():

    print("\ncurrent tasks:")
    if len(tasks) == 0:
        print("no added tasks")
        return
    task_keys = list(tasks.keys())
    for i in range(len(task_keys)):
        due_date = tasks[task_keys[i]]
        print(str(i+1) + ". " + task_keys[i] + " due " + str(due_date.strftime("%B")) + " " + str(due_date.strftime("%-d") + ", " + str(due_date.strftime("%Y"))) + " at " + str(due_date.strftime("%-H")) + ":" + str(due_date.strftime("%M")))
    
    # print(tasks)

def print_result(result_text):
    clear_terminal()
    if result_text != "No result":
        print(result_text)
    current_tasks()

def save_list_to_file():
    # return
    with open("tasks.txt", "w") as file:
        tasks_keys = list(tasks.keys())
        for key, value in tasks.items():
            file.write(key + "~" + str(value.strftime(format_data)) + "\n")


format_data = "%d/%m/%y %H:%M"

file = open("tasks.txt", "a")
read_file = open("tasks.txt")

tasks = {}

for item in read_file.readlines():
    parts = item.split("~")
    tasks[parts[0]] = datetime.strptime(parts[1].strip(), format_data)

# build = ""
# for character in read_file.read():
#     if character != "~":
#         build += character
#     else:
#         tasks.append(build)
#         build = ""



while True:

    choice = get_input()

    if choice == "add":
        clear_terminal()

        print("name of task you want to add")
        new_task = input()

        print("date when the task is due: [DD/MM/YY HH:MM]")
        input_time = input()

        task_due_date = datetime.strptime(input_time, format_data)

        tasks[new_task] = task_due_date

        save_list_to_file()
        print_result("task sucessfully added")


    if choice == "remove":
        clear_terminal()
        print("number of the task you want to remove")
        current_tasks()
        to_remove = input()

        tasks_keys = list(tasks.keys())

        del tasks[tasks_keys[int(to_remove)-1]]


        save_list_to_file()
        print_result("task sucessfully removed")


    if choice == "replace":
        clear_terminal()
        print("number of the task you want to replace")
        current_tasks()
        replacement_index = input()
        # clear_terminal()
        print("date when the task is due: [DD/MM/YY HH:MM]")
        replacement_time = input()

        task_due_date = datetime.strptime(replacement_time, format_data)

        tasks_keys = list(tasks.keys())

        tasks[tasks_keys[int(replacement_index)-1]] = task_due_date
        save_list_to_file()
        print_result("task sucessfully replaced")

    
    if choice == "view":
        print_result("No result")


    if choice == "reset":
        tasks = {}
        print_result("task sucessfully reset")
        save_list_to_file()
        

    if choice == "exit":
        print_result("No result")
        break
