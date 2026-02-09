from http.server import HTTPServer, BaseHTTPRequestHandler
import ssl

class LogOnlyHandler(BaseHTTPRequestHandler):
    def do_GET(self): self.log_and_close()
    def do_POST(self): self.log_and_close()
    def do_PUT(self): self.log_and_close()
    def do_DELETE(self): self.log_and_close()
    
    def log_and_close(self):
        content_length = int(self.headers.get("Content-Length", 0))
        body = self.rfile.read(content_length).decode("utf-8") if content_length else ""
        print("\n" + "="*50, flush=True)
        print(f"{self.command} {self.path}", flush=True)
        print(f"Headers: {dict(self.headers)}", flush=True)
        if body: print(f"Body: {body}", flush=True)
        print("="*50, flush=True)
    
    def log_message(self, format, *args): pass

httpd = HTTPServer(("", 8443), LogOnlyHandler)

# Use SSLContext instead of wrap_socket
context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain(certfile="/cert.pem", keyfile="/key.pem")
httpd.socket = context.wrap_socket(httpd.socket, server_side=True)

print("HTTPS server listening on port 8443...", flush=True)
httpd.serve_forever()
