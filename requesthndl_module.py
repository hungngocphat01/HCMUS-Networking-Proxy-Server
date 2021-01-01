from os import replace
import socket
from logging_module import *

BUFFER_SIZE = 1024

def parse_header(request_content: bytes) -> dict:

    headers = request_content[0:request_content.find(b"\r\n\r\n")]
    str_request = headers.decode("utf-8")
    lst_request = str_request.split('\r\n')

    # Get url of the request
    pos1 = lst_request[0].find('/')
    pos2 = lst_request[0].find('HTTP')
    str_url = lst_request[0][pos1:pos2-1]
    dict_headers = {"URI":str_url}

    # Get host information
    lst_host = lst_request[1].split(':')
    # If host contains port number
    if len(lst_host) == 3:
        dict_headers.update({lst_host[0]:lst_host[1]+':'+lst_host[2]})
    else:
        dict_headers.update({lst_host[0]:lst_host[1]})

    # Get method information
    if any("GET" in s for s in lst_request):
        method = "GET"
    elif any("POST" in s for s in lst_request):
        method = "POST"
    else:
        method = "UNK"
    dict_headers.update({"Method": method})

    # Add other values to dict
    splitedlist = [i.split(':') for i in lst_request]
    i = 2
    while i < len(splitedlist)-1:
        dict_headers.update({splitedlist[i][0]: splitedlist[i][1]})
        i = i + 1
    return dict_headers

def is_blocked(url: str) -> bool:
    pass
    

def get_target_info(header: dict) -> dict:
    pass


def send_403_forbidden(client_socket: socket.socket):
    client_socket.send(b'HTTP/1.1 403 Forbidden\r\n\r\n<html>\r\n<title>403 Forbidden</title>\r\n<body>\r\n'
                        b'<h1>Error 403: Forbidden</h1>\r\n<p>The requested websit violates our administrative policies.</p>'
                        b'</body>\r\n</html>\r\n')
    client_socket.close()

def recvall(s: socket.socket):
    pass


def handle_http_request(c: socket.socket, a: tuple):
    # Receive data from client
    request_content = recvall(c)
    log(f"{a} Request retrieved.")
    
    # parse request header
    request_headers = parse_header(request_content)
    dict_hostPort = get_target_info(request_headers)
    
    # Check method whether it is POST or GET
    method = request_headers["Method"]
    if(method != "GET" and method != "POST"):
        c.close()
        return

    # Check if the url is blocked or not
    isBlocked = is_blocked(request_headers["URI"])
    if isBlocked:
        send_403_forbidden(c)
        return
    # Get host and port of the destination server
    host = dict_hostPort["host"].strip()
    port = dict_hostPort["port"]

    # Send request data of client to destination server
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.connect((host, port))
    server_socket.sendall(request_content)
    # Forward server's reply to client

    log(f"{a} Forwarding: {request_headers['URI']}")
    with server_socket:
        while True:
            # Transfering 4 KB can't be slower than 1.5s in normal condition
            server_socket.settimeout(1.5)
            reply = b""
            try:
                reply = server_socket.recv(BUFFER_SIZE)
            except socket.timeout:
                pass
            if not reply:
                break
            c.sendall(reply)
    log(f"{a} Forwarded: {request_headers['URI']}")
    
    # Close connection
    server_socket.close()
    c.close()

    log(f"{a} Connection closed.")
    return