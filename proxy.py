#! /usr/bin/python3
import sys
import socket
import traceback
import threading
import requesthndl_module

# Global constants
MAX_RECV_SIZE = 4096
BACKLOG = 5

# Server socket initialization
server_socket = None

def create_new_handler(c, a, req):
    handler = threading.Thread(name=f"{a[0]} Handler", target=handle_http_request, args=(c, req))
    handler.setDaemon = True
    handler.start()
    return handler

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
            req = recvall(c)
            create_new_handler(c, a, req)
        
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
    