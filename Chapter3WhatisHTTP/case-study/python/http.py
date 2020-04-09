# Author: John Royce Punay
# Date created: April 9, 2020 6:44 PM




import http.server
import socketserver

PORT = 8000

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()




# Resources
# https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=1&ved=2ahUKEwiLl_bglNvoAhXLaN4KHVh3BgwQFjAAegQIARAB&url=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fhttp.html&usg=AOvVaw3PfbGGHNvf3aFJ53qSxvA3