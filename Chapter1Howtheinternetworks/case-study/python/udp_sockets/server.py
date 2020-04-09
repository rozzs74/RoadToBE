import socket



def get_address_family_ipv4():
    return socket.AF_INET

def get_socket_data_gram():
    return socket.SOCK_DGRAM

def create_socket():
    af_ipv4 = get_address_family_ipv4()
    upd_dgram = get_socket_data_gram()
    server = socket.socket(af_ipv4, upd_dgram)
    server.bind(("127.0.0.1", 6000))

    return server

def init_event_loop(server):
    while True:
        data = server.recv(500)
        if not data: 
            break
        print(f"Received data {data}")

def main():
    connection = create_socket()
    init_event_loop(connection)
    

if __name__ == "__main__":
    main()