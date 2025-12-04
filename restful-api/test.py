#!/usr/bin/python3
import http.server
import json

class Tutucu(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/salam':
            self.send_response(200)
            self.send_header('hello', 'salaaam')
            self.end_headers()

            response = {'message': 'salammeleyki'}
            self.wfile.write(json.dumps(response).encode())
        else:
            self.send_response(404)
            self.end_headers()

server = http.server.HTTPServer(('localhost', 8000), Tutucu)
print('Server is running on localhost')
server.serve_forever()
