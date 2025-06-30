import os
import sqlite3
from datetime import datetime
import dbOperations
import utility


def clear_terminal():
    """Clears the terminal screen."""
    if os.name == 'nt':  # For Windows
        os.system('cls')
    else:  # For macOS and Linux
        os.system('clear')
        # pass


def get_input():

    print("\noptions")
    print("add - add a task")
    print("remove - remove a task (cannot be undone)")
    print("edit - change the name or due date of an already existing task")
    print("mark as done - mark a task as done")
    print("view - select the kind of task you want to view")
    print("reset - delete all tasks (cannot be undone)")
    print("exit - exit the program")

    return input()


def print_result(result_text):
    clear_terminal()
    if result_text != "No result":
        print(result_text)
    dbOperations.print_all_tasks()


def check_dblength_compatability(database_name, table_name):
    if dbOperations.check_rows_length(database_name, table_name) < 1:
        print("no tasks to complete action with")
        return True


conn = sqlite3.connect('tasks.db')
c = conn.cursor()

# create the table if it doesn't already exist
c.execute("""CREATE TABLE IF NOT EXISTS tasks (
        name text,
        due_date text,
        status text
          
    )""")


format_data = "%m/%d/%y %H:%M"

while True:

    choice = get_input()

    if choice == "add":
        clear_terminal()

        print("name of task you want to add")
        new_task = input()

        print("date when the task is due: (MM/DD/YY HH:MM)")
        input_time = input()
        if utility.check_format("datetime", input_time) == False:
                print_result("your input does not match the correct format, please try again")
                continue

        
        dbOperations.add_one_task(new_task, input_time)
        print_result("task sucessfully added")


    if choice == "remove":
        clear_terminal()

        if check_dblength_compatability('tasks.db', 'tasks'):
            continue

        print("number of the task you want to remove")
        dbOperations.print_all_tasks()
        index_to_remove = input()

        if utility.check_format("int", index_to_remove) == False:
                print_result("your input does not match the correct format, please try again")
                continue


        index_to_remove = int(index_to_remove)-1
        
        if index_to_remove >= 0 and index_to_remove <= dbOperations.check_rows_length("tasks.db", 'tasks')-1:

            dbOperations.remove_row('tasks.db', 'tasks', index_to_remove)
        else:
            print_result("there is no task with this number")
            continue
        
        print_result("task sucessfully removed")


    if choice == "edit":
        clear_terminal()

        if check_dblength_compatability('tasks.db', 'tasks'):
            continue

        print("number of the task you want to edit")
        dbOperations.print_all_tasks()

        replacement_index = input()
        if utility.check_format("int", replacement_index) == False:
                print_result("your input does not match the correct format, please try again")
                continue
        replacement_index = int(replacement_index)-1

        if replacement_index >= 0 and replacement_index <= dbOperations.check_rows_length("tasks.db", 'tasks')-1:

            dbOperations.remove_row('tasks.db', 'tasks', index_to_remove)
        else:
            print_result("there is no task with this number")
            continue

        print("what part of this task do you want to edit: (name / due date)")
        column_name = input()

        clear_terminal()
        if column_name == "name":
            print("enter replacement name")
            replacement = input()
        elif column_name == "due date":
            print("enter replacement date: (MM/DD/YY HH:MM)")
            replacement = input()
            if utility.check_format("datetime", replacement) == False:
                print_result("your input does not match the correct format, please try again")
                continue
        else:
            print_result("your input is not an available option")
            continue


        dbOperations.edit_task_value(column_name, replacement_index, replacement)

        # tasks[int(replacement_index)-1] = replacement
        print_result("task sucessfully modified")


    if choice == "mark as done":
        clear_terminal()

        if check_dblength_compatability('tasks.db', 'tasks'):
            continue

        print("number of the task you want to mark as done")
        dbOperations.print_all_tasks()
        index_to_remove = int(input())
        index_to_remove -= 1
        
        dbOperations.mark_as_done(index_to_remove)
        
        print_result("task sucessfully marked as done")


    if choice == "view":
        clear_terminal()
        print("what do you want to view?: (all / missing / upcoming / done)")
        kind = input()

        if kind == "all":
            dbOperations.print_all_tasks()
        elif kind == "missing":
            dbOperations.print_all_tasks_of_a_kind('missing')
        elif kind == "upcoming":
            dbOperations.print_all_tasks_of_a_kind('upcoming')
        elif kind == "done":
            dbOperations.print_all_tasks_of_a_kind('done')


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
