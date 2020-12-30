from os import replace
import socket
from logging_module import *

BUFF_SIZE = 1024

def parse_header(request_content: bytes) -> dict:
    
    headers = request_content[0:request_content.find(b"\r\n\r\n")]
    str_request = request_content.decode("utf8")
    lst_request = str_request.split('\r\n')

    # Get url of the request
    pos1 = lst_request[0].find('/')
    pos2 = lst_request[0].find('HTTP')
    str_url = lst_request[0][pos1:pos2-1]
    dict_headers = {"URL":str_url}

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
    else method = "UNK"
    dict_headers.update({"Method":method})

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
    pass

def recvall(s: socket.socket):
    pass

def handle_http_request(c: socket.socket, a: tuple):

    # Receive data from client
    request_content = recvall(c)
    
    # parse request header
    request_headers = parse_header(request_content)
    dict_hostPort = get_target_info(request_headers)
    
    # Get host and port of the destination server
    host = dict_hostPort["hostname"]
    port = dict_hostPort["port"]

    # Send request data of client to destination server
    a.sendall(bytes(request_content,"utf8"))
    # Forward server's reply to client

    # Close connection