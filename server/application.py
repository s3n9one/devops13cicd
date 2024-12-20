"""Module for demonstration purposes"""
import http.server
import socketserver


PORT = 8000

"""Test class for demonstrarion purposes"""
class TestMe():
    """Return the number 5"""
    def take_five(self):
        return 5
    """Return the port number"""
    def port(self):
        return PORT

if __name__ == '__main__':
    Handler = http.server.SimpleHTTPRequestHandler

    with socketserver.TCPServer(("", PORT), Handler) as http:
        print("serving at port", PORT)
        http.serve_forever()
