# Python has a library that uses IPC for computer networks which provides low-level internet networking interface

# Author: John Royce Punay
# Date created: February 29, 2020 7:19 PM
# CLIENT
import socket

def get_address_family_ipv4():
    return socket.AF_INET

def get_socket_stream():
    return socket.SOCK_STREAM

def connect():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((TCP_IP, TCP_PORT))
    s.send(MESSAGE)
    data = s.recv(BUFFER_SIZE)
    s.close()
    print(f"From client received ${data}")

if __name__ == "__main__":
    TCP_IP = "127.0.0.1"
    TCP_PORT = 5005
    BUFFER_SIZE = 1024
    MESSAGE = b"Hello, World!"
    connect()