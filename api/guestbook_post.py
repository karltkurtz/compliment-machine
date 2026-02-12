from http.server import BaseHTTPRequestHandler
import json
import os
from datetime import datetime

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

def save_guestbook(entries):
    """Save guestbook to file"""
    try:
        with open(GUESTBOOK_FILE, 'w') as f:
            json.dump(entries, f)
    except:
        pass

class handler(BaseHTTPRequestHandler):
    def do_POST(self):
        """Handle POST request"""
        try:
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            data = json.loads(post_data.decode('utf-8'))
            
            # Validate
            if not data.get('name') or not data.get('message'):
                self.send_response(400)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({'error': 'Name and message required'}).encode())
                return
            
            # Create entry
            entry = {
                'name': data['name'][:50],
                'email': data.get('email', '')[:100],
                'website': data.get('website', '')[:200],
                'message': data['message'][:500],
                'timestamp': datetime.now().isoformat()
            }
            
            # Load, add, save
            entries = load_guestbook()
            entries.insert(0, entry)
            entries = entries[:100]  # Keep last 100
            save_guestbook(entries)
            
            self.send_response(201)
            self.send_header('Content-type', 'application/json')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(json.dumps({'success': True, 'entry': entry}).encode())
            
        except Exception as e:
            self.send_response(500)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({'error': str(e)}).encode())
    
    def do_OPTIONS(self):
        """Handle OPTIONS for CORS"""
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()
