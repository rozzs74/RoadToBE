
# Securing Sockets using SSL (Secure Socket Layer)
# Author: John Royce Punay
# Date created: March 3, 2020 6:10 PM
# Combo for IPV4 and IPV6 


import socket
import ssl 


hostname = 'www.python.org'
context = ssl.create_default_context()

print(ssl)
# create_connection is a higher level function of connect socket module
with socket.create_connection((hostname, 5000)) as my_socket:
     with context.wrap_socket(my_socket, server_hostname=hostname) as secured_socket:
         print(secured_socket.version())
