def get_input():
    print("to do list")
    print("add - add a task")
    print("remove - remove a task")
    print("replace - replace a task" )
    print("view - view all tasks")
    print("reset - delete all tasks")
    return input()

def current_tasks():
    print("current tasks:")
    for i in range(len(tasks)):
        print(str(i+1) + ". " + tasks[i])

tasks = []
       
choice = get_input()
if choice == "add":
    print("name of task you want to add")
    to_add = input()
    tasks.append(to_add)
    print("task sucesfully added")
    current_tasks()
if choice == "remove":
    to_add = input()
    tasks.append(to_add)
    print("task sucesfully added")
    current_tasks()
    


