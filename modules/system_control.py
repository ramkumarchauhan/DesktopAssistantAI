import os
import subprocess

def system_control(action):
    if action == 'restart':
        subprocess.call(['shutdown', '/r', '/t', '1'])
    elif action == 'shutdown':
        subprocess.call(['shutdown', '/s', '/t', '1'])
    elif action == 'sleep':
        os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
    else:
        print("Invalid system action. Please specify 'restart', 'shutdown', or 'sleep'.")
