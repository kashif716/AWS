import os 

command = "uptime"
command = "date"
command = "df -h"


def check_cpu(command):
    print(os.system(command))


def run_command(command):
    return(os.system(command))


import os
import datetime
def show_time():
    return datetime.datetime.today()
today = show_time()
print(today)