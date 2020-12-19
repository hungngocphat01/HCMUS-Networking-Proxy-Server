import datetime
from termcolor import colored
import sys

def log(message, iserror=False):
    now = datetime.datetime.now().strftime("[%d-%m-%Y %H:%M:%S]")
    
    color = "blue"
    if (iserror):
        color = "red"

    buffer = f"{colored(now, color)} {message}"
    # Print log to stdout and stderr
    print(buffer)