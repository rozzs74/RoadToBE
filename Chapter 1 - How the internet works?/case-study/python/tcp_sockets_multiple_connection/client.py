
import selectors
import sys
import types
import socket

sel = selectors.DefaultSelector()

def close_sys():
    sys.exit(1)

def get_args():
    return sys.argv

def close_selectors():
    sel.close()

def unregister_selector(current_connection):
    sel.unregister(current_connection)
    return True

def register_selector(current_connection, event, data=None):
    sel.register(current_connection, event, data)
    return True

def get_address_family_ipv4():
    return socket.AF_INET

def get_socket_stream():
    return socket.SOCK_STREAM

def connect_to_socket(current_connection, address):
    current_connection.connect_ex(address)

def create_socket():
    af_ipv4 = get_address_family_ipv4()
    socket_stream = get_socket_stream()
    server = socket.socket(af_ipv4, socket_stream)
    return { 
        "instance": server,
        "state": True
    }
def send_socket(current_connection, data):
    return current_connection.send(data)

def close_socket(current_connection):
    current_connection.close()
    return True

def init_blocking_socket(current_connection,state=True):
    # Set the socket into Non-blocking I/O mode
    current_connection.setblocking(state)
    return True

def start_connections(host_ip_address, port_number, number_connections):
    connection_id = 0
    client_messages = [b"Hey 1", b"Hey 2", b"Hey 3"]
    for i in range(0, number_connections):
        connection_id = i + 1
        print(f"Connection started connection id: {connection_id} to {(host_ip_address, port_number)}....")
        connection = create_socket()
        if connection["state"] == True:
            is_conn_not_blocking_state = init_blocking_socket(connection["instance"], False)
            if is_conn_not_blocking_state == True:
                connect_to_socket(connection["instance"], (host_ip_address, port_number))
                running_events = selectors.EVENT_READ | selectors.EVENT_WRITE
                data = types.SimpleNamespace(
                    connection_id = connection_id,
                    msg_total = sum(len(m) for m in client_messages),
                    recv_total = 0,
                    messages = list(client_messages),
                    outb=b""
                )
                register_selector(connection["instance"], running_events, data)

def service_connection(key, mask):
    current_connection = key.fileobj
    data = key.data
    if mask & selectors.EVENT_READ:
        recv_data = current_connection.recv(1024)
        if recv_data: 
            print(f"Client received!: {repr(recv_data)} from connection {data.connection_id}")
            data.recv_total += len(recv_data)
        if not recv_data or data.recv_total == data.msg_total:
            print(f"Client closing connection {data.connection_id}")
            unregister_selector(current_connection)
            close_socket(current_connection)

    if mask & selectors.EVENT_WRITE:
        if not data.outb and data.messages:
            data.outb = data.messages.pop(0)
        if data.outb:
            print(f"Sending {repr(data.outb)} to connection {data.connection_id}")
            sent = send_socket(current_connection, data.outb)
            data.outb = data.outb[sent:]

def run_event_loop():
    try:
        while True:
            running_events = sel.select(timeout=None)
            if running_events:
                for key, mask in running_events:
                    service_connection(key, mask)
            if not sel.get_map():
                break
    except KeyboardInterrupt:
        print("Closing client connection...")
    finally:
        close_selectors()

def main():
    args = get_args()
    if len(args) != 4:
        print(f"Usage: <host_ip_address> <port#> <number of connections>")
        close_sys()
    else:
        host_ip_address, port_number, number_connections = args[1:4]
        start_connections(host_ip_address, int(port_number), int(number_connections))
        run_event_loop()
        
if __name__ == "__main__":
    main()