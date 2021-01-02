#! /usr/bin/python3
import sys
import threading
from requesthndl_module import *

# Global constants
PORT = 8888
BACKLOG = 10

# Server socket initialization
server_socket = None

def main():
    log(f"Proxy server started at port {PORT}.")
    log("Waiting for new connection.")
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    server_socket.bind(("", 8888))
    server_socket.listen(BACKLOG)

    while True:
        client_socket, client_addr = server_socket.accept()
        log(f"{client_addr} Accepted connection.", color="green")

        d = threading.Thread(target=handle_http_request, args=(client_socket, client_addr))
        d.setDaemon(True)
        d.start()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        log("Termination signal detected.")
    except Exception:
        log(traceback.format_exc(), color="red")
    finally:
        log("Closing server socket.")
        if (server_socket is not None):
            server_socket.close()
        log("Force stopping any running threads.")
        sys.exit()
    