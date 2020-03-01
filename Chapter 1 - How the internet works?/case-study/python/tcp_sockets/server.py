#SERVER
# Run netstat -an to check the current socket server running refer to TCP_HOST and TCP_PORT
# Or lsof -i -n
# netstat -an | grep <port_number>

import socket

def get_address_family_ipv4():
    return socket.AF_INET

def get_socket_stream():
    return socket.SOCK_STREAM

def create_socket():
    af_ipv4 = get_address_family_ipv4()
    socket_stream = get_socket_stream()
    server = socket.socket(af_ipv4, socket_stream)
    server.bind((TCP_IP, TCP_PORT))
    server.listen(1)
    connection, addr = server.accept()
    run(connection)
    
def run(connection):
    print(f"Connection ${connection}")
    while IS_RUNNING:
        data = connection.recv(BUFFER_SIZE)
        if not data:
            break
        print(f"Received data ${data}")
        connection.send(data)
    connection.close()

def main():
    create_socket()

if __name__ == "__main__":
    print("....")
    print("Server is running")
    IS_RUNNING = True
    TCP_IP = "127.0.0.1"
    TCP_PORT = 5005
    BUFFER_SIZE = 500
    main()