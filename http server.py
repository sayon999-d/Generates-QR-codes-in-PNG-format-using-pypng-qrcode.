import http.server
import socket
import socketserver
import webbrowser
import pyqrcode
import os

# Port for server
PORT = 8010

# Change working directory to Desktop (OneDrive path assumed)
desktop = os.path.join(os.environ.get('USERPROFILE', ''), 'OneDrive')
os.chdir(desktop)

# HTTP handler
Handler = http.server.SimpleHTTPRequestHandler

# Get local IP address
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
local_ip = s.getsockname()[0]
s.close()

# Full URL
IP = f"http://{local_ip}:{PORT}"

# Create QR Code
qr = pyqrcode.create(IP)
qr.svg("myqr.svg", scale=8)

# Open QR Code in browser
webbrowser.open('myqr.svg')

# Start server
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Serving at port {PORT}")
    print(f"Type in your browser: {IP}")
    print("Or scan the QR code")
    httpd.serve_forever()
