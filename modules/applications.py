import os

def open_application(application_name):
    try:
        os.system(f"start {application_name}")
        print(f"Opening {application_name}")
    except Exception as e:
        print(f"Error opening {application_name}: {e}")

def close_application(application_name):
    try:
        os.system(f"taskkill /f /im {application_name}")
        print(f"Closing {application_name}")
    except Exception as e:
        print(f"Error closing {application_name}: {e}")
