import socket
import logging_module

def parse_header(request_content: bytes) -> dict:
    pass

def is_blocked(url: str) -> bool:
    pass

def get_target_info(header: dict) -> dict:
    pass

def send_403_forbidden(client_socket: socket.socket):
    pass

def recvall(socket: socket.socket) -> bytes:
    pass

def handle_http_request(c: socket.socket, request_content: bytes):
    pass