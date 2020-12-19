#! /usr/bin/python3
import socket
import traceback
import threading
import reqhndl_module

# Global constants
MAX_RECV_SIZE = 4096
BACKLOG = 5

# Server socket initialization
server_socket = None

# (2) functions here

# (1) functions here
def request_handling(c, a):
    pass

def create_new_handler(c, a):
    handler = threading.Thread(name=f"{a[0]} Handler", target=request_handling, args=(c, a))
    handler.setDaemon = True
    handler.start()
    return handler

def log(message, iserror=False):
    now = datetime.datetime.now().strftime("[%d-%m-%Y %H:%M:%S]")
    
    color = "green"
    if (iserror):
        color = "red"

    buffer = f"{colored(now, color)} {message}"
    # Print log to stdout and stderr
    print(buffer)

def main():
    if (len(sys.argv) <= 1):
        log("Port not specified.\nExample: python3 proxy.py 8888")

    # Server socket is the socket used to interface with the client
    global server_socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    server_socket.bind(("", sys.argv[1]))
    server_socket.listen(1)

    while True:
        c, a = server_socket.accept(BACKLOG)
        if (c):
            log(f"Accepted connection from {a}")
            create_new_handler(c, a)
        
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        log("Termination signal detected.")
    except Exception:
        log(traceback.format_exc(), iserror=True)
    finally:
        log("Closing server socket.")
        if (server_socket is not None):
            server_socket.close()
        log("Force stopping any running threads.")
        sys.exit()
        
