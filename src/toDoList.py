import os
from datetime import datetime
import fileOperations 

def clear_terminal():
    
    """Clears the terminal screen."""
    if os.name == 'nt':  # For Windows
        os.system('cls')
    else:  # For macOS and Linux
        os.system('clear')

def get_input():
    clear_terminal()
    current_tasks()

    print("\noptions")
    print("add - add a task and its due date")
    print("remove - remove a task entirely")
    print("edit task name - change the name of an already-existing task" )
    print("edit due date - change the due date of an already-existing task" )
    print("view - view all tasks and due dates")
    print("reset - delete all tasks")
    print("exit - exit the program")

    return input()

def current_tasks():

    print("\ncurrent tasks:")
    if len(tasks) == 0:
        print("no added tasks")
        return
    
    for i in range(len(tasks)):
        selected_dictionary = tasks[i]
        due_date = datetime.strptime(selected_dictionary["due_date"], format_data)
        print(str(i+1) + ". " + selected_dictionary["name"] + " due " + str(due_date.strftime("%B")) + " " + str(due_date.strftime("%-d") + ", " + str(due_date.strftime("%Y"))) + " at " + str(due_date.strftime("%-H")) + ":" + str(due_date.strftime("%M")) + ", currently " + selected_dictionary["status"]) 
        
def print_result(result_text):

    clear_terminal()
    if result_text != "No result":
        print(result_text)
    current_tasks()

def add_dict_to_list(list, task_name, task_due_date):
    dictionary = {
        "name": task_name,
        "due_date": task_due_date,
    }

    task_datetime = datetime.strptime(task_due_date, format_data)
    current_datetime = datetime.now()

    if task_datetime < current_datetime:
        dictionary["status"] = "missing"
    elif task_datetime > current_datetime:
        dictionary["status"] = "upcoming"

    list.append(dictionary)
    # print(list)

tasks = []
fileOperations.init_load_from_file("tasks.txt", tasks)

format_data = "%d/%m/%y %H:%M"

while True:
    
    choice = get_input()

    if choice == "add":
        clear_terminal()

        print("name of task you want to add")
        new_task = input()

        print("date when the task is due: [DD/MM/YY HH:MM]")
        input_time = input()

        task_due_date = datetime.strptime(input_time, format_data)

        add_dict_to_list(tasks, new_task, input_time)

        fileOperations.save_list_to_file("tasks.txt", tasks)
        print_result("task sucessfully added")


    if choice == "remove":
        clear_terminal()
        print("number of the task you want to remove")
        current_tasks()
        to_remove = input()

        del tasks[int(to_remove)-1]


        fileOperations.save_list_to_file("tasks.txt", tasks)
        print_result("task sucessfully removed")


    if choice == "edit task name":
            clear_terminal()
            print("number of the task you want to edit the name of")
            current_tasks()
            replacement_index = input()
            # clear_terminal()
            print("the new name of the task")
            replacement = input()

            dictionary = tasks[int(replacement_index)-1]
            dictionary["name"] = replacement



            fileOperations.save_list_to_file("tasks.txt", tasks)
            print_result("task name sucessfully changed")


    if choice == "edit due date":
        clear_terminal()
        print("number of the task you want to change the due date of")
        current_tasks()
        replacement_index = input()
        # clear_terminal()
        print("new date when the task is due: [DD/MM/YY HH:MM]")
        replacement_time = input()

        dictionary = tasks[int(replacement_index)-1]
        print(dictionary)
        dictionary["due_date"] = replacement_time

        fileOperations.save_list_to_file("tasks.txt", tasks)
        print_result("task due date sucesfully changed")

    
    if choice == "view":
        print_result("No result")


    if choice == "reset":
        tasks = []
        print_result("task sucessfully reset")
        fileOperations.save_list_to_file("tasks.txt", tasks)
        

    if choice == "exit":
        print_result("No result")
        break
