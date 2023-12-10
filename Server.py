from http.server import BaseHTTPRequestHandler, HTTPServer
import socket

class RequestHandler(BaseHTTPRequestHandler):
    request_count = 0

    @classmethod
    def increment_counter(cls):
        cls.request_count += 1

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(f'Hello, this is a simple server! Total requests: {RequestHandler.request_count}'.encode('utf-8'))
        self.wfile.flush()
        RequestHandler.increment_counter()

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        
        print(f"Received POST request:\n{post_data.decode('utf-8')}")
        
        RequestHandler.increment_counter()

        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.send_header('Cache-Control', 'no-store')
        self.end_headers()
        self.wfile.write(f'Request received successfully! Total requests: {RequestHandler.request_count}'.encode('utf-8'))
        self.wfile.flush()

def run(server_class=HTTPServer, handler_class=RequestHandler, port=8000):
    host_name = socket.gethostbyname(socket.gethostname())
    server_address = (host_name, port)
    
    httpd = server_class(server_address, handler_class)
    print(f'Starting server on {host_name}:{port}...')
    httpd.serve_forever()

if __name__ == '__main__':
    run()
