import sqlite3
from datetime import datetime

format_data = "%m/%d/%y %H:%M"

def check_status(input_due_date):
    task_due_date = datetime.strptime(input_due_date, format_data)
    current_datetime = datetime.now()
    if task_due_date < current_datetime:
        return "missing"
    else:
        return "upcoming"


def update_statuses(database_name, table_name):
    conn = sqlite3.connect(database_name)
    c = conn.cursor()

    c.execute(f"SELECT rowid, * FROM {table_name}")
    all_items = c.fetchall()
    for item in all_items:
        new_status = check_status(item[2])
        c.execute("""UPDATE tasks SET status = (?)
                    WHERE rowid = (?)""", (new_status, item[0],))
        
    conn.commit()
    conn.close()


def add_one_task(name, due_date):
    conn = sqlite3.connect('tasks.db')
    c = conn.cursor()

    c.execute("INSERT INTO tasks VALUES (?, ?, ?)", (name, due_date, check_status(due_date)))

    conn.commit()
    conn.close()


def remove_row(database_name, table_name, remove_index):
    conn = sqlite3.connect(database_name)
    c = conn.cursor()

    c.execute(f"SELECT rowid, * FROM {table_name}")
    conn.commit()
    all_items = c.fetchall()

    c.execute("DELETE from tasks WHERE rowid = (?)", (all_items[remove_index][0],))

    conn.commit()
    conn.close()


def get_column_names(database_name, table_name):
    conn = sqlite3.connect(database_name)
    c = conn.cursor()

    c.execute(f"PRAGMA table_info({table_name})")
    columns_info = c.fetchall()

    column_names = [column[1] for column in columns_info]  # column[1] is the name
    conn.close()
    return column_names


def edit_task_value(column_to_replace, replacement_index, replacement):
    conn = sqlite3.connect("tasks.db")
    c = conn.cursor()
    column_to_replace = column_to_replace.replace(" ", "_")
    c.execute("SELECT rowid, * FROM tasks")
    conn.commit()
    all_items = c.fetchall()

    allowed_columns = {"name", "due_date", "status"}
    if column_to_replace in allowed_columns:
        c.execute(f"UPDATE tasks SET {column_to_replace} = ? WHERE rowid = ?", (replacement, all_items[replacement_index][0]))
    else:
        raise ValueError("aw hell nah it didnt work")
    conn.commit()
    conn.close()

def print_all_tasks():
    conn = sqlite3.connect("tasks.db")
    c = conn.cursor()

    int("\ncurrent tasks:")
    c.execute("SELECT rowid, * FROM tasks")
    all_items = c.fetchall()
    conn.commit()
    if len(all_items) < 1:
        print("no added tasks")
        return

    for index in range(len(all_items)):
        task_due_date = datetime.strptime(all_items[index][2], format_data)

        print(f"{str(index+1)}. {all_items[index][1]} due {task_due_date.strftime('%B %-d, %Y')} at {task_due_date.strftime('%-H:%M')}, currently {all_items[index][3]}")
    conn.close()