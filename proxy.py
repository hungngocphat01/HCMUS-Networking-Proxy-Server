#! /usr/bin/python3
import sys
import socket
import traceback
import threading
from requesthndl_module import *

# Global constants
MAX_RECV_SIZE = 4096
PORT = 8888
BACKLOG = 10

# Server socket initialization
server_socket = None

def main():
    log(f"Proxy server started at port 8888.")
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    server_socket.bind(("", 8888))
    server_socket.listen(BACKLOG)

    while True:
        log(f"Waiting for new connection.")
        client_socket, client_addr = server_socket.accept()
        log(f"{client_addr} Accepted connection.")

        d = threading.Thread(target=handle_http_request, args=(client_socket, client_addr))
        d.setDaemon(True)
        d.start()

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
    