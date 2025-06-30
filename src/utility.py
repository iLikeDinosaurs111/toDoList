from datetime import datetime

format_data = "%m/%d/%y %H:%M"


def check_format(format, input):
    if format == "datetime":
        try:
            due_date = datetime.strptime(input, format_data)
        except Exception:
            return False
    elif format == "int":
        try:
            input = str(int(input))
        except Exception:
            return False
    return True
            