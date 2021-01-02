import datetime
from termcolor import colored
import sys

def log(message, color="blue", newline=False):
    now = datetime.datetime.now().strftime("[%d-%m-%Y %H:%M:%S]")

    buffer = f"{colored(now, color)} {message}"
    if (newline):
        buffer = "\n" + buffer
    # Print log to stdout
    print(buffer)

def req_log(request_info: dict):
    now = datetime.datetime.now().strftime("[%d-%m-%Y %H:%M:%S]")

    log("Request information", color="blue")
    log(f"Method: {request_info['Method']}", color="blue")
    log(f"URI: {request_info['URI']}", color="blue")
    if "Content-Type" in request_info.keys():
        log(f"Content-Type: {request_info['Content-Type']}", color="blue")
    print("\n")