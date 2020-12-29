from os import replace
import socket
from logging_module import *

BUFF_SIZE = 1024

def parse_header(request_content: bytes) -> dict:
    str_request = request_content.decode("utf8")
    lst_request = str_request.split('\r\n')
    pos1 = lst_request[0].find('/')
    pos2 = lst_request[0].find('html')
    str_url = lst_request[0][pos1:pos2+4]
    dict_headers = {"URL":str_url}
    splitedlist = [i.split(':') for i in lst_request]
    i = 1
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
    pass