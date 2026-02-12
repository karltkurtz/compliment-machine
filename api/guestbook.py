from http.server import BaseHTTPRequestHandler
import json
import os

GUESTBOOK_FILE = '/tmp/guestbook_entries.json'

def load_guestbook():
    """Load guestbook from file"""
    try:
        if os.path.exists(GUESTBOOK_FILE):
            with open(GUESTBOOK_FILE, 'r') as f:
                return json.load(f)
    except:
        pass
    return []

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        """Handle GET request"""
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        
        entries = load_guestbook()
        # Sort by timestamp, newest first
        entries.sort(key=lambda x: x.get('timestamp', ''), reverse=True)
        self.wfile.write(json.dumps(entries).encode())
        return
