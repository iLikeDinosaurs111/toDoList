import os

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
    for i in range(len(tasks)):
        print(str(i+1) + ". " + tasks[i])

def print_result(result_text):
    clear_terminal()
    if result_text != "No result":
        print(result_text)
    current_tasks()

def save_list_to_file(name_of_list):

    with open("tasks.txt", "w") as file:
        for item in tasks:
            if item != "": 
                file.write(item + "~")




file = open("tasks.txt", "a")
read_file = open("tasks.txt")

tasks = []
build = ""
for character in read_file.read():
    if character != "~":
        build += character
    else:
        tasks.append(build)
        build = ""



while True:

    choice = get_input()

    if choice == "add":
        clear_terminal()
        print("name of task you want to add")
        new_task = input()
        if new_task in tasks:
            print_result("no duplicates allowed")
            pass
        tasks.append(new_task)
        save_list_to_file(tasks)
        print_result("task sucessfully added")


    if choice == "remove":
        clear_terminal()
        print("number of the task you want to remove")
        current_tasks()
        to_remove = input()
        del tasks[int(to_remove)-1]
        save_list_to_file(tasks)
        print_result("task sucessfully removed")


    if choice == "replace":
        clear_terminal()
        print("number of the task you want to replace")
        current_tasks()
        replacement_index = input()
        clear_terminal()
        print("name of which you want to use to replace")
        replacement = input()
        tasks[int(replacement_index)-1] = replacement
        save_list_to_file(tasks)
        print_result("task sucessfully replaced")

    
    if choice == "view":
        print_result("No result")


    if choice == "reset":
        tasks = []
        print_result("task sucessfully reset")
        save_list_to_file(tasks)
        

    if choice == "exit":
        print_result("No result")
        break
