from datetime import datetime

format_data = "%d/%m/%y %H:%M"

def init_load_from_file(file_name, tasks_list):
    # file = open("tasks.txt", "a")
    read_file = open(file_name)
    for item in read_file.readlines():
        parts = item.split("~")
        # print(parts)
        # print(parts[1].strip())
        dictionary = {
            "name": parts[0],
            "due_date": parts[1].strip(),
        }
        task_datetime = datetime.strptime(parts[1], format_data)
        current_datetime = datetime.now()

        # print(dictionary)

        if task_datetime < current_datetime:
            dictionary["status"] = "missing"
        elif task_datetime > current_datetime:
            dictionary["status"] = "upcoming"

        # print(dictionary)
        tasks_list.append(dictionary)


def save_list_to_file(file_name, tasks_list):
    with open(file_name, "w") as file:
        for dictionary in tasks_list:
            build = ""
            for key, value in dictionary.items():
                build += str(value) + "~"
            file.write(build + "\n")


        # tasks_keys = list(tasks_list.keys())
        # for key, value in tasks_list.items():
        #     file.write(key + "~" + str(value.strftime(format_data)) + "\n")
            
