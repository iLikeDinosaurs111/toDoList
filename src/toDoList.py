import os
import sqlite3
from datetime import datetime
import dbOperations


def clear_terminal():
    """Clears the terminal screen."""
    if os.name == 'nt':  # For Windows
        os.system('cls')
    else:  # For macOS and Linux
        # os.system('clear')
        pass

def get_input():

    print("\noptions")
    print("add - add a task")
    print("remove - remove a task")
    print("edit task value - change the name or due date of an already existing task")
    print("view - view all tasks")
    print("reset - delete all tasks")
    print("exit - exit the program")

    return input()



def print_result(result_text):
    clear_terminal()
    if result_text != "No result":
        print(result_text)
    dbOperations.print_all_tasks()


format_data = "%m/%d/%y %H:%M"

conn = sqlite3.connect('tasks.db')
c = conn.cursor()

# create the table if it doesn't already exist
c.execute("""CREATE TABLE IF NOT EXISTS tasks (
        name text,
        due_date text,
        status text
          
    )""")

print(dbOperations.get_column_names("tasks.db", 'tasks'))

while True:

    choice = get_input()

    if choice == "add":
        clear_terminal()

        print("name of task you want to add")
        new_task = input()

        print("date when the task is due: (MM/DD/YY HH:MM)")
        input_time = input()

        
        dbOperations.add_one_task(new_task, input_time)
        print_result("task sucessfully added")


    if choice == "remove":
        clear_terminal()
        print("number of the task you want to remove")
        dbOperations.print_all_tasks()
        index_to_remove = int(input())
        index_to_remove -= 1
        
        dbOperations.remove_row('tasks.db', 'tasks', index_to_remove)
        
        print_result("task sucessfully removed")


    if choice == "edit task values":
        clear_terminal()
        print("number of the task you want to replace")
        dbOperations.print_all_tasks()
        replacement_index = int(input())
        replacement_index -= 1

        print("what part of this task do you want to edit: (name / due date)")
        column_name = input()

        clear_terminal()
        if column_name == "name":
            print("enter replacement name")
        elif column_name == "due date":
            print("enter replacement date: (MM/DD/YY HH:MM)")
        replacement = input()


        dbOperations.edit_task_value(column_name, replacement_index, replacement)

        # tasks[int(replacement_index)-1] = replacement
        print_result("task sucessfully replaced")


    if choice == "view":
        print_result("No result")
    

    if choice == "reset":
        
        c.execute("SELECT rowid, * FROM tasks")
        conn.commit()
        all_items = c.fetchall()

        c.execute("DELETE from tasks WHERE rowid > -10")
        conn.commit()

        print_result("task sucessfully reset")


    if choice == "exit":
        clear_terminal()
        print_result("No result")
        conn.close()
        break

    # make sure all status is up to date
    dbOperations.update_statuses('tasks.db', 'tasks')
