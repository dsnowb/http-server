from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs
from cowpy import cow
import json

PORT = 3000

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    '''Handles GET and POST requests to localhost endpoints'''

    def do_GET(self):
        '''handle GET requests'''
        
        # Parse out path and query string
        path = urlparse(self.path)
        qs = parse_qs(path.query)

        # Root endpoint
        if path.path == '/':
            self.send_response(200)
            self.end_headers()

            with open('index.html') as f:
                fdata = f.read()
                self.wfile.write(fdata.encode('utf8'))
            return

        # Cowsay endpoint
        elif path.path == '/cowsay':
            self.send_response(200)
            self.end_headers()

            with open('cowsay.html') as f:
                fdata = f.read()
                self.wfile.write(fdata.encode('utf8'))
            return

        # Cow endpoint
        elif path.path == '/cow':
            koala = cow.Koala()
            
            try:
                msg = json.loads(qs['msg'][0])
            except json.decoder.JSONDecodeError:
                msg = qs['msg'][0]
            except KeyError:
                self.send_response(400)
                self.end_headers()
                self.wfile.write(b'400 Error - Bad Request')
                return

            self.send_response(200)
            self.end_headers()
            self.wfile.write(koala.milk(msg).encode('utf8'))
            return

        # All other URI's
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b'404 - File not Found')

    def do_POST(self):
        '''Handle post requests'''
        
        # Parse out path and query string
        path = urlparse(self.path)
        qs = parse_qs(path.query)

        # Cow endpoint
        if path.path == '/cow':
            koala = cow.LukeKoala()
            try:
                msg = json.loads(qs['msg'][0])
            except json.decoder.JSONDecodeError:
                msg = qs['msg'][0]
            except KeyError:
                self.send_response(400)
                self.end_headers()
                self.wfile.write(b'400 Error - Bad Request')
                return

            json_dict = {"content" : koala.milk(msg)}

            self.send_response(200)
            self.end_headers()
            self.wfile.write(json.dumps(json_dict).encode('utf8'))
            return

        # All other URI's
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b'404 - File not Found')


def create_server():
    '''Instantiate HTTPServer on localhost:PORT'''
    return HTTPServer(('127.0.0.1',PORT), SimpleHTTPRequestHandler)


def run_forever():
    '''Begin serving'''

    svr = create_server()
    print('Starting server on port {}'.format(PORT))

    try:
        svr.serve_forever()
    except KeyboardInterrupt:
        svr.shutdown()
        svr.server_close()

if __name__ == "__main__":
    run_forever()
