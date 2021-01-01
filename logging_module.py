import datetime
from termcolor import colored
import sys

def log(message, color="blue"):
    now = datetime.datetime.now().strftime("[%d-%m-%Y %H:%M:%S]")

    buffer = f"{colored(now, color)} {message}"
    # Print log to stdout and stderr
    print(buffer)