import datetime

def get_date_time():
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M")
    current_date = now.strftime("%Y-%m-%d")
    print(f"The current time is {current_time} and the date is {current_date}.")
