# I/O Multiplexing is handle multiple connection concurrently with the help of selectors
# Author: John Royce Punay
# Date created: March 1 2020 1:39PM

import selectors
import socket
import types
import sys

def close_sys():
    sys.exit(1)

def get_args():
    return sys.argv

def close_selectors():
    default_selector = get_default_selectors()
    default_selector.close()

def get_default_selectors():
    default_selector = selectors.DefaultSelector()
    return default_selector

def unregister_selector(current_server):
    default_selector = get_default_selectors()
    default_selector.unregister(current_server)
    return True

def register_selector(current_server, event, data=None):
    default_selector = get_default_selectors()
    default_selector.register(current_server, event, data)
    return True

def get_address_family_ipv4():
    return socket.AF_INET

def get_socket_stream():
    return socket.SOCK_STREAM

def create_socket():
    af_ipv4 = get_address_family_ipv4()
    socket_stream = get_socket_stream()
    server = socket.socket(af_ipv4, socket_stream)
    return { 
        "instance": server,
        "state": True
    }

def send_socket(current_server, data):
    return current_server.send(data)

def close_socket(current_server):
    current_server.close()
    return True

def bind_socket(current_server, tcp_ip, tcp_port_number):
    current_server.bind((tcp_ip, tcp_port_number))
    return True

def listen_socket(current_server):
    current_server.listen()
    return True

def accept_socket(current_server):
    return current_server.accept()

def init_blocking_socket(current_server,state=True):
    # Set the socket into Non-blocking I/O mode
    current_server.setblocking(state)
    return True

def accept_connection(current_server):
    connection, address = accept_socket(current_server)
    print(f"Accepted connection ${address}")
    make_connection_non_block = init_blocking_socket(connection, False)
    if make_connection_non_block == True:
        data = types.SimpleNamespace(address=address, inb=b'', outb=b'')
        events = selectors.EVENT_READ | selectors.EVENT_WRITE
        register_selector(connection, events, data)

def service_connection(key, mask):
    current_server = key.fileobj
    data = key.data
    if mask & selectors.EVENT_READ:
        recv_data = current_server.recv(1024)
        if recv_data: 
            data.outb += recv_data
        else:
            print(f"Closing connection ${data.address}")
            unregister_selector(current_server)
            close_socket(current_server)

    if mask & selectors.EVENT_WRITE:
        if data.outb:
            print(f"Echoing ${data.outb} to ${data.address}")
            is_sent = send_socket(current_server, data.outb)
            data.outb = data.outb[is_sent:]

def run_event_loop():
    try:
        while IS_RUNNING:
            default_selectors = get_default_selectors()
            running_events = default_selectors.select(timeout=None)
            for key, mask in running_events:
                if key.data is None:
                    accept_connection(key.fileobj)
                else:
                    service_connection(key, mask)
    except KeyboardInterrupt:
        print("Closing server...")
    finally:
        close_selectors()

def main():
    args = get_args()
    if len(args) != 3:
        print(f"Usage: <host_ip_address> <port#>")
        sys.exit(1)
    else:
        server = create_socket()
        if server["state"] == True:
            is_socket_binded =  bind_socket(server["instance"], args[1], int(args[2]))
            if is_socket_binded == True:
                is_server_running = listen_socket(server["instance"])
                if is_server_running == True:
                    print(f"Listening on {args[1]} {args[2]}")
                    is_server_not_blocking_state = init_blocking_socket(server["instance"], False)
                    if is_server_not_blocking_state == True:
                        register_selector(server["instance"], selectors.EVENT_READ)
                        run_event_loop()

if __name__ == "__main__":
    IS_RUNNING = True
    main()
