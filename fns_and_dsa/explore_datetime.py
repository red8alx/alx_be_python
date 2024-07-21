import datetime
def display_current_datetime():
    x = datetime.datetime.now()
    current_date = x.strftime("%c")
    print(f"Current date and time: {x}")
display_current_datetime()


