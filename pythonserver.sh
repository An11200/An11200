import os
from http.server import HTTPServer, CGIHTTPRequestHandler
# Make sure the server is created at current directory
os.chdir('.')
# Create server object listening the port 8000
server_object = HTTPServer(server_address=('', 8000), RequestHandlerClass=CGIHTTPRequestHandler)
print("Starting at port number 8000")
# Start the web server
server_object.serve_forever()