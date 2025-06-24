from datetime import datetime

format_data = "%d/%m/%y %H:%M"

def init_load_from_file(file_name, tasks_list):
    # file = open("tasks.txt", "a")
    read_file = open(file_name)
    for item in read_file.readlines():
        parts = item.split("~")
        tasks_list[parts[0]] = datetime.strptime(parts[1].strip(), format_data)

def save_list_to_file(file_name, tasks_list):
    with open(file_name, "w") as file:
        tasks_keys = list(tasks_list.keys())
        for key, value in tasks_lists.items():
            file.write(key + "~" + str(value.strftime(format_data)) + "\n")