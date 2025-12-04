#!/usr/bin/python3
"""This is just a doc"""


import http.server
import json


class Handler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/data':
            data = {"name": "John", "age": 30, "city": "New York"}
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()

            self.wfile.write(json.dumps(data).encode())
        elif self.path == '/':
            message = 'Hello, this is a simple API!'
            self.send_response(200)
            self.send_header('Content-type', 'text')
            self.end_headers()

            self.wfile.write(json.dumps(message).encode())
        elif self.path == '/info':
            data = {"version": "1.0", "description": "A simple API built with http.server"}
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(data).encode())
        else:
            self.send_response(404)
            self.send_header('Content-type', 'text')
            self.end_headers()

            self.wfile.write(json.dumps('404 Not Found').encode())

server = http.server.HTTPServer(('localhost', 8000), Handler)
server.serve_forever()
