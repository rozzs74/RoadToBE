import socket


def create_socket():
    server =socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    MESSAGE = b"Hello, World!"
    server.connect(('127.0.0.1', 6000))
    server.send(MESSAGE)

def main():
    create_socket()
    pass

if __name__ == "__main__":
    main()