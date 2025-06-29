import os
import sqlite3
from datetime import datetime

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
    print("edit task name - change the name of an already existing task")
    print("edit due date - change the due date of an already existing taskexi")
    print("view - view all tasks")
    print("reset - delete all tasks")
    print("exit - exit the program")

    return input()

def current_tasks():

    print("\ncurrent tasks:")
    c.execute("SELECT rowid, * FROM tasks")
    all_items = c.fetchall()
    conn.commit()
    if len(all_items) < 1:
        print("no added tasks")
        return

    for index in range(len(all_items)):
        task_due_date = datetime.strptime(all_items[index][2], format_data)

        print(f"{str(index+1)}. {all_items[index][1]} due {task_due_date.strftime('%B %-d, %Y')} at {task_due_date.strftime('%-H:%M')}, currently {all_items[index][3]}")
        
def check_status(input_due_date):
    task_due_date = datetime.strptime(input_due_date, format_data)
    current_datetime = datetime.now()
    if task_due_date < current_datetime:
        return "missing"
    else:
        return "upcoming"

def print_result(result_text):
    clear_terminal()
    if result_text != "No result":
        print(result_text)
    current_tasks()


format_data = "%m/%d/%y %H:%M"

conn = sqlite3.connect('tasks.db')
c = conn.cursor()

# create the table if it doesn't already exist
c.execute("""CREATE TABLE IF NOT EXISTS tasks (
        name text,
        due_date text,
        status text
          
    )""")



while True:

    choice = get_input()

    if choice == "add":
        clear_terminal()

        print("name of task you want to add")
        new_task = input()

        print("date when the task is due: [MM/DD/YY HH:MM]")
        input_time = input()

        
        add_to_database = (new_task, input_time, check_status(input_time))
        c.execute("INSERT INTO tasks VALUES (?, ?, ?)", add_to_database)
        conn.commit()
        print_result("task sucessfully added")


    if choice == "remove":
        clear_terminal()
        print("number of the task you want to remove")
        current_tasks()
        input_to_remove = int(input())
        
        c.execute("SELECT rowid, * FROM tasks")
        conn.commit()
        all_items = c.fetchall()

        c.execute("DELETE from tasks WHERE rowid = (?)", (all_items[input_to_remove-1][0],))
        conn.commit()
        print_result("task sucessfully removed")


    if choice == "edit task name":
        clear_terminal()
        print("number of the task you want to replace")
        current_tasks()
        replacement_index = input()
        clear_terminal()
        print("name of which you want to use to replace")
        replacement = input()

        c.execute("SELECT rowid, * FROM tasks")
        conn.commit()
        all_items = c.fetchall()

        c.execute("""UPDATE tasks SET name = (?)
                  WHERE rowid = (?)""", (replacement, all_items[int(replacement_index)-1][0]))
        conn.commit()

        # tasks[int(replacement_index)-1] = replacement
        print_result("task sucessfully replaced")


    if choice == "edit due date":
        clear_terminal()
        print("number of the task you want to replace")
        current_tasks()
        replacement_index = input()
        clear_terminal()
        print("due date of which you want to use to replace")
        replacement = input()

        c.execute("SELECT rowid, * FROM tasks")
        conn.commit()
        all_items = c.fetchall()

        c.execute("""UPDATE tasks SET due_date = (?)
                    WHERE rowid = (?)""", (replacement, all_items[int(replacement_index)-1][0]))
        c.execute("""UPDATE tasks SET status = (?)
                    WHERE rowid = (?)""", (check_status(replacement), all_items[int(replacement_index)-1][0]))
        conn.commit()

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
    c.execute("SELECT rowid, * FROM tasks")
    all_items = c.fetchall()
    for item in all_items:
        new_status = check_status(item[2])
        c.execute("""UPDATE tasks SET status = (?)
                    WHERE rowid = (?)""", (new_status, item[0],))
    conn.commit()
